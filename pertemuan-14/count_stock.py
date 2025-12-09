stok = {"pensil": 10, "buku": 5, "pulpen": 8}

def tambah_stok(item , jumlah):
    if jumlah < 0:
        print(f"Error: Cannot add negative stock for {item}.")
        return
    if item in stok:
        stok[item] = stok[item] + jumlah
    else:
        stok[item] = jumlah

def kurang_stok(item , jumlah):
    if item in stok:
        if stok[item] - jumlah >= 0:
            stok[item] = stok[item] - jumlah
        else:
            print(f"Warning: Not enough stock for {item}. Setting stock to 0.")
            stok[item] = 0
    else:
        print(f"Error: Item {item} not found in stock.")

def transaksi():
    keranjang = {"pensil": 3, "buku": 2}
    total = 0

    for item , qty in keranjang.items():
        kurang_stok(item , qty)
        total += qty

    return total

def main():
    print("Stok awal:", stok)
    transaksi()
    kurang_stok("pulpen", -3)
    transaksi()
    print("Stok akhir:", stok)

if __name__ == "__main__":
    main()