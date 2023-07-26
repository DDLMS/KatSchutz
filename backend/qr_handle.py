"""Modul zum Erzeugen von QR-Codes."""

import qrcode as qr
from log_handle import Logger

QR_IMAGE_PATH = "img/qr_codes/"

# Initialisierung des internen Loggers
Log = Logger("qr_handle")

def generate_internal_id_qrcode(item_id: str) -> None:
    """Funktion zum Erzeugen eines QR-Codes für die ID eines Items."""
    
    qrCode = qr.QRCode(box_size=2, border=0)
    qrCode.add_data(item_id)
    img = qrCode.make_image(fit=True)
    img.save(QR_IMAGE_PATH + item_id + '.png')
    Log.log("QR-Code für Item-ID " + item_id + " wurde erzeugt.")

    
if __name__ == "__main__":
    # Testaufruf
    generate_internal_id_qrcode("4004980401907")
