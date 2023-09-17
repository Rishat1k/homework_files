with open('recipes.txt', 'r', encoding='utf-8') as f:
    lst_of_dishes = []
    lst = []
    for row in f.readlines():
        if row.strip() != '':
            lst.append(row.strip())
        else:
            lst_of_dishes.append(lst)
            lst = []
            continue
    lst_of_dishes.append(lst)

cook_book = {}
for dish in lst_of_dishes:
    lst = []
    for i in range(2, len(dish)):
        ingredient_name, quantity, measure = dish[i].split(' | ')
        lst.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
    cook_book[dish[0]] = lst
print(cook_book)


