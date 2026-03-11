from voice import listen
from speak import speak
from automation import open_chrome, shutdown_pc

speak("AI assistant started")

while True:

    command = listen()

    if "open chrome" in command:
        speak("Opening Chrome")
        open_chrome()

    elif "shutdown computer" in command:
        speak("Shutting down system")
        shutdown_pc()

    elif "stop" in command:
        speak("Goodbye")
        break
    
    elif "open youtube" in command:
        speak("Opening YouTube")
        import webbrowser
        webbrowser.open("https://youtube.com")
        

#     open youtube
# play music
# create folder
# search google
# open vscode