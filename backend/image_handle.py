import PIL.Image as Image
import PIL.ImageDraw as ImageDraw#
import PIL.ImageFont as ImageFont

QR_IMAGE_PATH = "img/qr_codes/"
LABEL_IMAGE_PATH = "img/labels/"

def build_label(qr_code_file, item_ean: str, item_mhd: str, item_price: str, item_buy_date: str, item_buy_place: str, item_comment: str = ""):
    master_image = Image.new(mode="RGB", size=(213,84), color="white")
    qr_code = Image.open(f"{QR_IMAGE_PATH}{qr_code_file}.png")
    
    #QR Code auf das Label platzieren
    master_image.paste(qr_code, (0,0))
    
    #Text auf das Label platzieren
    font = ImageFont.truetype("arial", 12)
    draw = ImageDraw.Draw(master_image)
    
    draw.text((50, 0), item_ean, fill="black", font=font)
    draw.text((50, 12), item_mhd, fill="black", font=font)
    draw.text((50, 36), item_price, fill="black", font=font)
    draw.text((50, 48), item_buy_date, fill="black", font=font)
    draw.text((50, 60), item_buy_place, fill="black", font=font)
    draw.text((50, 72), item_comment, fill="black", font=font)

    master_image.save(f"{LABEL_IMAGE_PATH}{qr_code_file}.png")

def build_shopping_list(shopping_list: dict):
    for category in shopping_list.keys():
        print(category)
        for product in shopping_list[category]:
            print(product)
            
