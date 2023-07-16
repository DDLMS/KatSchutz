import db

def get_product_info(barcode):
    try:
        product = db.get("ean", barcode)
        print(product)
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
    
    