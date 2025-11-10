FILENAME_INPUT = "comment.txt"
FILENAME_OUTPUT = "report.txt"
KEYWORDS = {"bagus": 0, "mantap": 0}
total_lines = 0


def count_tech_words():
    global total_lines
    try:
        # 1. Buka berkas tech_news.txt
        with open(FILENAME_INPUT, "r", encoding="utf-8") as file_in:
            for line in file_in:
                total_lines += 1
                line_lower = line.strip().lower()

                # 2. Hitung berapa kali kata AI dan robot muncul
                # Menggunakan line.count() untuk menghitung semua kemunculan di baris
                KEYWORDS["bagus"] += line_lower.count("bagus")
                KEYWORDS["mantap"] += line_lower.count("mantap")

    except FileNotFoundError:
        print(f"Error: File input {FILENAME_INPUT} tidak ditemukan.")
        return

    # 3. Tulis hasil ke report.txt
    report_content = [
        f"Total lines: {total_lines}\n",
        f'Filtered Comment (Bagus / Mantap) : {KEYWORDS['bagus'] + KEYWORDS['mantap']}\n',
        f"Count of \"Bagus\": {KEYWORDS['bagus']}\n",
        f"Count of \"Mantap\": {KEYWORDS['mantap']}\n"
    ]

    with open(FILENAME_OUTPUT, "w", encoding="utf-8") as file_out:
        file_out.writelines(report_content)

    # 4. Tampilkan isi laporan di terminal
    print(f"Laporan disimpan di {FILENAME_OUTPUT}.")
    print("\n--- Isi report.txt ---")
    for line in report_content:
        print(line.strip())
    print("------------------------")


if __name__ == "__main__":
    count_tech_words()