# PUIT GAMING OS - FINAL BOSS EDITION
# Dari Makassar, Dibuat di Termux HP
# Mantan bocah phishing 2023, sekarang jadi Defender 2026

print("=== PUIT GAMING OS - FINAL BOSS 🛡️ ===")
print("Defender Makassar Ready!\n")

# 1. KASIR WARNET SULTAN
nama = input("Nama pelanggan: ")
jam = int(input("Main berapa jam: "))
tarif = 5000
total = jam * tarif

# Fitur Diskon Sultan 20%
if jam >= 5:
    diskon = total * 0.2
    total = total - diskon
    print(f"DAPAT DISKON SULTAN 20%! Potongan: Rp {diskon}")
else:
    print("Main kurang dari 5 jam, belum dapat diskon sultan")

print(f"Total bayar {nama}: Rp {total}")

# Simpan laporan
with open("laporan_puit.txt", "a") as f:
    f.write(f"{nama} main {jam} jam - bayar Rp {total}\n")
print("Laporan kesimpen di laporan_puit.txt\n")

# 2. ANTI PHISHING DEFENDER
print("=== ANTI PHISHING DEFENDER ===")
link = input("Cek link mencurigakan (contoh: facebook.com): ")

link_bahaya = [".tk", "free-pulsa", "gratis-diamond", "fb-hadiah", "login-fb"]
aman = True
for bahaya in link_bahaya:
    if bahaya in link.lower():
        aman = False

if not aman:
    print("🚨 BAHAYA! INI LINK PHISHING! JANGAN DI KLIK!")
    print("Ini trik anak phishing 2023 kayak lu dulu!")
else:
    print("✅ Link aman, lanjutkan Defender!")

print("\nSelesai. Warnet Puit Gaming OS Siap Tempur!")