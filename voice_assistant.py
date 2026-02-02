"""
Voice Assistant Project - Oasis Infobyte Internship
A voice-activated assistant that can perform various tasks based on voice commands
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys

class VoiceAssistant:
    def __init__(self):
        # Initialize the speech recognizer
        self.recognizer = sr.Recognizer()
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        
        # Configure speech properties
        self.engine.setProperty('rate', 180)  # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
        
        # Get available voices and set a voice
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female (usually)
        
        self.name = "Assistant"
        
    def speak(self, text):
        """Convert text to speech"""
        print(f"{self.name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen(self):
        """Listen to user's voice command and convert to text"""
        with sr.Microphone() as source:
            print("Listening...")
            # Adjust for ambient noise
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("Processing...")
                
                # Using Google's speech recognition
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
                
            except sr.WaitTimeoutError:
                self.speak("I didn't hear anything. Please try again.")
                return ""
            except sr.UnknownValueError:
                self.speak("Sorry, I couldn't understand that. Could you repeat?")
                return ""
            except sr.RequestError:
                self.speak("Sorry, there's an issue with the speech recognition service.")
                return ""
            except Exception as e:
                print(f"Error: {e}")
                return ""
    
    def greet_user(self):
        """Greet the user based on time of day"""
        hour = datetime.datetime.now().hour
        
        if hour < 12:
            greeting = "Good morning!"
        elif hour < 18:
            greeting = "Good afternoon!"
        else:
            greeting = "Good evening!"
            
        self.speak(f"{greeting} I'm your voice assistant. How can I help you today?")
    
    def get_time(self):
        """Tell the current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")
    
    def get_date(self):
        """Tell the current date"""
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        day = datetime.datetime.now().strftime("%A")
        self.speak(f"Today is {day}, {current_date}")
    
    def search_web(self, query):
        """Search the web for information"""
        search_query = query.replace("search for", "").replace("search", "").strip()
        
        if search_query:
            self.speak(f"Searching for {search_query}")
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
        else:
            self.speak("What would you like me to search for?")
    
    def open_website(self, command):
        """Open popular websites"""
        websites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "github": "https://www.github.com",
            "stackoverflow": "https://stackoverflow.com",
            "linkedin": "https://www.linkedin.com",
        }
        
        for site, url in websites.items():
            if site in command:
                self.speak(f"Opening {site}")
                webbrowser.open(url)
                return True
        return False
    
    def tell_joke(self):
        """Tell a programming joke"""
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
            "What's a programmer's favorite hangout place? The Foo Bar!"
        ]
        import random
        self.speak(random.choice(jokes))
    
    def process_command(self, command):
        """Process the voice command and execute appropriate action"""
        
        if not command:
            return True
            
        # Exit commands
        if any(word in command for word in ["exit", "quit", "bye", "goodbye"]):
            self.speak("Goodbye! Have a great day!")
            return False
        
        # Time
        elif "time" in command:
            self.get_time()
        
        # Date
        elif "date" in command or "today" in command:
            self.get_date()
        
        # Search
        elif "search" in command:
            self.search_web(command)
        
        # Open websites
        elif "open" in command:
            if not self.open_website(command):
                self.speak("I'm not sure which website to open.")
        
        # Joke
        elif "joke" in command:
            self.tell_joke()
        
        # Help
        elif "help" in command or "what can you do" in command:
            self.speak("""I can help you with the following:
                Say 'time' to know the current time.
                Say 'date' to know today's date.
                Say 'search for' followed by your query to search the web.
                Say 'open' followed by a website name like YouTube, Google, or GitHub.
                Say 'joke' to hear a programming joke.
                Say 'exit' or 'goodbye' to close the assistant.""")
        
        # Unknown command
        else:
            self.speak("I'm not sure how to help with that. Say 'help' to know what I can do.")
        
        return True
    
    def run(self):
        """Main loop to run the voice assistant"""
        self.greet_user()
        
        running = True
        while running:
            # Listen for command
            command = self.listen()
            
            # Process the command
            running = self.process_command(command)

def main():
    """Main function to start the voice assistant"""
    print("=" * 50)
    print("Voice Assistant - Oasis Infobyte Internship")
    print("=" * 50)
    
    try:
        assistant = VoiceAssistant()
        assistant.run()
    except KeyboardInterrupt:
        print("\n\nAssistant stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
