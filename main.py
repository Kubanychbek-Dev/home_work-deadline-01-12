import json
import os
import utils


def get_questions():
    with open("questions.json", encoding="utf-8") as file:
        content = json.load(file)
        for data in content:
            my_list = data.get("questions")
            return my_list


while True:
    ask_name = input("Ваше имя\n").strip().title()
    if ask_name == "":
        print("Введите имя")
    elif ask_name.isalpha() is False:
        print("Введите только буквы!")
    else:
        break

print("Проверим ваш уровень английского языка?")
ask_level = input("Выберите один из 3х уровней сложности:"
                  "\n-легкий\n-средний\n-тяжелый\n").strip().lower()


json_questions = get_questions()
get_levels = utils.get_user_level(ask_level, json_questions)
get_words = utils.base_program(get_levels[0])
get_answers = utils.get_result(get_words)


with open("questions.json", encoding="utf-8") as levels:
    level_data = json.load(levels)
    for i in level_data:
        levels_dict = i.get("levels")

print(f"Ваш ранг: {levels_dict.get(str(get_answers[0]))}")

level_name = ""
if ask_level not in ["легкий", "средний", "тяжелый"]:
    level_name = "легкий"
else:
    level_name = ask_level

result_dict = {
    "user_name": ask_name,
    "level": level_name,
    "correct_answers": get_answers[1],
    "wrong_answers": get_answers[2],
    "rank": levels_dict.get(str(get_answers[0]))
}


def create_json():
    with open("english_result.json", encoding="utf-8") as file:
        data = json.load(file)

    with open("english_result.json", "w", encoding="utf-8") as file_2:
        data.append(result_dict)
        json.dump(data, file_2, ensure_ascii=False, indent=2)


def check_json_exist():
    if os.path.exists("english_result.json") is False:
        with open("english_result.json", "w", encoding="utf-8") as file:
            json.dump([], file)
        create_json()
    elif os.path.exists("english_result.json") is True:
        create_json()


check_json_exist()