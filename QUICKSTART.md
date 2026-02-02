# Quick Start Guide - Voice Assistant Project

## For Students New to Python Projects

### Step 1: Set Up Your Environment (5 minutes)

1. **Check Python Installation**
   ```bash
   python --version
   ```
   - You need Python 3.7 or higher
   - If not installed, download from [python.org](https://www.python.org/downloads/)

2. **Create a Project Folder**
   ```bash
   mkdir voice-assistant-project
   cd voice-assistant-project
   ```

3. **Download Project Files**
   - Place all the files in this folder:
     - `voice_assistant.py`
     - `voice_assistant_advanced.py`
     - `requirements.txt`
     - `test_installation.py`
     - `README.md`

### Step 2: Install Dependencies (10 minutes)

1. **Install Basic Requirements**
   ```bash
   pip install SpeechRecognition pyttsx3
   ```

2. **Install PyAudio (This is the tricky one!)**
   
   **Windows:**
   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```
   
   **Mac:**
   ```bash
   brew install portaudio
   pip install pyaudio
   ```
   
   **Linux:**
   ```bash
   sudo apt-get install python3-pyaudio
   ```

3. **Test Your Installation**
   ```bash
   python test_installation.py
   ```

### Step 3: Run the Basic Version (2 minutes)

1. **Start the Assistant**
   ```bash
   python voice_assistant.py
   ```

2. **Try These Commands:**
   - "What time is it?"
   - "What's the date?"
   - "Tell me a joke"
   - "Search for Python programming"
   - "Open YouTube"
   - "Exit"

### Step 4: Customize and Enhance

#### Add Your Name
Edit the code to personalize greetings:
```python
self.name = "Your Name's Assistant"  # Line ~20
```

#### Add More Jokes
Find the `tell_joke()` function and add your own jokes!

#### Add More Websites
In the `open_website()` function, add your favorite sites:
```python
"reddit": "https://www.reddit.com",
"twitter": "https://www.twitter.com",
```

### Step 5: Try Advanced Features (Optional)

1. **Install Advanced Dependencies**
   ```bash
   pip install requests wikipedia
   ```

2. **Run Advanced Version**
   ```bash
   python voice_assistant_advanced.py
   ```

3. **Set Up Weather (Optional)**
   - Get free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Edit `assistant_config.json`:
   ```json
   {
       "weather_api_key": "your_api_key_here",
       "default_city": "Your City"
   }
   ```

## Common Issues and Quick Fixes

### Issue: "No module named 'speech_recognition'"
**Fix:**
```bash
pip install SpeechRecognition
```

### Issue: "No module named 'pyttsx3'"
**Fix:**
```bash
pip install pyttsx3
```

### Issue: "PyAudio installation failed"
**Fix for Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

### Issue: "Microphone not working"
**Fixes:**
1. Check if microphone is plugged in
2. Check system microphone permissions
3. Try running as administrator (Windows)
4. Test microphone in system settings

### Issue: "Can't understand voice"
**Fixes:**
1. Speak clearly and at moderate speed
2. Reduce background noise
3. Move microphone closer
4. Check internet connection (needed for Google Speech Recognition)

## Testing Checklist

Before recording your demo video:

- [ ] Basic version runs without errors
- [ ] Can tell time and date
- [ ] Web search works
- [ ] Can open websites
- [ ] Jokes work
- [ ] Exit command works
- [ ] (Advanced) Weather works
- [ ] (Advanced) Wikipedia search works
- [ ] (Advanced) Calculator works

## For Your Video Demonstration

### What to Show (5-7 minutes):

1. **Introduction (30 sec)**
   - "Hello, this is my voice assistant project for Oasis Infobyte"
   - Briefly explain what it does

2. **Code Overview (1 min)**
   - Show the main files
   - Explain the basic structure
   - Highlight key functions

3. **Live Demo (3-4 min)**
   - Run the assistant
   - Demonstrate 5-7 commands
   - Show both successful commands and error handling

4. **Advanced Features (1 min)** *(if implemented)*
   - Show weather, Wikipedia, or other features
   - Show the config file

5. **Conclusion (30 sec)**
   - Mention what you learned
   - Possible future improvements

### Video Tips:
- Use screen recording software (OBS Studio is free)
- Record audio clearly
- Show terminal and code side-by-side if possible
- Edit out long pauses or errors
- Add captions for commands you speak

## GitHub Submission

### Quick Git Commands:

```bash
# Initialize repository
git init

# Add all files
git add .

# Commit
git commit -m "Voice Assistant - Oasis Infobyte Project 1"

# Add remote (create repo on GitHub first)
git remote add origin https://github.com/yourusername/voice-assistant.git

# Push
git push -u origin main
```

### Repository Structure:
```
voice-assistant/
├── README.md
├── voice_assistant.py
├── voice_assistant_advanced.py
├── requirements.txt
├── test_installation.py
└── demo/ (folder with screenshots/video)
```

## LinkedIn Post Template

```
🎤 Excited to share my Voice Assistant project! 🤖

Just completed Project 1 of my Python Programming Internship with Oasis Infobyte!

✨ Features:
• Voice command recognition
• Real-time web search
• Time & date functionality
• Weather updates
• Wikipedia integration
• And more!

🔧 Built with: Python, SpeechRecognition, pyttsx3

💡 Key learnings: API integration, error handling, natural language processing

🔗 GitHub: [your-repo-link]
📹 Demo: [your-video-link]

#oasisinfobyte #oasisinfotyte #python #machinelearning #internship #voiceassistant #pythonprogramming #coding
```

## Next Steps

After completing this project:

1. **Get Feedback**
   - Share with mentors/peers
   - Note areas for improvement

2. **Document Learning**
   - What was challenging?
   - What did you learn?
   - How would you improve it?

3. **Move to Project 2**
   - Apply lessons learned
   - Build on this foundation

## Need Help?

- Check the main README.md for detailed documentation
- Run `python test_installation.py` to diagnose issues
- Google the specific error message
- Check Python documentation
- Ask in your internship community

---

**Remember:** The goal is learning, not perfection! It's okay if something doesn't work perfectly the first time.

Good luck with your project! 🚀
