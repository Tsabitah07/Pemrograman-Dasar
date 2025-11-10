import os

FILENAME_INPUT = "resto_review.txt"
FILENAME_OUTPUT = "filtered_review.txt"
KEYWORDS = ["enak", "murah"]


def filter_reviews():
    filtered_lines = []

    # 1. Buka berkas resto_reviews.txt
    try:
        with open(FILENAME_INPUT, "r", encoding="utf-8") as file_in:
            for line in file_in:
                # Membersihkan baris dari spasi di awal/akhir dan mengubah ke lowercase
                clean_line = line.strip()
                line_lower = clean_line.lower()

                # 2. Periksa baris yang mengandung kata "enak" atau "murah"
                is_match = False
                for keyword in KEYWORDS:
                    if keyword in line_lower:
                        is_match = True
                        break

                if is_match:
                    # Tambahkan baris asli ke list (dengan newline untuk penulisan)
                    filtered_lines.append(clean_line + "\n")

    except FileNotFoundError:
        print(f"Error: File input {FILENAME_INPUT} tidak ditemukan.")
        return

    # 3. Simpan hasil ke berkas filtered_reviews.txt
    with open(FILENAME_OUTPUT, "w", encoding="utf-8") as file_out:
        file_out.writelines(filtered_lines)

    # 4. Tampilkan isi hasil di terminal
    print(f"Hasil filter disimpan di {FILENAME_OUTPUT}.")
    print("\n--- Isi filtered_reviews.txt ---")
    for line in filtered_lines:
        print(line.strip())
    print("---------------------------------")


if __name__ == "__main__":
    filter_reviews()