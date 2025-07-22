# Voice Chatbot with Enhanced Controls

A Python-based voice chatbot that listens to your speech, responds using Cohere AI, and speaks back to you using text-to-speech.

## Features

- **Voice Input**: Speaks to the bot using your microphone
- **AI Responses**: Powered by Cohere's command-r7b-arabic-02-2025 model
- **Voice Output**: Bot speaks responses back to you
- **Multiple Stop Methods**: Easy ways to exit the program
- **Error Recovery**: Handles TTS failures gracefully

## Requirements

```bash
pip install cohere RealtimeSTT pyttsx3
```

## Setup

1. **Install dependencies**:
   ```bash
   pip install cohere RealtimeSTT pyttsx3
   ```

2. **Get Cohere API Key**:
   - Sign up at [cohere.ai](https://cohere.ai)
   - Replace the API key in the code with your own

3. **Run the chatbot**:
   ```bash
   python chatbot.py
   ```

## How to Use

### Starting the Bot
1. Run the script
2. Wait for "🎤 Chatbot started! Speak to begin..."
3. Start speaking when you see "Listening..."

### Stopping the Bot

You have multiple ways to stop the chatbot:

#### Method 1: Voice Commands
Simply say any of these phrases:
- "stop chatbot"
- "quit"
- "exit"
- "goodbye"

#### Method 2: Keyboard Interrupt
- Press **Ctrl+C** (Windows/Linux)
- Press **Cmd+C** (Mac)


## How It Works

1. **Audio Input**: Uses RealtimeSTT to convert your speech to text
2. **AI Processing**: Sends text to Cohere AI for intelligent responses
3. **Audio Output**: Uses pyttsx3 to convert AI response back to speech
4. **Loop**: Continues listening for new input


### Response Length
The bot is configured to give short responses (under 15 words). To change this:
```python
preamble="You are a helpful AI assistant. Always answer with less than 15 words"
```

### Language Model
Currently uses `command-r7b-arabic-02-2025`. You can change to:
- `command-r-plus`
- `command-r`
- `command`

## Troubleshooting

### Bot stops talking after first response
- The enhanced version includes TTS error recovery
- If issues persist, try restarting the program


## Code Structure
```
chatbot.py
├── ChatBot class
│   ├── __init__() - Initialize components
│   ├── signal_handler() - Handle Ctrl+C gracefully  
│   ├── main() - Main conversation loop
│   └── cleanup() - Clean up resources
└── Entry point with multiprocessing support
```

## Security Note
Remember to:
- Keep your API key secure
- Don't commit API keys to version control
- Consider using environment variables for API keys
