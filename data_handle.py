import db
import id_handle as idh
import qr_handle as qrh
import printer_handle as ph
import image_handle as ih

from typing import Union, Any
from log_handle import Logger

Log = Logger("data_handle")

def get_product_info(barcode: str) -> Union[dict[str, Any], None]:
    """Gibt die Informationen zu einem Produkt zurück
    
    Args:
        barcode (str): Der Barcode des Produkts
        
    Returns:
        dict[str, Any]: Die Informationen zum Produkt
    """
    
    try:
        product = db.get("ean", barcode)
        return product
    except KeyError:
        print("Product not found")
    
def save_product(product: dict) -> None:
    barcode = product["ean"]
    db.set("ean", barcode, product)
    Log.log(f"saved product '{product['name']}' with barcode '{barcode}'")

def config():
    data = db.getAll("config")
    Log.log(f"got config data")
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
        
        
        
def add_shopping_list_item_barcode(barcode: str, amount: int):
    #Produkt aus Datenbank holen
    product = get_product_info(barcode)
    shopping_list_uid = db.get("zentralspeicher", "shopping_list_uid")
    
    db.set("shopping_list")
    
        
        
    