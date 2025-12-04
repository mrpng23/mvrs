import json
import os
PATH = os.path.dirname(__file__)   # JSON will always loaded from script folder

def load_data():
    try:
        f = open(PATH + "/ratings.json", "r")
        data = json.load(f)
        f.close()
        return data
    except:
        print("Error reading ratings.json")
        return {}
def similarity(user, other):
    score = 0
    for book in user:
        if book in other:
            score = score + 1
    return score
def recommend(user, data):
    best_person = ""
    best_score = -1
    for name in data:
        score = similarity(user, data[name])
        if score > best_score:
            best_score = score
            best_person = name
    recs = []
    other_user_books = data[best_person]

    for book in other_user_books:
        if book not in user:
            if other_user_books[book] >= 4:
                recs.append(book)
    return recs
def main():
    data = load_data()
    user = {}
    print("Enter book titles and ratings (press ENTER to finish):")
    while True:
        book = input("Book: ")
        if book == "":
            break
        try:
            r = int(input("Rating 1-5: "))
            user[book] = r
        except:
            print("Error. Please enter a number.")

    recs = recommend(user, data)
    print("\nRecommended books:")
    for r in recs:
        print("-", r)

main()

print("Hello!")