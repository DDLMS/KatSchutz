def analyze_barcode(barcode: str):
    if barcode.isdigit():
        if len(barcode) == 13:
            return "EAN13"
        elif len(barcode) == 8:
            return "EAN8"
        elif len(barcode) == 12:
            return "UPCA"
    else:
        if barcode.startswith("DD") and len(barcode) == 12:
            return "DDItem"
        else:
            return "Unbekannt"
    
def is_official(barcode: str):
    if analyze_barcode(barcode) is "EAN13" or analyze_barcode(barcode) is "EAN8" or analyze_barcode(barcode) is "UPCA":
        return True
    else:
        return False