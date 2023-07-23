import backend.db as db

cat = {
    "Lebensmittel": [
        "Brot & Backwaren",
        "Fisch & Meeresfrüchte",
        "Fleisch & Geflügel",
        "Getränke",
        "Getreide & Nudeln",
        "Gewürze",
        "Konserven",
        "Milchprodukte & Eier",
        "Obst & Gemüse",
        "Saucen",
        "Süßwaren & Snacks",
        "Tiefkühlkost",
        "Sonstiges"
        ],
    
    "Non-Food": [
        "Bürobedarf",
        "Haushaltswaren",
        "Hygieneartikel",
        "Reinigungsmittel",
        "Sonstiges"
        ],
    
    "Krisenvorsorge": [
        "Feuer & nichtelektrische Lichtquellen",
        "Kochen & Wärme",
        "Kleidung",
        "Medizinprodukte",
        "Moral",
        "Navigation, Kommunikation & Dokumente",
        "Nahrungsmittel",
        "Persönliche Schutzausrüstung",
        "Reparaturmaterial & Werkzeuge",
        "Strom, Energie & Beleuchtung",
        "Unterschlupf",
        "Verteidigung",
        "Wasser & Wasseraufbereitung",
        "Hygiene",
        "Sonstiges"
        ]
}

db.set("config", "category", cat)