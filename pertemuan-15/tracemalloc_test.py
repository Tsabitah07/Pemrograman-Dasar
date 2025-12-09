import tracemalloc

def buat_list_besar ():
    return [i for i in range(1_000_000)]

tracemalloc.start()

buat_list_besar ()

current , peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Memori saat ini :", current)
print("Memori puncak :", peak)