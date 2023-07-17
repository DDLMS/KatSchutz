import PIL.Image as Image
import PIL.ImageDraw as ImageDraw#
import PIL.ImageFont as ImageFont


def build_label(qr_code_file, item_ean: str, item_mhd: str, item_price: str, item_buy_date: str, item_buy_place: str, item_comment: str = ""):
    master_image = Image.new(mode="RGB", size=(213,84), color="white")
    qr_code = Image.open(f"internal_qr_codes/{qr_code_file}.png")
    
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
    
    
    
    master_image.save(f"labels/{qr_code_file}.png")
    
build_label("DD999999999932", "Testprodukt", "2021-12-31", "0,99€", "2021-12-31", "Testort")
