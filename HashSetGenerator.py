import csv
import hashlib

CSV_FILE = "top50_alphanum.csv"
OUTPUT_FILE = "top_50_passwords_with_duplicates.txt"

with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        for row in reader:
            password = row["Password"]
            frequency = int(row["Frequency"])
            # Write the password `frequency` times
            outfile.write((password + "\n") * frequency)

INPUT_FILE = "top_50_passwords_with_duplicates.txt"
OUTPUT_FILE = "hashed_50_passwords.csv"

with open(INPUT_FILE, "r", encoding="utf-8") as infile, \
        open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:

    writer = csv.writer(outfile)
    writer.writerow(["Password", "SHA1_Hash"])

    for line in infile:
        password = line.strip()

        sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest()
        writer.writerow([password, sha1_hash])