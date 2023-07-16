import tkinter as tk
from tkinter import ttk

from tkinter import messagebox
import data_handle as dh


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        # self.geometry("600x400")
        self.resizable(0, 0)

        self.create_barcode_entry_frame()
        self.create_product_info_frame()

    def create_barcode_entry_frame(self):
        self.barcodeEntryFrame = ttk.Frame(self)
        self.barcodeEntryFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.barcodeEntryLabel = ttk.Label(
            self.barcodeEntryFrame, text="Barcode:")
        self.barcodeEntryLabel.grid(row=0, column=0)

        self.barcodeEntry = ttk.Entry(self.barcodeEntryFrame)
        self.barcodeEntry.grid(row=0, column=1)

        # Enter Taste binden
        self.barcodeEntry.bind("<Return>", self.barcode_entry_scanned)

        # Fokus auf Eingabefeld setzen
        self.barcodeEntry.focus()

    def create_product_info_frame(self):
        self.productInfoFrame = ttk.Frame(self)
        self.productInfoFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.productEanLabel = ttk.Label(self.productInfoFrame, text="EAN:")
        self.productEanLabel.grid(row=0, column=0)

        self.productEan = ttk.Entry(self.productInfoFrame, width=30)
        self.productEan.grid(row=0, column=1)

        self.productNameLabel = ttk.Label(self.productInfoFrame, text="Name:")
        self.productNameLabel.grid(row=1, column=0)

        self.productName = ttk.Entry(self.productInfoFrame, width=30)
        self.productName.grid(row=1, column=1)

        self.productManufacturerLabel = ttk.Label(
            self.productInfoFrame, text="Hersteller:")
        self.productManufacturerLabel.grid(row=2, column=0)

        self.productManufacturer = ttk.Entry(self.productInfoFrame, width=30)
        self.productManufacturer.grid(row=2, column=1)

        self.productCategoryLabel = ttk.Label(
            self.productInfoFrame, text="Kategorie:")
        self.productCategoryLabel.grid(row=3, column=0)

        # Kategoriemenü
        self.productCategory = ""
        categories = dh.config()["category"]

        self.productCategoryMenuButtonText = tk.StringVar()
        self.productCategoryMenuButtonText.set("Kategorie auswählen")
        self.productCategoryMenuButton = ttk.Menubutton(
            self.productInfoFrame, textvariable=self.productCategoryMenuButtonText)
        self.productCategoryMenuButton.grid(row=3, column=1)

        self.productCategoryMenu = tk.Menu(
            self.productCategoryMenuButton, tearoff=False)
        self.productCategoryMenuButton.config(menu=self.productCategoryMenu)

        for category, subcategories in categories.items():
            submenu = tk.Menu(self.productCategoryMenu, tearoff=False)
            self.productCategoryMenu.add_cascade(label=category, menu=submenu)
            for subcategory in subcategories:
                submenu.add_command(label=subcategory, command=lambda cat=category,
                                    sub=subcategory: self.product_category_changed(cat, sub))

        # Textboxen wie den Save-Button binden
        self.productEan.bind("<Return>", lambda event: self.save_product())
        self.productName.bind("<Return>", lambda event: self.save_product())
        self.productManufacturer.bind(
            "<Return>", lambda event: self.save_product())

        # Textboxen sperren
        self.productEan.config(state="readonly")
        self.productName.config(state="readonly")
        self.productManufacturer.config(state="readonly")

    def product_category_changed(self, category, subcategory):
        print("Kategorie: " + category + " - " + subcategory)
        self.productCategory = category + " - " + subcategory
        self.productCategoryMenuButtonText.set(self.productCategory)

    def barcode_entry_scanned(self, event):
        barcode = self.barcodeEntry.get()
        print("Barcode: " + barcode)
        self.delete_product_info()
        self.barcodeEntry.delete(0, tk.END)

        product = None
        product = dh.get_product_info(barcode)

        # Wenn Barcode ein EAN-13 Code ist
        if len(barcode) == 13:
            # Wenn Produkt bereits in der Datenbank vorhanden ist
            if product is not None:
                self.unlock_product_info()

                self.productEan.insert(0, product["ean"])
                self.productName.insert(0, product["name"])
                self.productManufacturer.insert(0, product["manufacturer"])
                self.productCategory = product["category"]
                self.productCategoryMenuButtonText.set(self.productCategory)

            # Wenn Produkt nicht in der Datenbank vorhanden ist
            else:
                self.unlock_product_info()
                self.productEan.insert(0, barcode)
                self.productCategoryMenuButtonText.set("Kategorie auswählen")
                self.productCategory = ""

                messagebox.showinfo(
                    "Produkt nicht gefunden", "Produkt nicht gefunden. Informationen können jetzt eingetragen werden.")

                self.productName.focus()

            # EAN-13 Code sperren, da er nicht mehr geändert werden darf
            self.productEan.config(state="readonly")

        # Wenn Barcode kein EAN-13 Code ist
        else:
            messagebox.showerror("Fehler", "Der Barcode ist kein EAN-13 Code!")

    def delete_product_info(self) -> None:
        self.unlock_product_info()
        self.productEan.delete(0, tk.END)
        self.productName.delete(0, tk.END)
        self.productManufacturer.delete(0, tk.END)
        self.lock_product_info()

    def lock_product_info(self):
        self.productEan.config(state="readonly")
        self.productName.config(state="readonly")
        self.productManufacturer.config(state="readonly")

    def unlock_product_info(self):
        self.productEan.config(state="normal")
        self.productName.config(state="normal")
        self.productManufacturer.config(state="normal")

    def save_product(self):
        if self.productCategory == "":
            messagebox.showerror(
                "Fehler", "Es muss eine Kategorie ausgewählt werden!")
            return

        product = {
            "ean": self.productEan.get(),
            "name": self.productName.get(),
            "manufacturer": self.productManufacturer.get(),
            "category": self.productCategory
        }

        dh.save_product(product)
        messagebox.showinfo("Produkt gespeichert",
                            "Das Produkt wurde erfolgreich gespeichert")
        self.delete_product_info()
        self.productCategory = ""
        self.productCategoryMenuButtonText.set("Kategorie auswählen")
        self.barcodeEntry.focus()


if __name__ == "__main__":
    app = App()
    app.mainloop()
