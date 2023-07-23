import qr_handle as qr
import backend.db as db
import id_handle as uid
import printer_handle as printer




def main():
    id = []
    id.append(uid.getNext())
    print(id)
    qr.generateInternalIdQRCode(id)
    printer.print_qr(id)
    
    

if __name__ == "__main__":
    main()
