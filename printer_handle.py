import subprocess
def print_qr(uid: str):
    subprocess.run(f'"C:\\Program Files\\IrfanView\\i_view64.exe" "C:\\Users\\bjarne\\KatSchutz\\labels\\{uid}.png" /print')