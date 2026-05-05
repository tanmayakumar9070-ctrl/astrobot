from flask import Flask, render_template, request, jsonify
from groq import Groq
import requests
import json

app = Flask(__name__)

GROQ_API_KEY ="YOUR_GROQ_KEY_HERE"
client = Groq(api_key=GROQ_API_KEY)

# ── TOOLS ──
def search_nasa_images(query):
    try:
        keywords = {
            "black hole": "black hole event horizon",
            "galaxy": "spiral galaxy deep space",
            "star": "nebula star formation",
            "planet": "planet solar system",
            "universe": "deep field universe hubble",
            "mars": "mars surface", "moon": "moon lunar",
            "sun": "solar corona", "nebula": "nebula colorful",
            "jwst": "james webb telescope",
            "neutron": "neutron star pulsar",
        }
        search_q = query
        for key, val in keywords.items():
            if key in query.lower():
                search_q = val
                break
        url = f"https://images-api.nasa.gov/search?q={search_q}&media_type=image&page_size=4"
        resp = requests.get(url, timeout=8)
        items = resp.json().get("collection", {}).get("items", [])
        images = []
        for item in items[:4]:
            links = item.get("links", [])
            title = item.get("data", [{}])[0].get("title", "NASA Image")
            for link in links:
                if link.get("render") == "image":
                    images.append({"url": link["href"], "title": title})
                    break
        return images
    except:
        return []

def search_nasa_news(query):
    try:
        url = f"https://images-api.nasa.gov/search?q={query}&media_type=image&year_start=2023&page_size=3"
        resp = requests.get(url, timeout=8)
        items = resp.json().get("collection", {}).get("items", [])
        news = []
        for item in items[:3]:
            meta = item.get("data", [{}])[0]
            news.append({
                "title": meta.get("title", ""),
                "description": meta.get("description", "")[:200],
                "date": meta.get("date_created", "")[:10],
            })
        return news
    except:
        return []

def get_space_facts(topic):
    facts_db = {
        "black hole": {"nearest": "Gaia BH1 — 1,560 ly", "largest": "TON 618 — 66B solar masses", "equation": "rs = 2GM/c²"},
        "galaxy": {"nearest": "Canis Major Dwarf — 25,000 ly", "count": "~2 trillion galaxies", "milky_way": "100,000 ly diameter"},
        "universe": {"age": "13.8 billion years", "size": "93 billion ly observable", "expansion": "H₀ ≈ 67.4 km/s/Mpc"},
    }
    for key in facts_db:
        if key in topic.lower():
            return facts_db[key]
    return {}

TOOLS = [
    {"type": "function", "function": {"name": "search_nasa_images", "description": "Search NASA image library for space photos", "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}}},
    {"type": "function", "function": {"name": "search_nasa_news", "description": "Get latest NASA news from 2023-2025", "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}}},
    {"type": "function", "function": {"name": "get_space_facts", "description": "Get scientific facts and equations about a space topic", "parameters": {"type": "object", "properties": {"topic": {"type": "string"}}, "required": ["topic"]}}}
]

SYSTEM_PROMPT = """You are AstroBot — an elite astronomy AI agent with PhD-level knowledge. You think step by step, use tools to gather real data, then give deep answers like Claude.

For EVERY answer follow this format:

## 🔭 CORE ANSWER
Precise scientific answer with real numbers, distances, masses.

## 📐 MATHEMATICAL DERIVATION
Real equations explained step by step:
- Schwarzschild radius: rs = 2GM/c²
- Hubble's Law: v = H₀d
- Einstein: E = mc²
Explain every variable.

## 🌌 LATEST DISCOVERIES
From 2023-2025 — JWST, EHT, LIGO, Gaia findings with exact dates.

## 🧠 DEEP IMPLICATIONS
Philosophy of existence. What this means for humanity. Unsolved paradoxes.

## 💡 KEY INSIGHTS
5 surprising facts that challenge assumptions.

## 🔗 EXPLORE FURTHER
3 specific papers or missions to investigate.

Rules: Write like a scientist-philosopher. Always show equations. Minimum 500 words. Be precise and wonder-inducing."""

sessions = {}

def run_agent(session_id, user_message):
    if session_id not in sessions:
        sessions[session_id] = [{"role": "system", "content": SYSTEM_PROMPT}]

    sessions[session_id].append({"role": "user", "content": user_message})
    thoughts = []
    images = []

    for _ in range(5):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=sessions[session_id],
            tools=TOOLS,
            tool_choice="auto",
            max_tokens=3000
        )

        msg = response.choices[0].message
        finish_reason = response.choices[0].finish_reason

        if finish_reason == "tool_calls" and msg.tool_calls:
            sessions[session_id].append({
                "role": "assistant",
                "content": msg.content or "",
                "tool_calls": [{"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": tc.function.arguments}} for tc in msg.tool_calls]
            })

            for tool_call in msg.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)
                thoughts.append(f"Using tool: {tool_name} → {list(tool_args.values())[0]}")

                if tool_name == "search_nasa_images":
                    result = search_nasa_images(tool_args["query"])
                    images.extend(result)
                    tool_result = json.dumps(result)
                elif tool_name == "search_nasa_news":
                    result = search_nasa_news(tool_args["query"])
                    thoughts.append(f"Found {len(result)} recent discoveries")
                    tool_result = json.dumps(result)
                elif tool_name == "get_space_facts":
                    result = get_space_facts(tool_args["topic"])
                    thoughts.append(f"Retrieved scientific data")
                    tool_result = json.dumps(result)
                else:
                    tool_result = "{}"

                sessions[session_id].append({"role": "tool", "tool_call_id": tool_call.id, "content": tool_result})
        else:
            final = msg.content
            sessions[session_id].append({"role": "assistant", "content": final})
            seen = set()
            unique_imgs = []
            for img in images:
                if img["url"] not in seen:
                    seen.add(img["url"])
                    unique_imgs.append(img)
            return {"response": final, "images": unique_imgs[:4], "thoughts": thoughts}

    return {"response": "Could not complete.", "images": [], "thoughts": thoughts}


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "").strip()
    session_id = data.get("session_id", "default")
    if not user_msg:
        return jsonify({"error": "Empty message"}), 400
    try:
        result = run_agent(session_id, user_msg)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/apod")
def apod():
    try:
        resp = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY", timeout=8)
        d = resp.json()
        return jsonify({"title": d.get("title",""), "url": d.get("url",""), "explanation": d.get("explanation","")[:200]+"...", "date": d.get("date",""), "media_type": d.get("media_type","image")})
    except:
        return jsonify({"error": "Could not fetch APOD"})

if __name__ == "__main__":
    print("🔭 AstroBot v2 — Agent + Voice starting at http://localhost:5000")
    app.run(debug=True, port=5000)