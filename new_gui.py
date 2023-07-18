import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import tkcalendar as tkc

import data_handle as dh
import barcode_handle as bh

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Donnjer Development Life Management System")
        # self.geometry("600x400")
        self.resizable(False, False)

        self.create_mainframe()
        self.create_barcode_entry_frame()
        self.create_product_info_frame()
        self.create_management_window()
        self.prepare_scan_process()

    def create_mainframe(self):
        self.mainframe = ttk.Frame(self)
        self.mainframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.productFrame = ttk.Frame(self.mainframe)
        self.productFrame.grid(row=1, column=0, sticky="nsew")
        
        self.itemFrame = ttk.Frame(self.mainframe)
        self.itemFrame.grid(row=1, column=1, sticky="nsew")

    def create_barcode_entry_frame(self):
        self.barcodeEntryFrame = ttk.Frame(self.mainframe)
        self.barcodeEntryFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        # Auswahl der Barcode Eingabe
        self.scanProductButton = ttk.Button(self.barcodeEntryFrame, text="Produkt scannen", command=lambda: self.create_scanner_window("scan_product"))
        self.scanProductButton.grid(row=0, column=0, padx=5, pady=5)
        
        self.scanAddItemButton = ttk.Button(self.barcodeEntryFrame, text="Item hizufügen", command=lambda: self.create_scanner_window("add_item"))
        self.scanAddItemButton.grid(row=0, column=1, padx=5, pady=5)
        
        self.scanRemoveItemButton = ttk.Button(self.barcodeEntryFrame, text="Item entfernen", command=lambda: self.create_scanner_window("remove_item"))
        self.scanRemoveItemButton.grid(row=0, column=2, padx=5, pady=5)

    def create_product_info_frame(self):
        self.productInfoFrame = ttk.Frame(self.productFrame)
        self.productInfoFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.productInfoLabel = ttk.Label(self.productInfoFrame, text="Produktinformationen")
        self.productInfoLabel.grid(row=0, column=0, columnspan=2, pady=5)

        # EAN
        self.productEanLabel = ttk.Label(self.productInfoFrame, text="EAN:")
        self.productEanLabel.grid(row=1, column=0)
        self.productEan = ttk.Entry(self.productInfoFrame, width=30)
        self.productEan.grid(row=1, column=1)
        
        # Produktname
        self.productNameLabel = ttk.Label(self.productInfoFrame, text="Name:")
        self.productNameLabel.grid(row=2, column=0)
        self.productName = ttk.Entry(self.productInfoFrame, width=30)
        self.productName.grid(row=2, column=1)
        
        # Hersteller
        self.productManufacturerLabel = ttk.Label(self.productInfoFrame, text="Hersteller:")
        self.productManufacturerLabel.grid(row=3, column=0)
        self.productManufacturer = ttk.Entry(self.productInfoFrame, width=30)
        self.productManufacturer.grid(row=3, column=1)
        
        # Menge
        self.productAmountLabel = ttk.Label(self.productInfoFrame, text="Menge:")
        self.productAmountLabel.grid(row=4, column=0)
        self.productAmount = ttk.Entry(self.productInfoFrame, width=30)
        self.productAmount.grid(row=4, column=1)
        
        # Mengeneinheit
        self.productAmountUnitLabel = ttk.Label(self.productInfoFrame, text="Einheit:")
        self.productAmountUnitLabel.grid(row=5, column=0)
        self.productAmountUnit = ttk.Entry(self.productInfoFrame, width=30)
        self.productAmountUnit.grid(row=5, column=1)

        # Kategorie
        self.productCategoryLabel = ttk.Label(self.productInfoFrame, text="Kategorie:")
        self.productCategoryLabel.grid(row=6, column=0)

        self.productCategory = ""
        categories = dh.config()["category"]

        self.productCategoryMenuButtonText = tk.StringVar()
        self.productCategoryMenuButtonText.set("Kategorie auswählen")
        self.productCategoryMenuButton = ttk.Menubutton(
            self.productInfoFrame, textvariable=self.productCategoryMenuButtonText)
        self.productCategoryMenuButton.grid(row=6, column=1)

        self.productCategoryMenu = tk.Menu(
            self.productCategoryMenuButton, tearoff=False)
        self.productCategoryMenuButton.config(menu=self.productCategoryMenu)

        # Menüeinträge erstellen
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
        self.productAmount.bind("<Return>", lambda event: self.save_product())
        self.productAmountUnit.bind("<Return>", lambda event: self.save_product())

        # Textboxen sperren
        self.lock_product_info()

    def product_category_changed(self, category, subcategory):
        print(f"[GUI] selected category {category} - {subcategory}")
        self.productCategory = category + " - " + subcategory
        self.productCategoryMenuButtonText.set(self.productCategory)

    def populate_product_info(self, product):
        if type(product) is dict:
            self.productEan.insert(0, product["ean"])
            self.productName.insert(0, product["name"])
            self.productManufacturer.insert(0, product["manufacturer"])
            self.productAmount.insert(0, product["amount"])
            self.productAmountUnit.insert(0, product["amountUnit"])
            self.productCategory = product["category"]
            self.productCategoryMenuButtonText.set(self.productCategory)
        
        # Wenn das Produkt nicht im Speicher ist, kann es manuell angelegt werden
        else:
            self.productEan.insert(0, product)
            messagebox.showinfo("Produkt nicht gefunden", "Das Produkt wurde nicht gefunden. Die Produktinformationen können jetzt manuell ausgefüllt werden.")

            # EAN-Textbox sperren, da sie nicht mehr geändert werden darf
            self.productEan.config(state="readonly")

    def delete_product_info(self) -> None:
        self.unlock_product_info()
        self.productEan.delete(0, tk.END)
        self.productName.delete(0, tk.END)
        self.productManufacturer.delete(0, tk.END)
        self.productAmount.delete(0, tk.END)
        self.productAmountUnit.delete(0, tk.END)
        self.productCategory = ""
        self.productCategoryMenuButtonText.set("Kategorie auswählen")
        self.lock_product_info()

    def lock_product_info(self):
        self.productEan.config(state="readonly")
        self.productName.config(state="readonly")
        self.productManufacturer.config(state="readonly")
        self.productAmount.config(state="readonly")
        self.productAmountUnit.config(state="readonly")
        
        self.productCategoryMenuButton.config(state="disabled")

    def unlock_product_info(self):
        self.productEan.config(state="normal")
        self.productName.config(state="normal")
        self.productManufacturer.config(state="normal")
        self.productAmount.config(state="normal")
        self.productAmountUnit.config(state="normal")
        
        self.productCategoryMenuButton.config(state="normal")

    def save_product(self):
        if self.productCategory == "":
            messagebox.showerror(
                "Fehler", "Es muss eine Kategorie ausgewählt werden!")
            return

        product = {
            "ean": self.productEan.get(),
            "name": self.productName.get(),
            "manufacturer": self.productManufacturer.get(),
            "category": self.productCategory,
            "amount": self.productAmount.get(),
            "amountUnit": self.productAmountUnit.get(),
        }

        dh.save_product(product)
        messagebox.showinfo("Produkt gespeichert",
                            "Das Produkt wurde erfolgreich gespeichert")
        self.prepare_scan_process()


