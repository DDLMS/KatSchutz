import db

cat = {
    "Lebensmittel": ["Obst & Gemüse", "Fleisch & Geflügel", "Fisch & Meeresfrüchte", "Brot & Backwaren", "Getreide & Nudeln", "Konserven", "Tiefkühlkost", "Süßwaren & Snacks", "Milchprodukte & Eier", "Getränke", "Gewürze", "Saucen", "Sonstiges"],
    "Non-Food": ["Hygieneartikel", "Reinigungsmittel", "Haushaltswaren" "Sonstiges"]
}

db.set("config", "category", cat)