import webbrowser
import subprocess
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
    
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")

    elif "open github" in command:
    webbrowser.open("https://github.com")

    elif "open kaggle" in command:
    webbrowser.open("https://kaggle.com")

    elif "open chatgpt" in command:
    webbrowser.open("https://chat.openai.com")

    elif "open notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")

    elif "open calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")
    
    elif "open vscode" in command:
        speak("Opening VS Code")
        subprocess.Popen("C:\\Users\\YourName\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif "open word" in command:
        speak("Opening Microsoft Word")
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

    elif "open excel" in command:
        speak("Opening Excel")
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

    elif "open powerpoint" in command:
        speak("Opening PowerPoint")
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

    elif "open file explorer" in command:
        speak("Opening File Explorer")
        subprocess.Popen("explorer")


# play-music
# create folder
# open vscode