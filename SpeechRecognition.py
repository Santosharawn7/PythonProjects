# Importing the SpeechRecognition library and aliasing it as 'sr'
import speech_recognition as sr


# Before running this, ensure the installation of SpeechRecognition and PyAudio using pip
# The code also requires access to the system's microphone for recording audio

def speech_to_text():
    # Creating an instance of Recognizer, which will help recognize speech in the audio input
    recognizer = sr.Recognizer()

    # Using a context manager ('with' statement) to automatically manage the microphone
    # 'source' is the microphone input for capturing speech
    with sr.Microphone() as source:
        print("Say something:")  # Prompting the user to speak

        # Adjusting the recognizer to account for ambient noise in the environment
        recognizer.adjust_for_ambient_noise(source)

        # Listening to the audio from the microphone for a maximum of 5 seconds
        audio = recognizer.listen(source, timeout=5)

    try:
        # Attempting to recognize and convert the speech into text using Google's speech recognition API
        print('Recognizing...')
        text = recognizer.recognize_google(audio)
        print(f"Text: {text}")  # Displaying the recognized text

        # Opening (or creating) a file called "transcribed_text.txt" in write mode
        # Writing the transcribed text into the file and saving it
        with open("transcribed_text.txt", "w") as file:
            file.write(text)
            print("Transcribed text saved to file")

    # Handling the case where speech could not be understood (e.g., mumbling or unclear audio)
    except sr.UnknownValueError:
        print("Could not understand audio.")

    # Handling errors when there are issues connecting to the Google API (e.g., no internet connection)
    except sr.RequestError as e:
        print(f"Error connecting to Google API: {e}")


# This block runs the speech_to_text function if the script is executed directly
if __name__ == "__main__":
    speech_to_text()
