from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio_clip = recognizer.listen(source)

            try:
                transcript = recognizer.recognize_google(audio_clip)
            except sr.UnknownValueError:
                transcript = "Could not understand the audio."
            except sr.RequestError:
                transcript = "Error connecting to Google API."

    return render_template("index.html", transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True)
