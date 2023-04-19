import os
import datetime
import shutil

def backup_files(paths, extensions):
    '''
    Funkcja tworząca backup plików zmodyfikowanych w ostatnich 3 dniach
    
    Parametry:
    paths: lista zawierająca ścieżki do katalogów których pliki mają być zapisane
    extensions: lista rozszerzenia plików, które chcemy zapisać
    '''
    backup_dir = os.path.join(os.getcwd(), 'Backup', f'copy-{datetime.date.today()}')
    os.makedirs(backup_dir, exist_ok=True)
    three_days_ago = datetime.datetime.now() - datetime.timedelta(days=3)

    for extension in extensions:
        for path in paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(f'.{extension}'):
                        file_path = os.path.join(root, file)
                        mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                        if mod_time > three_days_ago:
                            backup_path = os.path.join(backup_dir, file)
                            if not os.path.exists(backup_path):
                                shutil.copy(file_path, backup_path)
    print('Stworzono backup na ścieżce ',backup_dir)
    
backup_files(["C:\\Users\\lab\\Desktop\\testowy1","C:\\Users\\lab\\Desktop\\testowy2"], ['txt','docx'])