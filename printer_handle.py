import subprocess
def print_qr(id: list):
    for code in id:
        subprocess.run(f'"C:\\Program Files\\IrfanView\\i_view64.exe" "C:\\Users\\bjarne\\KatSchutz\\internal_qr_codes\\{code}.png" /print')