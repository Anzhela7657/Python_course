'''1. A. Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
B. To each file append a random number between 1 and 100.
C. Create a summary file (summary.txt) that contains name of the file and number in that file'''

from random import randint as rd

for i in range(ord('A'), ord('Z') + 1):
    # print(chr(i))
    with open(chr(i) + '.txt', mode = 'w') as file:
        file.write(str(rd(0, 100)))

#2.Create file with some content. Create second file and copy content of the first file to the second file in upper case.

data = '''Тому що ніколи тебе не вирвеш,
    ніколи не забереш,
    тому що вся твоя свобода
    складається з меж,
    тому що в тебе немає
    жодного вантажу,
    тому що ти ніколи не слухаєш,
    оскільки знаєш і так,
    що я скажу'''
with open('../homework/text.txt', 'w') as file:
    text = file.write(data)
with open('../homework/text.txt', 'r') as file:
    text1 = (file.read()).upper()
with open('../homework/copy.txt', 'w') as file:
    text2 = file.write(text1)

#3.Write a program that will simulate user score in a game.
import random
import csv

list = ['Mark', 'Alice', 'Viki', 'Kate', 'John']
games =[]
for player in list:
    for game in range(100):
        score = random.randint(0,1000)
        games.append([player,score])
with open('../homework/scores.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Score'])
    writer.writerows(games)

'''4. Write a script that reads the data from previous CSV file and creates a new file called 
high_scores.csv where each row contains the player name and their highest score. 
Final score should sorted by descending of highest score'''
import csv

scores = []
with open('../homework/scores.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        player = row[0]
        score = int(row[1])
        scores.append((player, score))
scores.sort(key=lambda x: x[1], reverse=True)
high_scores = {}
for player, score in scores:
    if player not in high_scores:
        high_scores[player] = score
with open('../homework/high_scores.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Highest Score'])
    writer.writerows(high_scores.items())


