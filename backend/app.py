from flask import Flask, jsonify, request
from flask_cors import CORS

import openai

# import spacy
# nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

# Set CORS to allow specific origin with credentials
CORS(app)

client = openai.OpenAI(api_key="YOUR_OPENAI_API_KEY")

# def generate_mindmap(user_input):
#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are an assistant for generating mind map, and you are responsible for extracting a main topic and three subtopics from the given text. A main topic will always be provided, but the subtopics may not. If you cannot find the subtopics, try to come up with three relevant subtopics based on the main topic."},
#             {"role": "user", "content": user_input}
#         ]
#     )
#     content = completion.choices[0].message.content
#     print("Content: ", content)
#     lines = content.split('\n')
#     main_topic = lines[0].split(': ')[1]
#     subtopics = [line.split(': ')[1] for line in lines[2:5]]
#     return {"main_topic": main_topic, "subtopics": subtopics}


def generate_mindmap(user_input):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant for extracting main topic and subtopics from the input. Please always provide a response in exactly four lines: the first line is the main topic, and the next three lines are the subtopics, each on its own line. There should be no labels, prefixes, or additional formatting."},
            {"role": "user", "content": user_input}
        ]
    )
    content = completion.choices[0].message.content
    print("Message: ", completion.choices[0].message)
    lines = content.split('\n')
    if len(lines) >= 4:
        main_topic = lines[0].strip()
        subtopics = [line.strip() for line in lines[1:4]]
        return {"main_topic": main_topic, "subtopics": subtopics}
    else:
        return {"error": "Insufficient data returned"}



@app.route('/submit', methods=['POST'])
def print_input():
    user_input = request.json['userInput']
    print("Received input:", user_input)
    # print("Result from GPT-3.5: ", generate_mindmap(user_input))
    # return jsonify({"status": "Input received"})
    mindmap_data = generate_mindmap(user_input)
    print("Result from GPT-3.5: ", mindmap_data)
    return jsonify(mindmap_data)

if __name__ == '__main__':
    app.run(debug=True)
