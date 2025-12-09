import tracemalloc

def tidak_efisien ():
    data = list(range(200_000))
    for _ in range(100):
        data = data [:] # banyak salinan

    return data

def efisien ():
    data = list(range(200_000))
    for i in range(len(data)):
        data[i] *= 2

    return data

tracemalloc.start()
tidak_efisien ()
current1, peak1 = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
efisien ()
current2, peak2 = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Tidak efisien - Memori saat ini :", current1)
print("Tidak efisien - Memori puncak :", peak1 ,"\n")
print("Efisien - Memori saat ini :", current2)
print("Efisien - Memori puncak :", peak2)