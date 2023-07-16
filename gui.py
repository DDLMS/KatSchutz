import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import data_handle as dh

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        #self.geometry("600x400")
        self.resizable(0, 0)

        self.create_barcode_entry_frame()
        self.create_product_info_frame()

    def create_barcode_entry_frame(self):
        self.barcodeEntryFrame = ttk.Frame(self)
        self.barcodeEntryFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.barcodeEntryLabel = ttk.Label(self.barcodeEntryFrame, text="Barcode:")
        self.barcodeEntryLabel.grid(row=0, column=0)

        self.barcodeEntry = ttk.Entry(self.barcodeEntryFrame)
        self.barcodeEntry.grid(row=0, column=1)

        #Enter Taste binden
        self.barcodeEntry.bind("<Return>", self.barcode_entry_scanned)

        #Fokus auf Eingabefeld setzen
        self.barcodeEntry.focus()

    def create_product_info_frame(self):
        self.productInfoFrame = ttk.Frame(self)
        self.productInfoFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.productEanLabel = ttk.Label(self.productInfoFrame, text="EAN:")
        self.productEanLabel.grid(row=0, column=0)

        self.productEan = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productEan.grid(row=0, column=1)

        self.productNameLabel = ttk.Label(self.productInfoFrame, text="Name:")
        self.productNameLabel.grid(row=1, column=0)

        self.productName = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productName.grid(row=1, column=1)

        self.productManufacturerLabel = ttk.Label(self.productInfoFrame, text="Hersteller:")
        self.productManufacturerLabel.grid(row=2, column=0)

        self.productManufacturer = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productManufacturer.grid(row=2, column=1)

        self.productWeightLabel = ttk.Label(self.productInfoFrame, text="Gewicht:")
        self.productWeightLabel.grid(row=3, column=0)

        self.productWeight = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productWeight.grid(row=3, column=1)

        self.productAmountLabel = ttk.Label(self.productInfoFrame, text="Menge:")
        self.productAmountLabel.grid(row=4, column=0)

        self.productAmount = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productAmount.grid(row=4, column=1)

        self.productAmountUnitLabel = ttk.Label(self.productInfoFrame, text="Einheit:")
        self.productAmountUnitLabel.grid(row=5, column=0)

        self.productAmountUnit = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productAmountUnit.grid(row=5, column=1)

        self.productLengthLabel = ttk.Label(self.productInfoFrame, text="Länge:")
        self.productLengthLabel.grid(row=6, column=0)

        self.productLength = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productLength.grid(row=6, column=1)

        self.productHeightLabel = ttk.Label(self.productInfoFrame, text="Höhe:")
        self.productHeightLabel.grid(row=7, column=0)

        self.productHeight = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productHeight.grid(row=7, column=1)

        self.productDepthLabel = ttk.Label(self.productInfoFrame, text="Tiefe:")
        self.productDepthLabel.grid(row=8, column=0)

        self.productDepth = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productDepth.grid(row=8, column=1)

        self.productDescriptionLabel = ttk.Label(self.productInfoFrame, text="Beschreibung:")
        self.productDescriptionLabel.grid(row=9, column=0)

        self.productDescription = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productDescription.grid(row=9, column=1)

        self.productPackagingLabel = ttk.Label(self.productInfoFrame, text="Verpackung:")
        self.productPackagingLabel.grid(row=10, column=0)

        self.productPackaging = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productPackaging.grid(row=10, column=1)

        self.productPackagingMaterialLabel = ttk.Label(self.productInfoFrame, text="Verpackungsmaterial:")
        self.productPackagingMaterialLabel.grid(row=11, column=0)

        self.productPackagingMaterial = ttk.Entry(self.productInfoFrame, width=dh.config()["entrybox_length"])
        self.productPackagingMaterial.grid(row=11, column=1)

        

        self.productSaveButton = ttk.Button(self.productInfoFrame, text="Speichern", command=self.save_product)
        self.productSaveButton.grid(row=10, column=0, columnspan=2)


    def barcode_entry_scanned(self, event):
        barcode = self.barcodeEntry.get()

        product = None

        if len(barcode) == 13:
            product = dh.get_product_info(barcode)
            self.delete_product_info()

        if product is not None:
            self.productEan.insert(0, product["ean"])
            self.productName.insert(0, product["name"])
            self.productManufacturer.insert(0, product["manufacturer"])
            self.productWeight.insert(0, product["weight"])
            self.productAmount.insert(0, product["amount"])
            self.productAmountUnit.insert(0, product["amount_unit"])
            self.productLength.insert(0, product["size"]["length"])
            self.productHeight.insert(0, product["size"]["height"])
            self.productDepth.insert(0, product["size"]["depth"])
            self.productDescription.insert(0, product["description"])
        else:
            messagebox.showinfo("Produkt nicht gefunden", "Das Produkt konnte nicht gefunden werden. Es kann jetzt angelegt werden.")
            self.productEan.insert(0, barcode)

        self.barcodeEntry.delete(0, tk.END)

    def delete_product_info(self):
        self.productEan.delete(0, tk.END)
        self.productName.delete(0, tk.END)
        self.productManufacturer.delete(0, tk.END)
        self.productWeight.delete(0, tk.END)
        self.productAmount.delete(0, tk.END)
        self.productAmountUnit.delete(0, tk.END)
        self.productLength.delete(0, tk.END)
        self.productHeight.delete(0, tk.END)
        self.productDepth.delete(0, tk.END)
        self.productDescription.delete(0, tk.END)

    def save_product(self):
        product = {
            "ean": self.productEan.get(),
            "name": self.productName.get(),
            "manufacturer": self.productManufacturer.get(),
            "weight": self.productWeight.get(),
            "amount": self.productAmount.get(),
            "amount_unit": self.productAmountUnit.get(),
            "size": {
                "length": self.productLength.get(),
                "height": self.productHeight.get(),
                "depth": self.productDepth.get()
            },
            "description": self.productDescription.get()
        }

        dh.save_product(product)

        self.delete_product_info()

        messagebox.showinfo("Erfolg", "Produkt gespeichert")

        self.barcodeEntry.focus()

if __name__ == "__main__":
    app = App()
    app.mainloop()