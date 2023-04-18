import PyPDF2
import os

def ScaleniePDF(pdf_files):
    '''Funkcja, scalająca kilka plików pdf w jeden plik
    
    Parametry:
    pdf_files: lista plików pdf, które chcemy scalić
    '''
    writer = PyPDF2.PdfWriter()
    for filename in pdf_files:
        with open(filename, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in range(len(reader.pages)):
                writer.add_page(reader.pages[page])

    with open('scalony.pdf', 'wb') as scalony:
        writer.write(scalony)
    
    if os.path.exists('scalony.pdf'):
        print("Pliki PDF zostały połączone w jeden dokument.")
    else:
        print("Nie udało się połączyć plików PDF.")

pdf_files = ['test1_1.pdf', 'test1_2.pdf', 'test1_3.pdf']
ScaleniePDF(pdf_files)