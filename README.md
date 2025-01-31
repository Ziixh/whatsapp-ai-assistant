# WhatsApp AI Assistant

This is an AI assistant that listens to your voice commands and sends messages via WhatsApp Desktop.

## Features
- Converts voice commands into text using Vosk.
- Automates interactions with WhatsApp Desktop using PyAutoGUI.
- Supports confirmation before sending messages.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Ziixh/whatsapp-ai-assistant.git
   cd whatsapp-ai-assistant

2. Install the required dependencies:
   pip install -r requirements.txt

3. Download the Vosk model:
   Download the small English model from Vosk Models(https://alphacephei.com/vosk/models?spm=5aebb161.65358e84.0.0.7cf451714kEH30).
   Extract it into the project folder and update the model_path variable in whatsapp_ai_assistant.py.

## Usage

Run the script:
   python whatsapp_ai_assistant.py

Follow the voice prompts to send a message:
   Speak the message you want to send (e.g., "I am tired today").
   When prompted, speak the recipient's name (e.g., "Ali").
   Confirm the recipient and message when asked.

## Notes
   Ensure WhatsApp Desktop is installed and logged in on your system.
   The script assumes WhatsApp is already open when running.
   If the script doesn't work as expected, ensure your microphone and audio settings are configured correctly.

## Known Issues
   The script may require adjustments for different screen resolutions.
   Timing delays may vary depending on your system's performance. Adjust time.sleep() values in the script if needed.
   Ensure the contact name matches exactly as it appears in your WhatsApp contacts.

## License
This project is licensed under the MIT License.

## Contact
If you have any questions or suggestions, feel free to reach out:
   GitHub: @Ziixh