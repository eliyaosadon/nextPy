from gtts import gTTS
import os


def main():
    text = "first time i'm using a package in next.py course"
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save("welcome.mp3")
    os.system("start welcome.mp3")


if __name__ == '__main__':
    main()