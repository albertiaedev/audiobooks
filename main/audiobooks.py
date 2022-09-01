import pyttsx3
import PyPDF2

try:
    book = open("allergies-in-horses.pdf","rb")
    pdf_reader = PyPDF2.PdfFileReader(book)
    pages = pdf_reader.numPages

    print("File successfully uploaded.\n")
    print(f"This file has {pages} pages.\n")
    print("Transcripting...\n")

    for i in range(pages):
        audio = pyttsx3.init()
        to_audio = pdf_reader.getPage(0)
        text = page.extractText()
        audio.runAndWait()

    print("Done.")
except:
    print("Something went wrong.\n")
    print("Your file couldn't be transcripted to audio.")
