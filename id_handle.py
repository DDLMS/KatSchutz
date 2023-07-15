import db

def getNext() -> str:
    """Gibt die nächste freie ID zurück"""
    #Daten aus Zentralspeicher lesen
    data = db.read("zentralspeicher")
    
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
    
    #Neue ID in Zentralspeicher schreiben
    db.write("zentralspeicher", data)
    
    #ID zurückgeben
    return id