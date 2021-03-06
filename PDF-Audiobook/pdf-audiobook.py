import PyPDF2
import pyttsx3
  
# path of the PDF file
pdf = open("D://sample-life.pdf","rb")
  
# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(pdf)
  
# the page with which you want to start
# this will read the page of 25th page.
page = pdfReader.getPage(24)
  
# extracting the text from the PDF
text = page.extractText()
  
# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
