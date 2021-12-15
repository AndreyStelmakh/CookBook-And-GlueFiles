def parse_cook_book_file(filename):
    cook_book = {}
    with open(filename, encoding="utf-8") as file:
        dish = file.readline().strip()  # Название блюда
        while dish != '':
            ingredient_count = int(file.readline())
            ingredients = []
            while ingredient_count:
                ingredient = {}
                line = file.readline()
                items = line.split('|')
                ingredient["ingredient_name"] = items[0].strip()
                ingredient["quantity"] = int(items[1].strip())
                ingredient["measure"] = items[2].strip()

                ingredients.append(ingredient)
                ingredient_count -= 1

            cook_book[dish] = ingredients
            file.readline()  # Пустая строка
            dish = file.readline().strip()  # Название блюда

    return cook_book


print(parse_cook_book_file("recipes.txt"))


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = parse_cook_book_file("recipes.txt")
    result = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient["ingredient_name"]
            if ingredient_name in result:
                result[ingredient_name]["quantity"] += ingredient["quantity"] * person_count
            else:
                result[ingredient_name] = {"measure": ingredient["measure"],
                                           "quantity": ingredient["quantity"] * person_count}
    return result


print(get_shop_list_by_dishes(["Омлет", "Омлет"], 2))

