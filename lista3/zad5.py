def sprawdz_nawiasy(wyrazenie):
    
    '''Funkcja sprawdzająca poprawność implementacji nawiasów w podanym wyrażeniu
    
    Parametry:
    wyrazenie: wyrażenie, którego nawiasy chcemy sprawdzić
    '''
    stos = []
    for znak in wyrazenie:
        if znak in ['(', '[', '{','<']:
            stos.append(znak)
        elif znak in [')', ']', '}','>']:
            if len(stos) == 0:
                return "Niepoprawne nawiasy"
            poprzedni = stos.pop()
            if (znak == ')' and poprzedni != '(') or (znak == ']' and poprzedni != '[') or (znak == '}' and poprzedni != '{') or (znak == '>' and poprzedni != '<'):
                return "Niepoprawne nawiasy"
    if len(stos)== 0:
        return "Poprawne nawiasy"
    else:
        return "Niepoprawne nawiasy"


        

# przykład użycia:
dzialanie1 = "<2 * (3 + 4) - [5 / (6 - 2)]>"
wynik = sprawdz_nawiasy(dzialanie1)
print(wynik)  

dzialanie2 = "<2 * (3 + 4 - [5 / (6 - 2)]>"
wynik = sprawdz_nawiasy(dzialanie2)
print(wynik)  

