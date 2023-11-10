import speech_recognition as sr
import pyttsx3
import wolframalpha

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for 30 seconds...")
        try:
            audio = r.listen(source, timeout=30)
            print("Thinking...")
            query = r.recognize_google(audio)
            return query
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."
        except sr.RequestError:
            return "I'm having trouble accessing the Google API."
        except sr.WaitTimeoutError:
            return "No speech detected within the 30 seconds."

def respond(response_text):
    print("Assistant:", response_text)
    engine = pyttsx3.init()
    engine.say(response_text)
    engine.runAndWait()

def process_query(query):
    if query.lower() == "what is your name":
        return "My name is Jarvis, an AI computations and conversational program."
    elif query.lower() == "who created this application":
        return "Suleman Pervez, an AI Scientist, created this application."
    else:
        # Use Wolfram Alpha API for other queries
        app_id = "Q9PQTA-62PRJLKAVT"
        client = wolframalpha.Client(app_id)
        try:
            res = client.query(query)
            answer = next(res.results).text
            return answer
        except Exception as e:
            return "I'm not sure. Could you ask something else?"

def assistant():
    respond("Hello! How can I help you?")
    while True:
        user_input = listen().lower()
        if "exit" in user_input:
            respond("Goodbye!")
            break
        else:
            response = process_query(user_input)
            if response != "I'm not sure. Could you ask something else?":
                respond(response)

assistant()
