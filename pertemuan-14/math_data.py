def hitung_rata(data):
    cache = {"sum": 0, "count": 0}
    for x in data:
        cache["sum"] += x
        cache["count"] += 1

    return f"{cache['sum'] / cache['count']:.2f}"

def median(data):
    data.sort()
    mid = len(data) // 2
    if len(data) % 2 == 0:
        return f'{(data[mid + 1] + data[mid]) / 2:.2f}'
    else:
        return f'{data[mid]:.2f}'

def modus(data):
    frekuensi = {}
    for x in data:
        frekuensi[x] = frekuensi.get(x, 0) + 1
    sorted_items = sorted(frekuensi.items(), key=lambda y: y[1], reverse=True)

    return f'{sorted_items[0][0]:.2f}'

def convert_to_float(data):
    return [float(x) for x in data]

def main():
    score = [70, 80, 80, 90, 100]
    print("Rata-rata:", hitung_rata(score))
    print("Median:", median(score))
    print("Modus:", modus(score))

    score.append(80.5)
    print("Rata-rata setelah ditambah 80.5:", hitung_rata(score))
    print("Median setelah ditambah 80.5:", median(score))
    print("Modus setelah ditambah 80.5:", modus(score))

if __name__ == "__main__":
    main()