import qrcode
import cv2

# Tworzenie kodu QR
def MakeQR(data):
    '''Funkcja, która stworzy kod qr
    
    Parametry:
    data: dane, które chcemy zapisać kodem qr
    '''
    qr = qrcode.QRCode(version=1, box_size=10, border=5) 
    qr.add_data(data) 
    qr.make(fit=True) 
    img = qr.make_image(fill_color="black", back_color="white") 
    img.save("qr_code.png")
    print('Kod QR został zapisany pod nazwą "qr_code.png"')
MakeQR("https://pwr.edu.pl/")


# Odczytywanie kodu QR
def ReadQR(qrcode):
    '''Funkcja, która odczyta kod qr
    
    Parametry:
    qrcode: kod qr, który chcemy odczytać
    '''
    img = cv2.imread(qrcode) 
    detector = cv2.QRCodeDetector() 
    data, bbox, _ = detector.detectAndDecode(img) 
    if bbox is not None: 
        print("Dane znalezione w podanym kodzie QR:", data) 
    else: 
        print("Podany kod QR nie został znaleziony")
ReadQR("qr_code.png")