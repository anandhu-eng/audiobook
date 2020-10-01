import pyttsx3
import PyPDF2
from tkinter.filedialog import *
book=askopenfilename()
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)
speaker=pyttsx3.init()
pagestart=int(input("enter the starting page number you want to read:"))
pageend=int(input("enter the ending page number you want to read:"))
speaker.say("hello anandhu, are you ready to hear?")
for i in range(pagestart-1,pageend):
    page=pdfreader.getPage(i)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
