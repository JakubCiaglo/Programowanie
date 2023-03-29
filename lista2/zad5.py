from PIL import Image, ImageDraw, ImageFont

def dodaj_znak_wodny(sciezka_do_grafiki, tekst_znaku_wodnego):
    '''Funkcja dodająca do podanej grafiki zadany znak wodny
    
    Parametry:
    sciezka_do_grafiki: sciezka do grafiki, do której chcemy dodać znak wodny
    tekst_znaku_wodnego: tekst jaki chcemy dodać jako znak wodny'''
    with Image.open(sciezka_do_grafiki).convert('RGBA') as img:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 100)
        szerokosc_tekstu, wysokosc_tekstu = draw.textsize(tekst_znaku_wodnego, font)
        draw.text((0.5*img.width-szerokosc_tekstu, 0.5*img.height - wysokosc_tekstu), tekst_znaku_wodnego, font=font, fill=(255, 255, 255, 20))
        img.save("znak_wodny_" + sciezka_do_grafiki)
        print("Dodano znak wodny do grafiki:", sciezka_do_grafiki)

sciezka='c:\\users\\lab\\desktop'
tekst='Znak-Wodny'
dodaj_znak_wodny(sciezka,tekst)
