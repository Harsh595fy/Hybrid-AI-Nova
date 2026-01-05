from flask import Flask, request, jsonify, render_template
from ai_engine import get_ai_response

app = Flask(__name__)

# --- Routes ---

@app.route("/")
def home():
    # Directly serves the Chat Interface
    return render_template("chat.html")

@app.route("/api/ai/chat", methods=["POST"])
def ai_chat():
    data = request.json
    user_message = data.get("message", "")
    subject = data.get("subject", "General")
    
    # Check if user explicitly wants to use local/offline mode
    # (You can toggle this logic based on your needs)
    use_offline = False 
    
    # Get response from the AI Engine
    reply = get_ai_response(user_message, subject=subject, use_local=use_offline)
        
    return jsonify({"reply": reply, "success": True})

if __name__ == "__main__":
    print("🚀 Nova AI Server Running on http://127.0.0.1:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)
