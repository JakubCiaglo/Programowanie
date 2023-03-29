def generowanie_slupka(operacja):
    '''Funkcja generująca słupek z podanej operacji
    
    Parametry: 
    operacja: operacja matematyczna, którą chcemy przedstawić w forme słupka'''
    if "+" in operacja:
        liczby = operacja.split("+")
        operator = "+"
    elif "-" in operacja:
        liczby = operacja.split("-")
        operator = "-"
    elif "*" in operacja:
        liczby = operacja.split("*")
        operator = "*"
    else:
        return "Nieprawidłowe działanie"
    liczby2=[]
    for i in liczby:
        liczby2.append(int(i))

    wynik = liczby2[0]
    for i in range(1, len(liczby2)):
        if operator == "+":
            wynik += liczby2[i]
        elif operator == "-":
            wynik -= liczby2[i]
        elif operator == "*":
            wynik *= liczby2[i]


    szerokosc_slupka = (max(len(str(i)) for i in liczby2 + [wynik])+1)

    slupek= ""
    for i in range(len(liczby)-1):
        slupek += '' + str(liczby[i]).rjust(szerokosc_slupka+1) +''+ "\n"
    slupek += operator +" "*((szerokosc_slupka) - len((liczby[-1]))) + liczby[-1] + "\n"
    slupek += "-"*(szerokosc_slupka+1) + "\n"
    slupek += str(wynik).rjust(szerokosc_slupka+1)
    return slupek

dzialanie1='300+1000+5+160000'
dzialanie2='10*2'
dzialanie3='100-67'
wynik1=generowanie_slupka(dzialanie1)
wynik2=generowanie_slupka(dzialanie2)
wynik3=generowanie_slupka(dzialanie3)
print(wynik1)
print('')
print(wynik2)
print('')
print(wynik3)