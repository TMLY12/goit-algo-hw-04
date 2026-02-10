def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                cat_info = {
                    "id": parts[0],
                    "name": parts[1],
                    "price": parts[2],
                    }
                cats_list.append(cat_info)
        return cats_list
    except FileNotFoundError:
        print(f"Ошибка: Файл по адресу {path} не найден.")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []
if __name__ == "__main__":
    cats = get_cats_info("cats_info.txt")
    for cat in cats:
        print(cat)