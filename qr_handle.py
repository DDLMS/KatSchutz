import qrcode as qr

def generateInternalIdQRCode(id):
    qrCode = qr.QRCode(box_size=2, border=0)
    qrCode.add_data(id)
    img = qrCode.make_image(fit=True)
    img.save('internal_qr_codes/' + id + '.png')
