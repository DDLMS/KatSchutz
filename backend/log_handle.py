#Farben für die Ausgabe
red = "\033[31m"
gray = "\033[90m"
purple = "\033[35m"
yellow = "\033[33m"

LOG_PATH = "logs/"

class Logger:
    def __init__(self, module_name: str):
        self.module = module_name
        
    def log(self, message: str, level: int = 4) -> None:
        """Gibt eine Log-Nachricht aus und speichert sie in der Log-Datei"""
        
        print_log, save_log  = self.generate_log(message, level)
        print(print_log)
        
        with open(f"{LOG_PATH}{self.module}.log", "a") as f:
            f.write(save_log + "\n")
        
    def generate_log(self, message: str, level: int) -> tuple:
        """
        Erzeugt einen Log-Eintrag
        
        Log-Level:
        1. Fehler: Rot
        2. Warnung: Gelb
        3. Info: Lila
        4. Debug: Grau
        """
        
        
        #Nachrichtenfarbe auf Basis des Log-Levels erstellen
        print_prefix = ""
        save_prefix = ""
        log_message = ""
        save_message = f"[{self.module}] {message}"
        
        if level == 1:
            print_prefix = red
            save_prefix = "[ERROR] "
        elif level == 2:
            print_prefix = yellow
            save_prefix = "[WARNING] "
        elif level == 3:
            print_prefix = purple
            save_prefix = "[INFO] "
        elif level == 4:
            print_prefix = gray
            save_prefix = "[DEBUG] "
            
        #Ausgabenachricht für die Konsole erstellen
        log_message = f"{print_prefix}{save_message}"
        save_message = f"{save_prefix}{save_message}"
        
        #Die Nachrichten zurückgeben
        return log_message, save_message
     
if __name__ == "__main__":
    testlogger = Logger("test")
    testlogger.log("Testnachricht Level 1", 1)
    testlogger.log("Testnachricht Level 2", 2)
    testlogger.log("Testnachricht Level 3", 3)
    testlogger.log("Testnachricht Level 4", 4)
    testlogger.log("Testnachricht ohne Level")