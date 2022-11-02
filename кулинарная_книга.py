
with open("кулинарная_книга.txt", "r", encoding="utf8") as f:
    a = f.readlines()
    l = [line.rstrip() for line in a]
    cook_book = {}

    def transformation (value):
        try :
            return int(value)
        except (ValueError, TypeError):
            return value
    l_1 = [transformation (i) for i in l]

    for i in range (0, (len(l_1)-1)):
       if type(l_1[i]) == int :
           ingredient = []
           cook_book[l_1[i-1]] = ingredient
           index = 1
           while index <= l_1[i]:
                dict_ingradient = {}
                ingradient = (l_1[i+index]).split("|")
                dict_ingradient["ingredient_name"] = ingradient[0]
                dict_ingradient["quantity"] = ingradient[1]
                dict_ingradient["measure"] = ingradient[2]
                ingredient.append(dict_ingradient)
                index += 1

print(cook_book)
print(cook_book["Омлет"])
print(cook_book["Омлет"][0]["ingredient_name"])
def get_shop_list_by_dishes(dishes, person_count):
    shop_ingedients = {}
    j = 0
    while j < len(dishes):
        dishes_num = dishes[j]
        i = 0
        while i < len(cook_book[dishes_num]):
            key_shop = cook_book[dishes_num][i]["ingredient_name"]
            dict_count = {}
            shop_ingedients[key_shop] = dict_count
            dict_count["measure"] = cook_book[dishes_num][i]["measure"]
            shop_count = int(cook_book[dishes_num][i]["quantity"]) * person_count
            dict_count["quantity"] = shop_count
            i += 1
        j += 1
    print(shop_ingedients)
get_shop_list_by_dishes(["Омлет", "Запеченный картофель"], 2)



#
