"""✅ Project 1:"""

movie1 = input("Please Enter your first favorite movie: ")
movie2 = input("Please Enter your second favorite movie: ")
movie3 = input("Please Enter your third favorite movie: ")

movie_list = [movie1, movie2, movie3]

print("Your fovorite movies are" , movie_list)
print("First movie:" , movie_list[0])
print("Last movie:" , movie_list[2])
print("Total movie:" , len(movie_list))


"""✅ Project 2:"""

birth_year = input("Please Enter your birth year: ")
age = 2025 - int(birth_year)
if age < 18:
    print("You are not an adult")
else:
    print("You are an adult")

✅ Project 3:

sentence = input("Please Enter your sentence: ")

words = sentence.split()

print("Character count:", len(sentence.replace(" ", "")))
print("Word count:", len(words))
print("Unique words:", len(set(words)))
print("Longest word:", max(words, key=len))



"""✅ Project 4:"""

products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}
basket = []
total_price = 0

for i in range(3):
    item = input(f"Please Enter product {i+1}: ").lower()
    if item in products:
        basket.append(item)
        total_price += products[item]
    else:
        print("Sorry, product not found.")

print(f"Your Basket:" , " , ".join(basket))
print(f"Total price:" , total_price, "€")

"""✅ Project 5:"""
students = {}

for i in range(3):
    name = input(f"Enter the name of student {i+1}: ")
    grades = []


    for j in range(3):
        grade = int(input(f"Enter grade {j+1} for {name}: "))
        grades.append(grade)

    students[name] = grades

print("\n--- Student Averages ---")
highest_avg = 0
top_student = ""

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{name}: {avg:.2f}")

    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print(f"\nHighest average: {highest_avg:.2f} → {top_student}")

✅ Project 6: 

kitapListesi = {}
while True:
    giris = input("kitap eklemek iicn 1, \nodunc almak icin 2, \niade icin 3\n, tum kitaplari goruntulemek icin 4\n, cikis icin bes basiniz")
    if giris == "1":
        kitapAdi= input("Kitap ismii girin").upper()
        kitap={kitapAdi:"Available"}
        kitapListesi.update(kitap)
    elif (giris == "2"):
        kitapIsmi = input("alincak kitabi yazin").upper()
        kitapListesi[kitapIsmi]= "kullanilmaz"
        print("Kitap odunc verirdi")
    elif(giris=="3"):
        kitapIsmi = input("kistap ismi").upper()

        kitapListesi[kitapIsmi]="Available"
    elif(giris == "4"):
        print(kitapListesi)
    elif(giris == "5"):
        break
    else:
        print("Gecerli bisiler girin")


