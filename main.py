from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-poem', methods=['POST'])
def generate_poem():
    try:
        data = request.get_json()
        feeling = data.get('feeling')

        prompt = f"Write a beautiful, poetic song that reflects this human emotion: '{feeling}'. Make it lyrical and musical, like a verse and chorus."

        # ========== SAFETY NOTE ==========
        # 🔒 API access is disabled in this version.
        # 🛠️ To enable OpenAI API, uncomment and fill in your credentials below:

        # import openai
        # openai.api_key = "your_openai_api_key"
        # project_id = "your_project_id"

        # client = openai.OpenAI(
        #     api_key=openai.api_key,
        #     default_headers={"OpenAI-Project": project_id}
        # )

        # response = client.chat.completions.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "system", "content": "You are a poetic assistant..."},
        #         {"role": "user", "content": prompt}
        #     ],
        #     max_tokens=150
        # )

        # poem = response.choices[0].message.content
        # return jsonify({"poem": poem})

        # ========== FALLBACK RESPONSE ==========
        fallback_responses = [
            f"🎵 A song born from your heart: '{feeling[:30]}...' 🎵\n\nVerse:\nIn the melody of your words\nI hear the whispers of your soul\nEvery feeling a note that rings true\nIn the symphony that makes you whole\n\nChorus:\nSing your story, let it flow\nLet the world around you know\nThat in your heart there beats a song\nWhere all our voices belong",
            f"🎶 From the depths of '{feeling[:25]}...' 🎶\n\nVerse 1:\nYour emotions paint the sky\nWith colors words cannot describe\nEach heartbeat writes a melody\nOf human truth and honesty\n\nChorus:\nThis is your moment to shine\nYour story weaving through time\nEvery word a precious note\nIn life's most beautiful quote",
            f"🌟 Inspired by: '{feeling[:20]}...' 🌟\n\nVerse:\nIn the garden of your heart\nWhere feelings bloom like art\nI find the seeds of poetry\nGrowing wild and growing free"
            # 👉 You can add more creative fallback responses here
        ]

        selected_response = random.choice(fallback_responses)
        return jsonify({"poem": selected_response})
    
    except Exception as e:
        print(f"Error generating poem: {e}")
        return jsonify({"poem": "Sorry, we couldn't create your song right now. Please try again later."})

# Run the app (for Replit or local testing)
app.run(host='0.0.0.0', port=3000)
