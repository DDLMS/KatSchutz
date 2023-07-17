import db
import id_handle as idh
import qr_handle as qrh
import printer_handle as ph
import image_handle as ih

def get_product_info(barcode):
    try:
        product = db.get("ean", barcode)
        return product
    except KeyError:
        print("Product not found")
        return None
    
def save_product(product):
    barcode = product["ean"]
    db.set("ean", barcode, product)

def config():
    data = db.getAll("config")
    return data
    
    
def save_item(
    barcode: str,
    amount: int,
    mhd: str,
    price: float = 0.0,
    buy_date: str = "",
    buy_place: str = "",
    comment: str = "",    
    ):
    
    #Die Anzahl der Items wird geloopt und für jedes Item wird eine UID generiert
    for i in range(amount):
        uid = idh.getNext()
        item = {
            "barcode": barcode,
            "mhd": mhd,
            "price": price,
            "comment": comment,
        }
        
        # Item in die Datenbank speichern
        db.set("item", uid, item)
        
        # QR-Code für das Lager erstellen
        qrh.generateInternalIdQRCode(uid)
        
        price_label = f"{item['price']}€"
        
        ih.build_label(uid, item["barcode"], item["mhd"], price_label, buy_date, buy_place, item["comment"])
        
        ph.print_qr(uid)
        
        
        
        
    