##################################################################

# Verwaltugsfenster

    def create_management_window(self):
        self.itemManagementFrame = ttk.Frame(self.itemFrame)
        self.itemManagementFrame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.itemManagementLabel = ttk.Label(self.itemManagementFrame, text="Item Verwaltung")
        self.itemManagementLabel.grid(row=0, column=0, columnspan=2)
        
        self.itemMhdLabel = ttk.Label(self.itemManagementFrame, text="MHD:")
        self.itemMhdLabel.grid(row=1, column=0)
        
        self.itemMhd = tkc.DateEntry(self.itemManagementFrame, width=30)
        self.itemMhd.grid(row=1, column=1)
        
        self.itemAmountLabel = ttk.Label(self.itemManagementFrame, text="Menge:")
        self.itemAmountLabel.grid(row=2, column=0)
        
        self.itemAmount = ttk.Entry(self.itemManagementFrame, width=30)
        self.itemAmount.grid(row=2, column=1)
        
        self.itemPriceLabel = ttk.Label(self.itemManagementFrame, text="Preis:")
        self.itemPriceLabel.grid(row=3, column=0)
        
        self.itemPrice = ttk.Entry(self.itemManagementFrame, width=30)
        self.itemPrice.grid(row=3, column=1)
        
        self.itemBuyDateLabel = ttk.Label(self.itemManagementFrame, text="Einkaufsdatum:")
        self.itemBuyDateLabel.grid(row=4, column=0)
        
        self.itemBuyDate = tkc.DateEntry(self.itemManagementFrame, width=30)
        self.itemBuyDate.grid(row=4, column=1)    
        
        self.itemBuyPlaceLabel = ttk.Label(self.itemManagementFrame, text="Einkaufsort:")
        self.itemBuyPlaceLabel.grid(row=5, column=0)
        
        self.itemBuyPlace = ttk.Entry(self.itemManagementFrame, width=30)
        self.itemBuyPlace.grid(row=5, column=1)
        
        self.itemCommentLabel = ttk.Label(self.itemManagementFrame, text="Kommentar:")
        self.itemCommentLabel.grid(row=6, column=0)
        
        self.itemComment = ttk.Entry(self.itemManagementFrame, width=30)
        self.itemComment.grid(row=6, column=1)  
        
    def unlock_item_info(self):
        self.itemMhd.config(state="normal")
        self.itemAmount.config(state="normal")
        self.itemPrice.config(state="normal")
        self.itemBuyDate.config(state="normal")
        self.itemBuyPlace.config(state="normal")
        self.itemComment.config(state="normal")
    
    def lock_item_info(self):
        self.itemMhd.config(state="disabled")
        self.itemAmount.config(state="readonly")
        self.itemPrice.config(state="readonly")
        self.itemBuyDate.config(state="disabled")
        self.itemBuyPlace.config(state="readonly")
        self.itemComment.config(state="readonly")
    
    def delete_item_info(self):
        self.unlock_item_info()
        self.itemMhd.delete(0, tk.END)
        self.itemAmount.delete(0, tk.END)
        self.itemPrice.delete(0, tk.END)
        self.itemBuyDate.delete(0, tk.END)
        self.itemBuyPlace.delete(0, tk.END)
        self.itemComment.delete(0, tk.END)
        self.lock_item_info()
     
##################################################################

# Scanner

    def create_scanner_window(self, reason: str):
        self.scannerWindow = tk.Toplevel(self)
        self.scannerWindow.title("Scanner")
        
        self.prepare_scan_process()
        
        self.scannerBox = ttk.Entry(self.scannerWindow, width=30)
        self.scannerBox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.scannerBox.focus()
        self.scannerBox.bind("<Return>", lambda event: self.barcode_scanned(reason))
        
    def barcode_scanned(self, reason: str):
        barcode = self.scannerBox.get()
        self.scannerWindow.destroy()
        type = bh.is_official(barcode)
        
        self.unlock_product_info()
        product = dh.get_product_info(barcode)
        if product is not None:
            self.populate_product_info(product)
        else:
            self.populate_product_info(barcode)
        
        
        if reason == "scan_product":
            pass
        
        elif reason == "add_item":
            self.lock_product_info()
            self.unlock_item_info()
            
    def prepare_scan_process(self):
        self.unlock_product_info()
        self.unlock_item_info()
        self.delete_item_info()
        self.delete_product_info()
        self.lock_item_info()
        self.lock_product_info()

if __name__ == "__main__":
    app = App()
    app.mainloop()
    