import data_handle as dh

def test_item_save():
    dh.save_item("1234567890123", 10, "2021-12-31", 420.69, "2021-07-23", "Testgeschäft", "Testkommentar")
    
    
if __name__ == "__main__":
    test_item_save()