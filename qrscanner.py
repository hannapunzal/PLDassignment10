#Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read
import cv2, webbrowser, datetime


def QRCodeScanner():
    vidScan = cv2.VideoCapture(0)
    readQR = cv2.QRCodeDetector()

    while True:
        _, img = vidScan.read()

        data, bbox, _ = readQR.detectAndDecode(img)
    
        if data:
            a=data
            with open("Contact Tracing Info.txt", mode = 'w') as file:     
                file.write(f'QR Code Info: \nContact Tracing Data:\nName: Hannafaith B. Punzal\nSex: Female (F)\nAge: 19\nBirthdate: October 18, 2002\nContact Information: hannapunzal18@gmail.com\n\nVaccination Status:\nFully Vaccinated (Johnson & Johnson Janssen COVID-19 Vaccine){a} \n\nDate and Time Scanned: %s.' % 
                    (datetime.datetime.now()))      
            print(a)
            break 
    
        cv2.imshow("QR Code Scanner", img)    
        if cv2.waitKey(1) == ord("q"):
            break
  
    b=webbrowser.open(str(a))
    vidScan.release()
    cv2.destroyAllWindows()
    
QRCodeScanner()