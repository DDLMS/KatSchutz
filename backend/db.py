import json
import typing
from log_handle import Logger

Log = Logger("db")
db_path = "db/"

def read(db: str) -> dict[str, typing.Any]:
    try:
        with open(f"{db_path}{db}.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
        Log.log(f"created new database '{db}'", 3)
        write(db, data)
    return data

def write(db: str, data: dict[str, typing.Any]) -> None:
    """Schreibt die Daten in die Datenbank"""
    
    with open(f"{db_path}{db}.json", 'w') as f:
        json.dump(data, f, indent=4)

def set(db: str, key: str, value: typing.Any) -> None:
    """Setzt einen Wert für den gegebenen Schlüssel in der Datenbank"""
    
    data = read(db)
    data[key] = value
    Log.log(f"set key '{key}' to value '{value}' in database '{db}'")
    write(db, data)

def get(db: str, key: str) -> typing.Any:
    """Holt den Wert für den gegebenen Schlüssel aus der Datenbank"""
    
    data = read(db)
    Log.log(f"got key '{key}' from database '{db}'")
    return data[key]

def delete(db: str, key: str) -> None:
    """Löscht den gegebenen Schlüssel aus der Datenbank"""
    
    data = read(db)
    del data[key]
    Log.log(f"deleted key '{key}' from database '{db}'")
    write(db, data)

def getAll(db: str) -> dict[str, typing.Any]:
    """Holt alle Schlüssel aus der Datenbank und gibt sie als Dictionary zurück"""
    
    data = read(db)
    Log.log(f"got all keys from database '{db}'")
    return data