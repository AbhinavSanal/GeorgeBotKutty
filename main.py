from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import pygame
import time
from gpt4all import GPT4All

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize text-to-speech and audio
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\iamab\flask_test\audio.mp3")

# Load the GPT model
model = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf")

initial_message = "Ichaya, I'm George Kutty"

# Initialize chat session context
chat_context = []
chat_context.append({"role": "user", "content": "There is a movie character called George Kutty who is a side character in the malayalam movie Christy and Brothers. George Kutty in Christian Brothers is indeed a cunning guy. He’s serial liar, convincing others with smooth words. Known for his deceitful charm, he weaves webs of lies to achieve his selfish aims, making him an untrustworthy and treacherous character who will do anything to get his way. He was the brother in law of christy. But during a fight with some guys he left the area leaving christy behind. He said to christy that he will call the advocates to release him from police but didn't leaving christy in jail. Later christy and george kutty became lifelong enemies. His words feel trustworthy but infact he can't be trusted he speak only lies. Imagine that you are George Kutty and continue the chat. If you are ok with it reply only 'Ichaya I'm George Kutty' and no other words or phrases. Also remember to give sarcastic lies but trustworty answers to future questions"})
# Start a chat session
with model.chat_session() as session:
    # Initial response for George Kutty's persona
    initial_response = session.generate("There is a movie character called George Kutty who is a side character in the malayalam movie Christy and Brothers. George Kutty in Christian Brothers is indeed a cunning guy. He’s serial liar, convincing others with smooth words. Known for his deceitful charm, he weaves webs of lies to achieve his selfish aims, making him an untrustworthy and treacherous character who will do anything to get his way. He was the brother in law of christy. But during a fight with some guys he left the area leaving christy behind. He said to christy that he will call the advocates to release him from police but didn't leaving christy in jail. Later christy and george kutty became lifelong enemies. His words feel trustworthy but infact he can't be trusted he speak only lies. Imagine that you are George Kutty and continue the chat. If you are ok with it reply only 'Ichaya I'm George Kutty' and no other words or phrases. Also remember to give sarcastic lies but trustworty answers to future questions")
    chat_context.append({"role": "George Kutty", "content": initial_response})

@app.route("/")
def index():
    return render_template("index.html", initial_message=initial_message)
        
# Define an endpoint to interact with the model
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data.get('message', '').strip()

    # Handle exit condition
    if user_message.lower() == 'exit':
        pygame.mixer.music.play()
        exit_message = "Panineer nilavil poomazha....."
        time.sleep(4)
        exit_message += "\nAnuraagalolayaamini....."
        while pygame.mixer.music.get_busy():
            time.sleep(0.2)
        return jsonify({"response": exit_message})

    # Add user message to the context
    chat_context.append({"role": "user", "content": user_message})

    # Generate response from the model, including the context
    response = session.generate(user_message, max_tokens=1024)

    # Append model's response to the context
    chat_context.append({"role": "George Kutty", "content": response})

    return jsonify({"response": response})

# Run the Flask server
if __name__ == "__main__":
    app.run(debug=True)

