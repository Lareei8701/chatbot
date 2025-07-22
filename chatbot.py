import cohere
from RealtimeSTT import AudioToTextRecorder
import pyttsx3
import multiprocessing
import signal
import sys

class ChatBot:
    def __init__(self):
        self.running = True
        self.recorder = None
        self.tts = None
        
    def signal_handler(self, sig, frame):
        print("\n🛑 Stopping chatbot...")
        self.running = False
        if self.recorder:
            self.recorder.stop()
        sys.exit(0)
        
    def main(self):
        # Set up signal handler for Ctrl+C
        signal.signal(signal.SIGINT, self.signal_handler)
        
        try:
            print("Initializing...")
            
            # Initialize Cohere
            co = cohere.Client("add_your_cohere_api_key_here")
            print("✅ Cohere ready")
            
            # Initialize Speech-to-Text
            self.recorder = AudioToTextRecorder(model="base", language="en")
            print("✅ Speech-to-Text ready")
            
            # Initialize Text-to-Speech
            self.tts = pyttsx3.init()
            self.tts.setProperty('rate', 150)
            print("✅ Text-to-Speech ready")
            
            print("🎤 Chatbot started! Speak to begin...")
            print("💡 Say 'stop chatbot' or 'quit' to exit, or press Ctrl+C")
            
            while self.running:
                try:
                    # Step 1: Convert audio to text
                    print("Listening...")
                    self.recorder.start()
                    text = self.recorder.text()
                    self.recorder.stop()
                    
                    if not text:
                        continue
                        
                    print("You said:", text)
                    
                    # Check for stop commands
                    if any(word in text.lower() for word in ['stop chatbot', 'quit', 'exit', 'goodbye']):
                        print("👋 Goodbye!")
                        break
                    
                    # Step 2: Generate response using Cohere
                    response = co.chat(
                        message=text,
                        model="command-r7b-arabic-02-2025",
                        preamble="You are a helpful AI assistant. Always answer with less than 15 words"
                    )
                    
                    answer = response.text
                    print("Bot:", answer)
                    
                    # Step 3: Convert response to audio
                    self.tts.say(answer)
                    self.tts.runAndWait()
                    
                except KeyboardInterrupt:
                    print("\n🛑 Interrupted by user")
                    break
                except Exception as e:
                    print(f"Error: {e}")
                    
        except Exception as e:
            print(f"Setup Error: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        print("🧹 Cleaning up...")
        if self.recorder:
            self.recorder.stop()
        if self.tts:
            self.tts.stop()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    bot = ChatBot()
    bot.main()