import google.generativeai as genai
from flask import Flask, request, jsonify

# Set up Gemini API Key
genai.configure(api_key="AIzaSyDibbryO_jfUKTz9bB5vs3Hb7FTOYgIJXY")

app = Flask(__name__)

def chat_with_gemini(user_input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)
    return response.text

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = chat_with_gemini(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)