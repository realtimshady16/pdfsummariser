#pdftotext
import PyPDF2, sys, os

# pdf_path = "C:\\Users\\tevertse\\IdeaProjects\\Automation\\AI\\on-being-lucky.pdf"
pdf_path = sys.argv[1]
print("PDF: ", pdf_path)
print("Current Working Directory: ", os.getcwd())
print("Files in current Directory: ", os.listdir())
print("File exists: ", os.path.exists(pdf_path))
pdf_file = open(pdf_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ''
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text += page.extract_text()

with open("maths_learning.txt", "w", encoding="utf-8") as txtFile:
    txtFile.write(text)
