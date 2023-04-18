def zamiana(nazwa_pliku):
    '''Funkcja zamieniająca znaki przejścia do nowej lini w Unixowych na Windowsowe i odwrotnie
    
    Parametry:
    nazwa_pliku: nazwa pliku, który chcemy zmodyfikować'''
    try:
        with open(nazwa_pliku, 'r') as plik:
            zawartosc = plik.read()
        
        # Sprawdzenie typu znaków końca linii w pliku
        if '\r\n' in zawartosc:
            # Zamiana z Windowsowych na Unixowe
            zawartosc = zawartosc.replace('\r\n', '\n')
        elif '\n' in zawartosc:
            # Zamiana z Unixowych na Windowsowe
            zawartosc = zawartosc.replace('\n', '\r\n')
        else:
            print("Plik nie zawiera znaków końca linii.")
            return
        
        # Zapisanie nowej zawartości do pliku
        with open(nazwa_pliku, 'w') as plik:
            plik.write(zawartosc)
        
        print("Zamiana znaków końca linii w pliku zakończona powodzeniem.")
    
    except FileNotFoundError:
        print("Plik nie istnieje.")

zamiana('testowy1.txt')
zamiana('testowy2.txt')
zamiana('testowy3.txt')