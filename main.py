import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# dataset dari tugas modul 3
data = {
    "ID_Transaksi": range(1, 21),
    "Produk": ["Bakso", "Mie Ayam", "Soto", "Nasi Goreng", "Ayam Geprek", "Bakso", "Mie Ayam", "Soto", "Nasi Goreng", "Ayam Geprek",
                "Bakso", "Mie Ayam", "Soto", "Nasi Goreng", "Ayam Geprek", "Bakso", "Mie Ayam", "Soto", "Nasi Goreng", "Ayam Geprek"],
    "Jumlah": [2, 1, 3, 2, 1, 5, 3, 2, 4, 3, 2, 6, 3, 1, 2, 5, 2, 3, 4, 2],
    "Harga_Satuan": [15000, 12000, 18000, 20000, 22000, 15000, 12000, 18000, 20000, 22000,
                     15000, 12000, 18000, 20000, 22000, 15000, 12000, 18000, 20000, 22000],
}

df = pd.DataFrame(data)

# Menambahkan kolom Total_Harga
df["Total_Harga"] = df["Jumlah"] * df["Harga_Satuan"]

# Menambahkan kolom Diskon 10% jika Total_Harga > 50000
df["Total_After_Diskon"] = df["Total_Harga"].apply(lambda x: x * 0.9 if x > 50000 else x)
print("Ringkasan Statistik:\n", df.describe())

# Visualisasi distribusi Total_Harga
plt.figure(figsize=(8,5))
sns.histplot(df["Total_Harga"], bins=10, kde=True, color='blue')
plt.title("Distribusi Total Harga")
plt.xlabel("Total Harga")
plt.ylabel("Frekuensi")
plt.show()

# Visualisasi hubungan antara Jumlah dan Total Harga
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["Jumlah"], y=df["Total_Harga"], hue=df["Produk"], palette="viridis")
plt.title("Jumlah vs Total Harga")
plt.xlabel("Jumlah Produk")
plt.ylabel("Total Harga")
plt.show()

# Korelasi antar variabel numerik
plt.figure(figsize=(6, 4))
numeric_df = df.select_dtypes(include=["number"])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt='.2f')
plt.title("Heatmap Korelasi")
plt.show()

