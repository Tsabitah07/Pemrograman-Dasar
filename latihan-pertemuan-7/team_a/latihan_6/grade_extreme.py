# Pastikan Anda sudah membuat file grades.csv dengan isi sesuai soal.
import csv
from collections import defaultdict

FILENAME_INPUT = "grade.csv"
FILENAME_OUTPUT = "summary.csv"


def grades_extremes():
    # 3. Kelompokkan data berdasarkan mata kuliah
    course_scores = defaultdict(list)

    try:
        # 1. Baca grades.csv
        with open(FILENAME_INPUT, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, skipinitialspace=True)
            for row in reader:
                # 2. Gunakan kolom course dan score
                course = row['course'].strip()
                try:
                    # Konversi score ke integer
                    score = int(row['score'].strip())
                except ValueError:
                    continue

                course_scores[course].append(score)

    except FileNotFoundError:
        print(f"Error: File input {FILENAME_INPUT} tidak ditemukan.")
        return

    summary_data = []
    # 4. Hitung nilai maksimum dan minimum untuk setiap mata kuliah
    for course, scores in course_scores.items():
        if scores:
            max_score = max(scores)
            min_score = min(scores)

            summary_data.append({
                'course': course,
                'max': max_score,
                'min': min_score
            })

    # 5. Simpan hasil ke summary.csv
    fieldnames = ['course', 'max', 'min']
    with open(FILENAME_OUTPUT, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(summary_data)

    print(f"Summary nilai disimpan di {FILENAME_OUTPUT}.")


if __name__ == "__main__":
    grades_extremes()