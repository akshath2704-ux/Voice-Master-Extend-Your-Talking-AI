import pyttsx3
import random
import datetime
import time

class VoiceMasterPlus:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)  
        self.engine.setProperty('volume', 1.0)
        self.greetings = [
            "Hello there! How can I help you today?",
            "Hi! Voice Master Plus at your service!",
            "Greetings! Ready to chat?",
            "Hey! What shall we talk about?"
        ]
        
        self.jokes = [
            "Why don't robots ever get scared? Because they have nerves of steel!",
            "I would tell you a joke about AI, but I'm afraid you wouldn't get it.",
            "Why did the computer go to the doctor? Because it caught a virus!"
        ]
        
        self.is_running = True

    def speak(self, text):
        """Core TTS Concept"""
        print(f"AI: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def handle_command(self, user_input):
        """Command interpretation concept"""
        user_input = user_input.lower().strip()

        if user_input in ['exit', 'quit', 'bye', 'goodbye']:
            self.speak("Goodbye! Shutting down Voice Master Plus.")
            self.is_running = False
            
        elif 'hello' in user_input or 'hi' in user_input:
            response = random.choice(self.greetings)
            self.speak(response)
            
        elif 'time' in user_input:
            now = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {now}")
            
        elif 'joke' in user_input:
            joke = random.choice(self.jokes)
            self.speak(joke)
            
        elif 'your name' in user_input:
            self.speak("I am Voice Master Plus, your extended talking AI companion!")
            
        elif 'how are you' in user_input:
            responses = ["I am doing fantastic! Thanks for asking.", 
                         "All systems operational!",
                         "I'm great and ready to talk!"]
            self.speak(random.choice(responses))
            
        elif user_input.startswith("say "):
            message = user_input[4:]
            self.speak(message)
            
        elif 'clear' in user_input or 'speed' in user_input:
            if 'fast' in user_input:
                self.engine.setProperty('rate', 250)
                self.speak("Speeding up!")
            elif 'slow' in user_input:
                self.engine.setProperty('rate', 130)
                self.speak("Slowing down... now speaking slowly.")
            else:
                self.engine.setProperty('rate', 180)
                self.speak("Voice reset to normal.")
        else:
            self.speak(f"You said: {user_input}. I am learning to respond to that. Try saying 'joke', 'time', 'say hello', or 'bye'.")

    def start(self):
        """Main Application Loop"""
        self.speak(random.choice(self.greetings))
        print("\n--- Voice Master+ is listening (Type your commands) ---")
        print("Commands: hello, time, joke, say [text], fast, slow, bye\n")

        while self.is_running:
            try:
                user_text = input("You: ")
                
                if not user_text.strip():
                    continue
                    
                self.handle_command(user_text)
                
            except KeyboardInterrupt:
                self.speak("Interrupted. Goodbye!")
                break
if __name__ == "__main__":
    ai = VoiceMasterPlus()
    ai.start()