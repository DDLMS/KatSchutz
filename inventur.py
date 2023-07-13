import qr_handle as qr

import json

def read(db):
    try:
        with open(f"{db}.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
        write(db, data)
    return data

def write(db, data):
    with open(f"{db}.json", 'w') as f:
        json.dump(data, f, indent=4)

def set(db, key, value):
    data = read(db)
    data[key] = value
    write(db, data)

def get(db, key):
    data = read(db)
    return data[key]

def delete(db, key):
    data = read(db)
    del data[key]
    write(db, data)


def getNextId() -> str:
    """Gibt die nächste freie ID zurück"""
    #Daten aus Zentralspeicher lesen
    data = read("zentralspeicher")
    
    #ID aus Zentralspeicher lesen oder wenn nicht vorhanden auf Nullwert setzen
    try:
        id = data["id"]
    except KeyError:
        id = "DD0000000000"
    
    #ID zerlgen und erhöhen (format: DD0000000000)
    id_num = int(id[2:])
    id_num += 1
    
    #ID neu formatieren
    id = f"DD{id_num:012d}"
    data["id"] = id
    
    #Daten in Zentralspeicher schreiben
    write("zentralspeicher", data)
    
    #ID zurückgeben
    return id

def main():
    id = getNextId()
    print(id)
    qr.generateInternalIdQRCode(id)
    
    

if __name__ == "__main__":
    main()
