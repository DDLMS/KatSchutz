import subprocess
from log_handle import Logger

LABEL_IMAGE_PATH = "img\\labels"
SHOPPING_IMAGE_PATH = "img\\shopping_lists"

# Initialisierung des internen Loggers
Log = Logger("printer_handle")

def print_label(uid: str):
    Log.log(f"Drucke QR-Code für Item-ID: '{uid}'", 3)
    subprocess.run(f'"C:\\Program Files\\IrfanView\\i_view64.exe" "C:\\Users\\bjarne\\KatSchutz\\{LABEL_IMAGE_PATH}\\{uid}.png" /print')
    
def print_shopping_list(shopping_list_uid: str):
    Log.log(f"Drucke Einkaufsliste mit ID: '{shopping_list_uid}'", 3)
    subprocess.run(f'"C:\\Program Files\\IrfanView\\i_view64.exe" "C:\\Users\\bjarne\\KatSchutz\\{SHOPPING_IMAGE_PATH}\\{shopping_list_uid}.png" /print')
    