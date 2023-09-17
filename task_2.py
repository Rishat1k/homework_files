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

def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for dish in dishes:
        for lst in cook_book[dish]:
            if lst['ingredient_name'] in shop_dict:
                shop_dict[lst['ingredient_name']]['quantity'] += int(lst['quantity']) * person_count
            else:
                shop_dict[lst['ingredient_name']] = {'measure': lst['measure'], 'quantity': int(lst['quantity'])*person_count}
    return shop_dict

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

