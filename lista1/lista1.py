import random
import math
class Vector:
    '''Klasa do stworzenia Wektora '''

    def __init__(self,size=3):
        '''Konstruktor init pozwala nam zainicjować nasz wektor

        Parametry:
        --------------------------------------------
        size: liczba mówiąca nam jaką wielkość ma mieć nasz wektor, domyślna wartość to 3
        '''
        self.size=size
        self.vector=[0]*size

    def random(self,low,high):
        '''Metoda random pozwala nam wylosować elementy naszego wektora

        Parametry:
        --------------------------------------------
        low: dolna granica dla naszej losowego elementu
        high: górna granica dla naszej losowego elementu
        '''
            
        for i in range(len(self.vector)):
            self.vector[i]=random.randint(low,high)
        
    def wczytanie(self,lista):
        '''
        Metoda wczytanie pozwala wczytać elementy wektora z listy.

        Parametry:
        --------------------------------------------
        lista: lista elementów wektora
        '''
        if len(self.vector) != len(lista):
            raise ValueError('Błąd! Lista i wektor mają rózne wielkości')
        else:
            self.vector=lista.copy()
            
    def __add__(self,other):
        '''
        Operator dodawania dwóch wektorów

        Parametry:
        --------------------------------------------
        other: drugi stworzony przez nas wektor

        Zwraca:
        --------------------------------------------
         wynik: nowy wektor będący sumą dwóch poprzednich wektorów
        '''
        if self.size != other.size:
            raise ValueError('Wektory muszą mieć tę samą wielkość!')
        else:
            wynik = Vector(self.size)
            for i in range(self.size):
                wynik.vector[i] = self.vector[i] + other.vector[i]
            return wynik
            
        
    def __sub__(self, other):
        '''
        Operator odejmowania dwóch wektorów

        Parametry:
        --------------------------------------------
        other: drugi stworzony przez nas wektor

        Zwraca:
        --------------------------------------------
        wynik: nowy wektor będący różnicą dwóch poprzednich wektorów
        '''
        if self.size != other.size:
            raise ValueError('Wektory muszą mieć tę samą wielkość!')
        wynik = Vector(self.size)
        for i in range(self.size):
            wynik.vector[i] = self.vector[i] - other.vector[i]
        return wynik

    def __mul__(self, skalar):
        '''
        Operator mnożenia wektora przez skalar

        Parametry:
        --------------------------------------------
        skalar: liczba przez którą chcemy pomnożyć nasz wektor

        Zwraca:
        --------------------------------------------
        wynik: nowy wektor będący wynikiem pomnożenia naszego wektora przez skalar
        '''
        wynik = Vector(self.size)
        for i in range(self.size):
            wynik.vector[i] = self.vector[i] * skalar
        return wynik

    def dlugosc(self):
        '''
        Metoda dlugosc pozwala na wyliczenie długości naszego wektora

        Zwraca:
        --------------------------------------------    
        długość wektora'''
        return math.sqrt(sum([i**2 for i in self.vector]))

    def suma(self):
        '''
        Metoda suma pozwala na wyliczenie sumy elementów naszego wektora

        Zwraca:
        --------------------------------------------    
        suma elementów wektora
        '''
        return sum(self.vector)

    def iloczyn(self, other):
        '''
        Metoda iloczyn pozwala na obliczenie iloczynu skalarnego dwóch wektorów

        Parametry:
        --------------------------------------------
        other: drugi, stworzony przez nas wektor

        Zwraca:
        --------------------------------------------
        iloczyn skalarny dwóch wektorów
        '''
        if self.size != other.size:
            raise ValueError("Wektory nie mogą mieć różnych wielkości!")
        return sum([self[i] * other[i] for i in range(self.size)])

    def __repr__(self):
        '''
        Metoda repr pozwala na pokazanie reprezentacji tekstowej naszego wektora
        
        Zwraca:
        reprezentację tekstową wektora
        '''
        return "Vector(" + ", ".join(str(i) for i in self.vector) + ")"

    def __getitem__(self, indeks):
        '''
        Operator [] pozwalający na dostęp do konkretnych elementów naszego wektora.

        Parametry:
        --------------------------------------------
        indeks: indeks elementu wektora

        Zwraca:
        --------------------------------------------
        Element wektora o podanym indeksie
        '''
        return self.vector[indeks]

    def __contains__(self, element):
        '''
        Operator in sprawdzający przynależność elementu do wektora.

        Parametry:
        --------------------------------------------
        element: element do sprawdzenia

        Zwraca:
        --------------------------------------------
        True, jeśli element jest elementem wektora

        False jeśli podany element nie należy do wektora
        '''
        if element in self.vector:
            return True
        else: 
            return False



if __name__ == '__main__':
    v1 = Vector()
    v1.random(-10,10)
    print('\nv1 =', v1)

    v2 = Vector()
    v2.wczytanie([1, 2, 3])
    print('\nv2 =', v2)

    v3 = v1 + v2
    print('\nv3 = v1-v2=', v3)

    v4 = v1 - v2
    print('\nv4 = v1-v2=', v4)

    v5 = v1 * 2
    print('\nv5 = v1 *2=', v5)

    dlugosc = v1.dlugosc()
    print('\ndlugosc wektora v1 to', dlugosc)

    suma = v1.suma()
    print('\nsuma elementów wektora v1 to ', suma)

    iloczyn = v1.iloczyn(v2)
    print('\niloczyn skalarny wektorów v1 i v1 to', iloczyn)

    print('\nCzy 2 należy do elementów v1?:', 2 in v1)
    print('Czy 4 należy do elementów v1?:', 4 in v1)

    print("\nv1[0] =", v1[0])
    print("v1[1] =", v1[1])
    print("v1[2] =", v1[2])