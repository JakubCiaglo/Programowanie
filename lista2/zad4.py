import PyPDF2
import os

def podziel_plik_pdf(nazwa_pliku, liczba_stron_na_plik):
    '''Funkcja dzieląca podany plik pdf
    
    Parametry:
    nazwa_pliku: nazwa pliku pdf, który chcemy podzielić
    liczba_stron_na_plik: liczba stron jaką chcemy mieć w każdym pliku'''

    with open(nazwa_pliku, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        liczba_stron = len(pdf_reader.pages)
        liczba_plikow = (liczba_stron // liczba_stron_na_plik) + 1

        for i in range(liczba_plikow):
            pdf_writer = PyPDF2.PdfWriter()
            for j in range(i * liczba_stron_na_plik, min((i + 1) * liczba_stron_na_plik, liczba_stron)):
                page = pdf_reader.pages[j]
                pdf_writer.add_page(page)
            nowa_nazwa_pliku = os.path.splitext(nazwa_pliku)[0] + "_" + str(i+1) + ".pdf"
            with open(nowa_nazwa_pliku, 'wb') as new_pdf_file:
                pdf_writer.write(new_pdf_file)
                print("Utworzono plik", nowa_nazwa_pliku)

podziel_plik_pdf("test1.pdf", 5)