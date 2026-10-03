import qrcode

#taking bank id as a input
bankid = input("Enter your Bank ID: ")


#create URL
esewa_url = f"upi://pay?pa={bankid}&pn=Recipient%20Name&mc=1234"

#create qrcodes for each payment app

esewaqr = qrcode.make(esewa_url)

#show qr


esewaqr.show()