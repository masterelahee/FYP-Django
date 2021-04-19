import qrcode
import pyotp
import time
from qrcode.image.pure import PymagingImage

def qrcodeGenerator(userEmail):
    
    #check if secret is empty in firebase do somethingm, if not, do something else
    secret = pyotp.random_base32() 
    print('Secret:', secret)
    #save to firebase

    totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(
        userEmail,
        issuer_name="fyp-scanner")

    print(totp_uri)

    qr = qrcode.make(totp_uri)
    qr.save('D:/Desktop/FYP/FYP-Django/mysite/myapp/QRcodes/otp.png') #send to email #secret saved in DB
    return secret

def validation(secret,inputOtp):
    #directly retrive from firebase the useremail
    totp = pyotp.TOTP(secret)

    result = totp.verify(inputOtp)
    print('Code Valid:',result)
    return result

def main():
    userEmail='fypemail78@yahoo.com'

    
    #secret = call from firebase

    totp = pyotp.TOTP(secret)

    your_code = input("Enter your OTP: ")#get user input from django form
    validation(secret,your_code)
    print('OTP code:',totp.now())

    time.sleep(30)
    your_code = input("Enter your OTP: ")
    validation(secret,your_code)
    print('OTP code:',totp.now())

if __name__ == '__main__':
    main() 