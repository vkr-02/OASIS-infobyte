"""
Demo Script - Voice Assistant
Demonstrates the assistant's capabilities without requiring voice input
Run this to see what the assistant can do!
"""

import sys
import time

class DemoAssistant:
    """Simulated assistant for demonstration purposes"""
    
    def __init__(self):
        self.name = "Demo Assistant"
    
    def simulate_command(self, command):
        """Simulate a voice command"""
        print(f"\n{'='*60}")
        print(f"🎤 User says: '{command}'")
        print(f"{'='*60}")
        time.sleep(0.5)
    
    def simulate_response(self, response):
        """Simulate assistant response"""
        print(f"🤖 {self.name}: {response}")
        time.sleep(1)
    
    def demo_basic_commands(self):
        """Demonstrate basic commands"""
        print("\n" + "="*60)
        print("BASIC COMMANDS DEMONSTRATION")
        print("="*60)
        
        demos = [
            ("Hello", "Good morning! I'm your voice assistant. How can I help you today?"),
            ("What time is it?", "The current time is 02:30 PM"),
            ("What's the date?", "Today is Sunday, February 01, 2026"),
            ("Tell me a joke", "Why do programmers prefer dark mode? Because light attracts bugs!"),
            ("Search for Python tutorials", "Searching for Python tutorials... Opening Google search."),
            ("Open YouTube", "Opening YouTube"),
        ]
        
        for command, response in demos:
            self.simulate_command(command)
            self.simulate_response(response)
    
    def demo_advanced_commands(self):
        """Demonstrate advanced commands"""
        print("\n" + "="*60)
        print("ADVANCED COMMANDS DEMONSTRATION")
        print("="*60)
        
        demos = [
            ("What's the weather?", "The weather in New York is partly cloudy. Temperature is 18 degrees Celsius with 65% humidity."),
            ("Who is Albert Einstein?", "According to Wikipedia: Albert Einstein was a German-born theoretical physicist who developed the theory of relativity..."),
            ("Calculate 25 plus 37", "The answer is 62"),
            ("Remind me to buy groceries", "Reminder set: buy groceries"),
            ("List my reminders", "You have 1 reminder: Reminder 1: buy groceries"),
        ]
        
        for command, response in demos:
            self.simulate_command(command)
            self.simulate_response(response)
    
    def demo_error_handling(self):
        """Demonstrate error handling"""
        print("\n" + "="*60)
        print("ERROR HANDLING DEMONSTRATION")
        print("="*60)
        
        demos = [
            ("mumble mumble...", "Sorry, I couldn't understand that. Could you repeat?"),
            ("Do something impossible", "I'm not sure how to help with that. Say 'help' to know what I can do."),
            ("What's the weather in Mars?", "Unable to get weather for Mars. Please check the city name."),
        ]
        
        for command, response in demos:
            self.simulate_command(command)
            self.simulate_response(response)
    
    def demo_help_system(self):
        """Demonstrate help system"""
        print("\n" + "="*60)
        print("HELP SYSTEM DEMONSTRATION")
        print("="*60)
        
        self.simulate_command("Help")
        help_text = """I can help you with the following:
        Say 'time' to know the current time.
        Say 'date' to know today's date.
        Say 'search for' followed by your query to search the web.
        Say 'open' followed by a website name.
        Say 'weather' to get weather updates.
        Say 'joke' to hear a programming joke.
        Say 'calculate' for math operations.
        Say 'exit' or 'goodbye' to close the assistant."""
        self.simulate_response(help_text)

def print_header():
    """Print demo header"""
    print("\n" + "="*60)
    print(" "*15 + "VOICE ASSISTANT DEMO")
    print(" "*10 + "Oasis Infobyte Internship Project")
    print("="*60)
    print("\nThis demo shows what the voice assistant can do")
    print("without requiring a microphone or voice input.\n")
    print("In the actual application, you would speak these")
    print("commands, and the assistant would respond with voice.\n")

def print_footer():
    """Print demo footer"""
    print("\n" + "="*60)
    print("DEMO COMPLETE!")
    print("="*60)
    print("\nTo run the actual voice assistant:")
    print("  python voice_assistant.py")
    print("\nFor advanced features:")
    print("  python voice_assistant_advanced.py")
    print("\nFor installation testing:")
    print("  python test_installation.py")
    print("\n" + "="*60)

def main():
    """Main demo function"""
    try:
        print_header()
        
        demo = DemoAssistant()
        
        input("\nPress Enter to start the basic commands demo...")
        demo.demo_basic_commands()
        
        input("\nPress Enter to see advanced commands demo...")
        demo.demo_advanced_commands()
        
        input("\nPress Enter to see error handling demo...")
        demo.demo_error_handling()
        
        input("\nPress Enter to see help system demo...")
        demo.demo_help_system()
        
        print_footer()
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\nError during demo: {e}")

if __name__ == "__main__":
    main()
