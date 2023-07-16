import json

db_path = "db/"

def read(db):
    try:
        with open(f"{db_path}{db}.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
        write(db, data)
    return data

def write(db, data):
    with open(f"{db_path}{db}.json", 'w') as f:
        json.dump(data, f, indent=4)

def set(db, key, value):
    data = read(db)
    data[key] = value
    print(f"[DB] wrote new data to key '{key}' in database '{db}'")
    write(db, data)

def get(db, key):
    data = read(db)
    print(f"[DB] got key '{key}' from database '{db}'")
    return data[key]

def delete(db, key):
    data = read(db)
    del data[key]
    print(f"[DB] deleted key '{key}' from database '{db}'")
    write(db, data)

def getAll(db):
    data = read(db)
    print(f"[DB] got all data from database '{db}'")
    return data