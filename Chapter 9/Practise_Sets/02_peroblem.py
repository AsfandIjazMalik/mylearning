# 02_Problem
# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

lst = [1, 2, 'Asfand', 33, 'Faisal',4, '77', True]

for index, item in enumerate(lst):
    if index == 2:
        print(item)
    elif index == 4:
        print(item)
    elif index == 6:
        print(item)
        
print('with or operator')
for idx, itm in enumerate(lst):
    if idx == 2 or idx == 4 or idx == 6 :
        print(itm)