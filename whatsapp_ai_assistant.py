import os
import time
import json
from vosk import Model, KaldiRecognizer
import pyaudio
import pyautogui
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def ask_yes_no(prompt):
    """Ask a yes/no question and return the user's response."""
    print(prompt)
    speak(prompt)
    print("Listening... Speak now!")
    while True:
        try:
            data = stream.read(2048, exception_on_overflow=False)  # Smaller chunk size
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()
                recognized_text = json.loads(result)["text"].strip().lower()
                print(f"Debug: Raw recognized text: {recognized_text}")  # Debugging

                # Check for "yes" or "no" in the recognized text
                if "yes" in recognized_text:
                    return True
                elif "no" in recognized_text:
                    return False
                else:
                    print("Please say 'yes' or 'no'.")
                    speak("Please say 'yes' or 'no'.")
        except OSError as e:
            print(f"Audio buffer overflow: {e}. Continuing...")
            continue
        except KeyboardInterrupt:
            print("\nExiting...")
            speak("Exiting.")
            exit()

# Step 1: Set up Vosk for Speech-to-Text
model_path = "C:/vosk-model-small-en-in-0.4"  # Update this path to a larger model
model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

# Step 2: Set up PyAudio to capture your voice
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)  # Larger buffer size
stream.start_stream()

# Slow down PyAutoGUI actions and enable failsafe
pyautogui.PAUSE = 1  # Add a 1-second pause between actions
pyautogui.FAILSAFE = True  # Move the mouse to the top-left corner to stop the script

print("AI Assistant is ready!")
speak("AI Assistant is ready!")

while True:
    # Step 3: Ask for the message
    print("What message would you like to send?")
    speak("What message would you like to send?")
    print("Listening... Speak now!")
    message = ""
    while True:
        try:
            data = stream.read(2048, exception_on_overflow=False)  # Smaller chunk size
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()
                recognized_text = json.loads(result)["text"].strip()  # Get the recognized text
                print(f"Debug: Raw recognized text: {recognized_text}")  # Debugging
                if recognized_text.lower() in ["that's all", "go ahead", "done"]:
                    print(f"Message received: {message}")
                    break
                else:
                    message += " " + recognized_text  # Append to the message
        except OSError as e:
            print(f"Audio buffer overflow: {e}. Continuing...")
            continue

    # Step 4: Ask for the contact name
    print("Who would you like to send the message to?")
    speak("Who would you like to send the message to?")
    print("Listening... Speak now!")
    contact_name = ""
    while True:
        try:
            data = stream.read(2048, exception_on_overflow=False)  # Smaller chunk size
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()
                recognized_text = json.loads(result)["text"].strip()  # Get the recognized text
                print(f"Debug: Raw recognized text: {recognized_text}")  # Debugging
                if recognized_text.lower() in ["that's all", "go ahead", "done"]:
                    print(f"Contact name received: {contact_name}")
                    break
                else:
                    contact_name += " " + recognized_text  # Append to the contact name
        except OSError as e:
            print(f"Audio buffer overflow: {e}. Continuing...")
            continue

    # Step 5: Verify the contact name
    if not ask_yes_no(f"You want to send a message to {contact_name}. Is that correct? Say 'yes' or 'no'."):
        print("Please say the contact name again.")
        speak("Please say the contact name again.")
        continue  # Restart the contact name step

    # Step 6: Automate WhatsApp to send the message
    try:
        print(f"Sending message '{message}' to {contact_name}...")
        speak(f"Sending message to {contact_name}.")
        
        # Open WhatsApp (if not already open)
        print("Opening WhatsApp...")
        speak("Opening WhatsApp.")
        pyautogui.hotkey('win', 's')  # Open Windows search
        time.sleep(1)
        pyautogui.write('WhatsApp')  # Search for WhatsApp
        time.sleep(1)
        pyautogui.press('enter')  # Open WhatsApp
        time.sleep(5)  # Wait for WhatsApp to load
        print("WhatsApp opened.")

        # Search for the recipient
        print(f"Searching for recipient: {contact_name}")
        speak(f"Searching for {contact_name}.")
        pyautogui.hotkey('ctrl', 'f')  # Open search bar in WhatsApp
        time.sleep(2)
        pyautogui.write(contact_name.strip())  # Type recipient's name (remove extra spaces)
        time.sleep(3)  # Wait for search results to load

        # Select the contact from the search results
        print("Selecting the contact...")
        speak("Selecting the contact.")
        pyautogui.keyDown('down')  # Press the down arrow key
        time.sleep(0.1)  # Short delay to ensure the key is registered
        pyautogui.keyUp('down')  # Release the down arrow key
        time.sleep(1)
        pyautogui.press('enter')  # Select the contact
        time.sleep(3)  # Wait for the chat to open
        print(f"Recipient selected: {contact_name}")

        # Verify that the chat has opened
        print("Checking if the chat has opened...")
        time.sleep(2)  # Additional delay to ensure the chat is ready
        pyautogui.write(message.strip())  # Type the message (remove extra spaces)
        time.sleep(1)
        pyautogui.press('enter')  # Send the message
        print("Message sent.")
        speak("Message sent.")

    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, an error occurred while sending the message.")

    # Step 7: Ask if the user wants to send another message
    if not ask_yes_no("Would you like to send another message? Say 'yes' or 'no'."):
        print("Goodbye!")
        speak("Goodbye!")
        break  # Exit the script

# Clean up
stream.stop_stream()
stream.close()
p.terminate()