import hashlib
import csv
import random
import string
import time

def fixedUserAttack(user, userDict, passwords):
    hash = userDict.get(user)
    count = 0

    for p in passwords:
        count += 1
        if hashlib.sha1(p.encode("utf-8")).hexdigest() == hash:
            return p, count
    return "NOT FOUND", 0

def genUsers():
    userDict = dict()
    hashes = []

    with open("hashed_50_passwords.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            hashes.append(row["SHA1_Hash"])


    count = 0

    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                for d in string.ascii_lowercase:
                    for e in string.ascii_lowercase:
                        userDict[a+b+c+d+e] = hashes[count]
                        count += 1

                        if count == len(hashes):
                            return userDict


if __name__ == "__main__":
    passwords = []

    with open("top50_alphanum.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            password = row["Password"]
            passwords.append(password)

    userDict = genUsers()

    ev = 0

    for i in range(10000):
        user = random.choice(list(userDict))
        pwrd = fixedUserAttack(user, userDict, passwords)[0]
        tries = fixedUserAttack(user, userDict, passwords)[1]
        userDict.pop(user)
        ev += tries

    print("Average tries:" + str(float(ev)/10000.0))