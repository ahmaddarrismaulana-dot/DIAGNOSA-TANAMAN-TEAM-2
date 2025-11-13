import os
import csv
from rich.console import Console
from rich.panel import Panel
from rich.traceback import install

# Aktifkan rich traceback
install()

console = Console()

# ------------------------------
# Fungsi utilitas
# ------------------------------
def bersihkan():
    os.system("cls" if os.name == "nt" else "clear")

def enter(a=""):
    input(f"{a}tekan [ENTER] untuk melanjutkan >> ")

# ------------------------------
# Fungsi untuk menampung data user dari CSV
# ------------------------------
def penampung_user():
    user = []
    nomer_hp = []
    gmail_list = []
    alamat = []
    list_username = []
    list_password = []

    try:
        with open("dataadmin/datauser.csv", mode="r", newline="") as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)  # skip header
            for i in csv_reader:
                user.append(i[0])
                nomer_hp.append(i[1])
                gmail_list.append(i[2])
                alamat.append(i[3])
                list_username.append(i[4])
                list_password.append(i[5])
    except FileNotFoundError:
        # Kalau file CSV belum ada, buat header kosong
        with open("dataadmin/datauser.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["nama lengkap", "nomor hp", "gmail", "alamat", "username", "password"])
    return user, nomer_hp, gmail_list, alamat, list_username, list_password

# ------------------------------
# Fungsi registrasi
# ------------------------------
def registrasi():
    bersihkan()
    user, nomer_hp_list, gmail_list, alamat_list, list_username, list_password = penampung_user()

    # ---- Nama ----
    while True:
        try:
            nama = input("Masukan nama anda: ")
            if len(nama) < 4:
                raise ValueError("Masukan nama minimal 4 karakter.")
            break
        except ValueError as e:
            console.print(Panel(f"[red bold]Terjadi kesalahan![/red bold]\n{e}", title="🚨 ERROR", border_style="red"))
            enter()

    # ---- Nomor HP ----
    while True:
        try:
            nomerhp = input("Masukan Nomor Handphone (contoh: 08934427689): ")
            if not nomerhp.isdigit():
                raise ValueError("Nomor HP hanya boleh angka.")
            if len(nomerhp) < 10 or len(nomerhp) > 12:
                raise ValueError("Nomor HP harus 10–12 digit.")
            break
        except ValueError as e:
            console.print(Panel(f"[red bold]Terjadi kesalahan![/red bold]\n{e}", title="🚨 ERROR", border_style="red"))
            enter()

    # ---- Gmail ----
    while True:
        try:
            email_input = input("Masukan Gmail (contoh: gugugaga@gmail.com): ")
            if not email_input.endswith("@gmail.com"):
                raise ValueError("Masukan Gmail yang benar!")
            break
        except ValueError as e:
            console.print(Panel(f"[red bold]Terjadi kesalahan![/red bold]\n{e}", title="🚨 ERROR", border_style="red"))
            enter()

    # ---- Alamat ----
    alamat_input = input("Masukan alamat anda: ")

    # ---- Username ----
    while True:
        try:
            username = input("Masukan Username Baru Anda: ")
            if len(username) < 4:
                raise ValueError("Username harus lebih dari 4 karakter!")
            elif username in list_username:
                raise ValueError("Username sudah ada!")
            break
        except ValueError as e:
            console.print(Panel(f"[red bold]Terjadi kesalahan![/red bold]\n{e}", title="🚨 ERROR", border_style="red"))
            enter()

    # ---- Password ----
    while True:
        try:
            password = input("Masukan Password Baru Anda: ")
            if len(password) < 4:
                raise ValueError("Password minimal 4 karakter")
            break
        except ValueError as e:
            console.print(Panel(f"[red bold]Terjadi kesalahan![/red bold]\n{e}", title="🚨 ERROR", border_style="red"))
            enter()

    # ---- Konfirmasi Password ----
    while True:
        try:
            password2 = input("Konfirmasi Password Anda Sekali Lagi: ")
            if password2 != password:
                raise ValueError("Password yang Anda Masukan Tidak Sama!")
            break
        except ValueError as e:
            console.print(Panel(f"[red bold]Terjadi kesalahan![/red bold]\n{e}", title="🚨 ERROR", border_style="red"))
            enter()

    # ---- Simpan ke CSV ----
    with open("dataadmin/datauser.csv", mode="a", newline="") as file:
        border = ["nama lengkap", "nomor hp", "gmail", "alamat", "username", "password"]
        writer = csv.DictWriter(file, fieldnames=border)
        writer.writerow({
            "nama lengkap": nama,
            "nomor hp": nomerhp,
            "gmail": email_input,
            "alamat": alamat_input,
            "username": username,
            "password": password2
        })
    os.makedirs(f"datauser/{nama}")
    with open(f"datauser/{nama}/riwayat_diagnosa.csv", mode = "w") as file : 
        writer = csv.writer(file)
        writer.writerow("")
    with open(f"datauser/{nama}/riwayat_pembelian.csv", mode = "w") as file : 
        writer = csv.writer(file)
        writer.writerow()
    console.print(Panel("[green bold]Registrasi berhasil! Silakan login.[/green bold]", title="✅ Sukses", border_style="green"))
    enter()
    bersihkan()
    #halaman
    

# ====Login====
def login_petani():
    global user_profil, nomer_hp_profil, list_gmail_profil, alamat_profil, list_pasword_profil, list_username_profil
    user_profil = []
    nomer_hp_profil = []
    list_gmail_profil = []
    alamat_profil = []
    list_pasword_profil = []
    list_username_profil = []
    eror = 0
    bersihkan()
    
    while True:
        user, nomer_hp, list_gmail, alamat, list_pasword, list_username = penampung_user()
        username =  input("Masukan Nama Anda: ")
        pasword = input("Masukan Pasword Anda: ")
        try:
            for i in range len()
            if username == list_username and pasword == list_pasword:
               
            else:
                break
        except ValueError as e:
            console.print(Panel(f"[red bold]Terjadi kesalahan![/red bold]\n{e}", title="🚨 ERROR", border_style="red"))
            enter()
            