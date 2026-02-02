"""
Installation Test Script
Run this to verify all dependencies are properly installed
"""

import sys

def test_imports():
    """Test if all required libraries can be imported"""
    print("=" * 60)
    print("Voice Assistant - Installation Test")
    print("=" * 60)
    print()
    
    results = {}
    
    # Test core dependencies
    print("Testing core dependencies...")
    print("-" * 60)
    
    try:
        import speech_recognition as sr
        print("✓ SpeechRecognition: OK")
        results['speech_recognition'] = True
    except ImportError as e:
        print("✗ SpeechRecognition: FAILED")
        print(f"  Error: {e}")
        results['speech_recognition'] = False
    
    try:
        import pyttsx3
        print("✓ pyttsx3: OK")
        results['pyttsx3'] = True
    except ImportError as e:
        print("✗ pyttsx3: FAILED")
        print(f"  Error: {e}")
        results['pyttsx3'] = False
    
    try:
        import pyaudio
        print("✓ PyAudio: OK")
        results['pyaudio'] = True
    except ImportError as e:
        print("✗ PyAudio: FAILED")
        print(f"  Error: {e}")
        print("  Note: PyAudio can be tricky to install. See README for platform-specific instructions.")
        results['pyaudio'] = False
    
    print()
    print("Testing optional dependencies (for advanced features)...")
    print("-" * 60)
    
    try:
        import requests
        print("✓ requests: OK (weather feature available)")
        results['requests'] = True
    except ImportError:
        print("○ requests: Not installed (weather feature unavailable)")
        results['requests'] = False
    
    try:
        import wikipedia
        print("✓ wikipedia: OK (Wikipedia search available)")
        results['wikipedia'] = True
    except ImportError:
        print("○ wikipedia: Not installed (Wikipedia search unavailable)")
        results['wikipedia'] = False
    
    print()
    print("=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    core_working = results['speech_recognition'] and results['pyttsx3']
    
    if core_working and results['pyaudio']:
        print("✓ All core dependencies installed correctly!")
        print("  You can run the basic voice assistant.")
    elif core_working:
        print("⚠ Core dependencies installed, but PyAudio is missing.")
        print("  The assistant may have issues with microphone input.")
    else:
        print("✗ Some core dependencies are missing.")
        print("  Please install missing packages using:")
        print("  pip install SpeechRecognition pyttsx3 PyAudio")
    
    print()
    
    if results.get('requests') and results.get('wikipedia'):
        print("✓ All optional dependencies installed!")
        print("  You can use all advanced features.")
    else:
        print("ℹ Some optional dependencies are missing.")
        print("  Install them for advanced features:")
        print("  pip install requests wikipedia")
    
    print()
    
    return core_working and results['pyaudio']

def test_microphone():
    """Test if microphone is accessible"""
    print("\n" + "=" * 60)
    print("Microphone Test")
    print("=" * 60)
    
    try:
        import speech_recognition as sr
        import pyaudio
        
        recognizer = sr.Recognizer()
        
        print("\nAttempting to access microphone...")
        with sr.Microphone() as source:
            print("✓ Microphone access successful!")
            print(f"  Using device: {source.DEVICE_INDEX if hasattr(source, 'DEVICE_INDEX') else 'Default'}")
            
            # List available microphones
            try:
                print("\nAvailable audio devices:")
                p = pyaudio.PyAudio()
                for i in range(p.get_device_count()):
                    info = p.get_device_info_by_index(i)
                    if info['maxInputChannels'] > 0:
                        print(f"  [{i}] {info['name']}")
                p.terminate()
            except:
                pass
            
        return True
        
    except ImportError:
        print("✗ Cannot test microphone - required libraries not installed")
        return False
    except Exception as e:
        print(f"✗ Microphone access failed: {e}")
        print("\nPossible solutions:")
        print("  1. Check if microphone is connected")
        print("  2. Check system microphone permissions")
        print("  3. Try a different microphone")
        return False

def test_text_to_speech():
    """Test text-to-speech functionality"""
    print("\n" + "=" * 60)
    print("Text-to-Speech Test")
    print("=" * 60)
    
    try:
        import pyttsx3
        
        print("\nInitializing text-to-speech engine...")
        engine = pyttsx3.init()
        
        print("✓ Text-to-speech engine initialized!")
        
        # Get voice properties
        voices = engine.getProperty('voices')
        print(f"  Available voices: {len(voices)}")
        
        print("\nAttempting to speak test message...")
        print("  (You should hear: 'Voice assistant test successful')")
        
        engine.say("Voice assistant test successful")
        engine.runAndWait()
        
        print("✓ Text-to-speech test complete!")
        return True
        
    except ImportError:
        print("✗ Cannot test TTS - pyttsx3 not installed")
        return False
    except Exception as e:
        print(f"✗ Text-to-speech test failed: {e}")
        return False

def main():
    """Run all tests"""
    # Test imports
    imports_ok = test_imports()
    
    if not imports_ok:
        print("\n⚠ Please install missing dependencies before proceeding.")
        sys.exit(1)
    
    # Test microphone
    mic_ok = test_microphone()
    
    # Test TTS
    tts_ok = test_text_to_speech()
    
    print("\n" + "=" * 60)
    print("Final Results")
    print("=" * 60)
    
    if imports_ok and mic_ok and tts_ok:
        print("✓ All tests passed! Your system is ready.")
        print("\nYou can now run:")
        print("  python voice_assistant.py")
        print("  OR")
        print("  python voice_assistant_advanced.py")
    else:
        print("⚠ Some tests failed. Please address the issues above.")
        if not mic_ok:
            print("\n  Microphone issues are most common.")
            print("  Make sure your microphone is connected and permissions are granted.")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
