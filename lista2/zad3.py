import os
import zipfile
import datetime

def kopia_zapasowa(katalogi, sciezka_kopii):
    '''Funkcja, która tworzy kopie zapasową wybranych katalogów
    
    Parametry:
    katalogi: nazwy katalogów, których kopie chcemy zrobić
    sciezka_kopii: scieżka, na której ma być zapisana nasza kopia
    '''
    if not os.path.exists(sciezka_kopii):
        os.makedirs(sciezka_kopii)

    date = datetime.datetime.now()
    nazwa = f"{date.strftime('%Y-%m-%d')}_backup.zip"
    
    for katalog in katalogi:
        dir_path = os.path.abspath(katalog)
        sciezka_zip = os.path.join(sciezka_kopii, nazwa)
        with zipfile.ZipFile(sciezka_zip, 'a') as zip_file:
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, file)

    print("Kopia została stworzona na ścieżce:" , sciezka_kopii)

katalogi= ["c:\\users\\lab\\desktop\\test1", "c:\\users\\lab\\desktop\\test2"]
sciezka_kopii= "c:\\users\\lab\\desktop"
kopia_zapasowa(katalogi, sciezka_kopii)