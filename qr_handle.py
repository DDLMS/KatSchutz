import qrcode as qr

def generateInternalIdQRCode(internalId):
    qrCode = qr.QRCode(box_size=20, border=0)
    qrCode.add_data(internalId)
    img = qrCode.make_image(fit=True)
    img.save('qr_code.png')
