def kelompokkan_penjualan(transaksi):

    data_per_bulan = dict.fromkeys(range(1, 13), [])

    for bulan , nilai in transaksi:
        if bulan in data_per_bulan:
            data_per_bulan[bulan] = data_per_bulan[bulan] + [nilai]

    empty_months = [bulan for bulan, daftar in data_per_bulan.items() if len(daftar) == 0]
    for bulan in empty_months:
        del data_per_bulan[bulan]

    return data_per_bulan

def hitung_total_per_bulan(data_per_bulan):
    total = {}
    for bulan , daftar_nilai in data_per_bulan.items():
        total[bulan] = sum(daftar_nilai)

    return total

def main():
    transaksi = [
        (1, 100000),
        (1, 150000),
        (2, 200000),
        (3, 50000),
        (3, 75000),
        (12, 300000),
    ]

    data_per_bulan = kelompokkan_penjualan(transaksi)
    print("Data per bulan:", data_per_bulan)

    total = hitung_total_per_bulan(data_per_bulan)
    print("Total per bulan:", total)

if __name__ == "__main__":
    main()