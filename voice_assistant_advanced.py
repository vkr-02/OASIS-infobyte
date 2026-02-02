"""
Advanced Voice Assistant Project - Oasis Infobyte Internship
Enhanced version with NLP, email, weather updates, and more advanced features
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys
import json

# Advanced features (install via requirements.txt)
try:
    import requests
    WEATHER_AVAILABLE = True
except ImportError:
    WEATHER_AVAILABLE = False

try:
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    EMAIL_AVAILABLE = True
except ImportError:
    EMAIL_AVAILABLE = False

try:
    import wikipedia
    WIKIPEDIA_AVAILABLE = True
except ImportError:
    WIKIPEDIA_AVAILABLE = False


class AdvancedVoiceAssistant:
    def __init__(self):
        # Initialize the speech recognizer
        self.recognizer = sr.Recognizer()
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        
        # Configure speech properties
        self.engine.setProperty('rate', 180)
        self.engine.setProperty('volume', 0.9)
        
        # Set voice
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        
        self.name = "Advanced Assistant"
        
        # Load or create configuration
        self.config_file = "assistant_config.json"
        self.load_config()
        
        # Reminders list
        self.reminders = []
        
    def load_config(self):
        """Load configuration from file"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            # Default configuration
            self.config = {
                "user_name": "User",
                "email_address": "",
                "email_password": "",
                "weather_api_key": "",
                "default_city": "New York"
            }
            self.save_config()
    
    def save_config(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"{self.name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen to user's voice command with improved error handling"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Processing...")
                
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
                
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                self.speak("I couldn't understand that. Please try again.")
                return ""
            except sr.RequestError as e:
                self.speak("There's an issue with the speech recognition service.")
                print(f"Error: {e}")
                return ""
            except Exception as e:
                print(f"Unexpected error: {e}")
                return ""
    
    def greet_user(self):
        """Personalized greeting"""
        hour = datetime.datetime.now().hour
        
        if hour < 12:
            greeting = "Good morning"
        elif hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        
        user_name = self.config.get("user_name", "there")
        self.speak(f"{greeting} {user_name}! I'm your advanced voice assistant. How may I assist you today?")
    
    def get_time(self):
        """Tell current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")
    
    def get_date(self):
        """Tell current date"""
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        day = datetime.datetime.now().strftime("%A")
        self.speak(f"Today is {day}, {current_date}")
    
    def search_web(self, query):
        """Enhanced web search"""
        search_query = query.replace("search for", "").replace("search", "").strip()
        
        if search_query:
            self.speak(f"Searching for {search_query}")
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
        else:
            self.speak("What would you like me to search for?")
    
    def get_weather(self, city=None):
        """Get weather information using API"""
        if not WEATHER_AVAILABLE:
            self.speak("Weather feature requires the requests library. Please install it.")
            return
        
        if not self.config.get("weather_api_key"):
            self.speak("Weather API key not configured. Please set it up in the config file.")
            return
        
        if not city:
            city = self.config.get("default_city", "New York")
        
        try:
            api_key = self.config["weather_api_key"]
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": city,
                "appid": api_key,
                "units": "metric"
            }
            
            response = requests.get(base_url, params=params, timeout=5)
            data = response.json()
            
            if response.status_code == 200:
                temp = data["main"]["temp"]
                description = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                
                weather_report = f"The weather in {city} is {description}. "
                weather_report += f"Temperature is {temp} degrees Celsius with {humidity}% humidity."
                
                self.speak(weather_report)
            else:
                self.speak(f"Unable to get weather for {city}. Please check the city name.")
                
        except Exception as e:
            self.speak("Sorry, I couldn't fetch the weather information.")
            print(f"Weather error: {e}")
    
    def send_email(self, recipient, subject, body):
        """Send email functionality"""
        if not EMAIL_AVAILABLE:
            self.speak("Email feature is not available. Please install required libraries.")
            return
        
        if not self.config.get("email_address") or not self.config.get("email_password"):
            self.speak("Email credentials not configured. Please set them up in the config file.")
            return
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config["email_address"]
            msg['To'] = recipient
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Using Gmail SMTP
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.config["email_address"], self.config["email_password"])
            
            server.send_message(msg)
            server.quit()
            
            self.speak("Email sent successfully!")
            
        except Exception as e:
            self.speak("Sorry, I couldn't send the email.")
            print(f"Email error: {e}")
    
    def search_wikipedia(self, query):
        """Search Wikipedia for information"""
        if not WIKIPEDIA_AVAILABLE:
            self.speak("Wikipedia feature requires the wikipedia library.")
            return
        
        try:
            self.speak(f"Searching Wikipedia for {query}")
            result = wikipedia.summary(query, sentences=2)
            self.speak(result)
            
        except wikipedia.exceptions.DisambiguationError:
            self.speak("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            self.speak("I couldn't find information on that topic.")
        except Exception as e:
            self.speak("Sorry, I encountered an error while searching Wikipedia.")
            print(f"Wikipedia error: {e}")
    
    def set_reminder(self, reminder_text):
        """Set a simple reminder"""
        self.reminders.append({
            "text": reminder_text,
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.speak(f"Reminder set: {reminder_text}")
    
    def list_reminders(self):
        """List all reminders"""
        if not self.reminders:
            self.speak("You have no reminders.")
        else:
            self.speak(f"You have {len(self.reminders)} reminder(s):")
            for i, reminder in enumerate(self.reminders, 1):
                self.speak(f"Reminder {i}: {reminder['text']}")
    
    def calculate(self, expression):
        """Perform basic calculations"""
        try:
            # Clean the expression
            expression = expression.replace("what is", "").replace("calculate", "").strip()
            expression = expression.replace("plus", "+").replace("minus", "-")
            expression = expression.replace("times", "*").replace("multiplied by", "*")
            expression = expression.replace("divided by", "/")
            
            result = eval(expression)
            self.speak(f"The answer is {result}")
            
        except Exception as e:
            self.speak("Sorry, I couldn't calculate that.")
            print(f"Calculation error: {e}")
    
    def open_application(self, app_name):
        """Open applications on the computer"""
        applications = {
            "notepad": "notepad.exe" if sys.platform == "win32" else "gedit",
            "calculator": "calc.exe" if sys.platform == "win32" else "gnome-calculator",
            "browser": "start chrome" if sys.platform == "win32" else "google-chrome"
        }
        
        if app_name in applications:
            try:
                os.system(applications[app_name])
                self.speak(f"Opening {app_name}")
            except:
                self.speak(f"Sorry, I couldn't open {app_name}")
        else:
            self.speak("I don't know how to open that application.")
    
    def get_help(self):
        """Provide help information"""
        help_text = """Here's what I can do:
            Tell time and date.
            Search the web or Wikipedia.
            Get weather updates.
            Send emails if configured.
            Set and list reminders.
            Perform calculations.
            Open applications.
            Tell jokes.
            And much more! Just ask me."""
        self.speak(help_text)
    
    def process_command(self, command):
        """Process commands with natural language understanding"""
        
        if not command:
            return True
        
        # Exit commands
        if any(word in command for word in ["exit", "quit", "bye", "goodbye", "stop"]):
            self.speak("Goodbye! It was nice talking to you!")
            return False
        
        # Time
        elif "time" in command:
            self.get_time()
        
        # Date
        elif "date" in command or "what day" in command:
            self.get_date()
        
        # Weather
        elif "weather" in command:
            self.get_weather()
        
        # Search web
        elif "search" in command and "wikipedia" not in command:
            self.search_web(command)
        
        # Wikipedia
        elif "wikipedia" in command or "who is" in command or "what is" in command:
            query = command.replace("wikipedia", "").replace("who is", "").replace("what is", "").strip()
            self.search_wikipedia(query)
        
        # Email (example - would need more sophisticated parsing)
        elif "send email" in command:
            self.speak("Email feature requires configuration. Please set up your credentials.")
        
        # Reminder
        elif "remind me" in command or "set reminder" in command:
            reminder = command.replace("remind me to", "").replace("set reminder", "").strip()
            self.set_reminder(reminder)
        
        elif "list reminders" in command or "my reminders" in command:
            self.list_reminders()
        
        # Calculate
        elif "calculate" in command or "what is" in command and any(op in command for op in ["+", "-", "*", "/", "plus", "minus", "times", "divided"]):
            self.calculate(command)
        
        # Open application
        elif "open" in command:
            app = command.replace("open", "").strip()
            self.open_application(app)
        
        # Joke
        elif "joke" in command:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
                "Why do Java developers wear glasses? Because they don't C#!",
                "How many programmers does it take to change a light bulb? None, it's a hardware problem!"
            ]
            import random
            self.speak(random.choice(jokes))
        
        # Help
        elif "help" in command or "what can you do" in command:
            self.get_help()
        
        # Unknown
        else:
            self.speak("I'm not sure how to help with that. Say 'help' to see what I can do.")
        
        return True
    
    def run(self):
        """Main loop"""
        self.greet_user()
        
        running = True
        while running:
            command = self.listen()
            running = self.process_command(command)


def main():
    """Main function"""
    print("=" * 60)
    print("Advanced Voice Assistant - Oasis Infobyte Internship")
    print("=" * 60)
    print("\nNote: Some features require additional configuration.")
    print("Edit 'assistant_config.json' to set up email, weather API, etc.\n")
    
    try:
        assistant = AdvancedVoiceAssistant()
        assistant.run()
    except KeyboardInterrupt:
        print("\n\nAssistant stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
