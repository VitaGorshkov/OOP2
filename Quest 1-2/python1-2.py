cook_book = {}
ingredients_list = []

with open('recipes.txt') as f:
    lines = f.readlines()
    def list_of_name_dish(lines):
        dish = []
        for xid, line in enumerate(lines):
            if xid == 0:
                dish.append(line.strip())
            elif len(line) == 1:
                dish.append(lines[xid + 1].strip())
        return len(dish)


def book():
    with open('recipes.txt') as f:
        cook_book = {}
        i = 1
        while i <= list_of_name_dish(lines):
                ingredients_list = []
                dish_name = f.readline().strip()
                ingridients_qty = int(f.readline().strip())
                for ingredient_line in range(ingridients_qty):
                    ingridients_qty -= 1
                    ingridient_dict = {}
                    item1, item2, item3 = f.readline().split("|")
                    ingridient_dict['ingredient_name'] = item1.strip(' ')
                    ingridient_dict['quantity'] = item2.strip(' ')
                    ingridient_dict['measure'] = item3.strip(' \n')
                    ingredients_list.append(ingridient_dict)
                    cook_book[dish_name] = ingredients_list
                end = f.readline().strip()
                i += 1
        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    list_grocery = {}
    for dish in dishes:
        if dish in book().keys():
            
            for ingridient in book()[dish]:
                dict_ingridients = {}
                if ingridient['ingredient_name'] not in list_grocery.keys():
                    list_grocery[ingridient['ingredient_name']] = {}
                    dict_ingridients['measure'] = ingridient['measure']
                    dict_ingridients['quantity'] = int(ingridient['quantity']) * person_count
                    list_grocery[ingridient['ingredient_name']] = dict_ingridients
                else:
                   list_grocery[ingridient['ingredient_name']]['quantity'] = int((int(list_grocery[ingridient['ingredient_name']]['quantity']) / 
                        + int(ingridient['quantity'])) * person_count)

                        
                
    
    
    print(list_grocery)





get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1)



