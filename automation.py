import subprocess
import os

def open_chrome():
    subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

def shutdown_pc():
    os.system("shutdown /s /t 1")