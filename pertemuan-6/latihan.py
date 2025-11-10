import basic_function as fnc

def score():
        exam_score = [78, 85, 90, 67, 88, 92, 74, 90, 81]
        search_score = 92

        print(fnc.min_score(exam_score))
        print(fnc.max_score(exam_score))

        fnc.search_score(exam_score, search_score)



def arrange_score():
        exam_score = [78, 85, 90, 67, 88, 92, 74, 90, 81]
        print(fnc.sorted_scores(exam_score))

        exam_score = [78, 85, 90, 67, 88, 92, 74, 90, 81]
        print(fnc.sorted_scores(exam_score, True))

        # print("Sorted scores highest to lowest:", sorted(exam_score, reverse=True))
        # print("Sorted scores lowest to highest:", sorted(exam_score))



def merged_list():
    produk_harga = [
        {"nama": "Laptop", "harga": 9500000},
        {"nama": "Mouse", "harga": 150000},
        {"nama": "Keyboard", "harga": 350000},
        {"nama": "Monitor", "harga": 2200000}
    ]

    produk_stok = [
        {"nama": "Laptop", "stok": 3},
        {"nama": "Mouse", "stok": 25},
        {"nama": "Keyboard", "stok": 10},
        {"nama": "Monitor", "stok": 4}
    ]

    merged = []
    for harga in produk_harga:
        for stok in produk_stok:
            if harga["nama"] == stok["nama"]:
                merged.append({
                    "nama": harga["nama"],
                    "harga": harga["harga"],
                    "stok": stok["stok"]
                })

    for id, item in enumerate(merged, start=1):
            print(f'{id}. Nama: {item["nama"]}, Harga: {item["harga"]}, Stok: {item["stok"]}')

    print(merged)



def list_operation():
    cabang_a = {"Andi", "Budi", "Citra", "Dewi", "Eka"}
    cabang_b = {"Budi", "Dewi", "Farah", "Gilang", "Hadi"}

    list_and = cabang_a & cabang_b
    list_or = cabang_a | cabang_b
    list_not_in_b = cabang_a - cabang_b
    list_not_in_a = cabang_b - cabang_a
    list_xor = cabang_a ^ cabang_b

    print(list_and)
    print(list_or)
    print(list_not_in_b)
    print(list_not_in_a)
    print(list_xor)



# score()
arrange_score()
# merged_list()
# list_operation()