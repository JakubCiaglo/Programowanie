from PIL import Image
def wygeneruj_miniature(nazwa_wejsciowa, nazwa_wyjsciowa, rozmiar):
    '''Funkcja generująca miniature obrazu
    
    Parametry: 
    nazwa_wejsciowa: nazwa obrazu do zminimalizowania
    nazwa_wyjsciowa: nazwa miniatury
    rozmiar: krotka o formacie (szerokosc, wyokosc)'''
    with Image.open(nazwa_wejsciowa) as obraz:
        obraz.thumbnail(rozmiar)
        obraz.save(nazwa_wyjsciowa, "JPEG")
        print("Utworzono miniaturę")
wygeneruj_miniature("test.jpg" , "miniatura.jpg", (50,60))