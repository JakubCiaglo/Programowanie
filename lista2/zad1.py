import random
import string
znaki = string.ascii_letters + string.digits + string.punctuation
def haslo(liczba_znaków):
    '''Funkcja generuje losowe hasło

    Parametry:
    liczba_znaków: liczba, która mówi ile znaków ma mieć wygenerowane hasło'''
    
    haslo=''.join(random.choice(znaki) for i in range(liczba_znaków))
    print("Wygenerowane hasło: ", haslo)
haslo(8)