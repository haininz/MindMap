from flask import Flask, jsonify, request
from flask_cors import CORS

import openai

# import spacy
# nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

# Set CORS to allow specific origin with credentials
CORS(app)

client = openai.OpenAI(api_key="sk-proj-lUIm1n1ZvT6xfxElbyoHT3BlbkFJgyvhdLxJ4lENn8vxRron")

def generate_mindmap(user_input):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant for generating mind map, and you are responsible for extracting a main topic and three subtopics from the given text."},
            {"role": "user", "content": user_input}
        ]
    )
    content = completion.choices[0].message.content
    lines = content.split('\n')
    main_topic = lines[0].split(': ')[1]
    subtopics = [line.split(': ')[1] for line in lines[2:5]]
    return {"main_topic": main_topic, "subtopics": subtopics}

@app.route('/submit', methods=['POST'])
def print_input():
    user_input = request.json['userInput']
    print("Received input:", user_input)
    # print("Result from GPT-3.5: ", generate_mindmap(user_input))
    # return jsonify({"status": "Input received"})
    mindmap_data = generate_mindmap(user_input)
    return jsonify(mindmap_data)

if __name__ == '__main__':
    app.run(debug=True)
