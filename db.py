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

def getAll(db):
    data = read(db)
    return data