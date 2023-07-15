import qrcode as qr

def generateInternalIdQRCode(ids: list):
    for id in ids:
        qrCode = qr.QRCode(box_size=2, border=0)
        qrCode.add_data(id)
        img = qrCode.make_image(fit=True)
        img.save('internal_qr_codes/' + id + '.png')
