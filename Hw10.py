cats = []
number = int(input('Enter the number of cat: '))
for i in range(1, number+1):
    for j in range(1, number+1):
        if j % i == 0:
            if j in cats:
                cats.remove(j)
            else:
                cats.append(j)
print('The cats with hats are: ', cats)