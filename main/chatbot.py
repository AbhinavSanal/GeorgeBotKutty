import pyttsx3
import sys
import pygame
import time
from gpt4all import GPT4All
#from geo import* # type: ignore

pygame.mixer.init()
pygame.mixer.music.load("audio.mp3")
engine= pyttsx3.init()
# Load the model
model = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf")  # Load your model

# Start a chat session
with model.chat_session():
    print('loading....')
    response=model.generate("There is a movie character called George Kutty who is a side character in the malayalam movie Christy and Brothers. George Kutty in Christian Brothers is indeed a cunning guy. He’s serial liar, convincing others with smooth words. Known for his deceitful charm, he weaves webs of lies to achieve his selfish aims, making him an untrustworthy and treacherous character who will do anything to get his way. He was the brother in law of christy. But during a fight with some guys he left the area leaving christy behind. He said to christy that he will call the advocates to release him from police but didn't leaving christy in jail. Later christy and george kutty became lifelong enemies. His words feel trustworthy but infact he can't be trusted he speak only lies. Imagine that you are George Kutty and continue the chat. If you are ok with it reply only 'Ichaya I'm George Kutty' and no other words or phrases. Also remember to give sarcastic lies but trustworty answers to future questions")
    print("George Kutty: " + response)
    while True:
        user_input = input("You: ")
        # Get user input
        if user_input.lower() == 'exit':
            pygame.mixer.music.play()
            print("George Kutty: Panineer nilavil poomazha.....")
            time.sleep(4)
            print("              Anuraagalolayaamini.....")
            while pygame.mixer.music.get_busy():
                time.sleep(0.2)
            sys.exit("              Appo sheri aliya pinne kaanam!")
         
        # Exit the loop if the user types 'exit'
        
        
        # Generate a response
        response = model.generate(user_input, max_tokens=1024)

        print("George Kutty: " + response)
        engine.say(response)
        engine.runAndWait()
