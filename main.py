#Порахуємо символи. Принципову роль тут відіграє
#саме довжина рядку, тому користуватимемось len()
file = open("demofile.txt", "r")
text = file.read()
number_of_characters = len(text)
print('Number of characters in text file :', number_of_characters)

#Порахуємо слова. Просто "розіб'ємо" файл
# на окремі слова за допомогою "split"
# і порахуємо їх
file = open("demofile.txt", "rt")
text = file.read()
words = text.split()
print('Number of words in text file :', len(words))