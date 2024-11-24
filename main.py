import json
import utils


def get_questions():
    with open("questions.json", encoding="utf-8") as file:
        content = json.load(file)
        for data in content:
            my_list = data.get("questions")
            return my_list


print("Проверим ваш уровень английского языка?")
ask_level = input("Выберите один из 3х уровней сложности:"
                  "\n-легкий\n-средний\n-тяжелый\n").strip().lower()


json_questions = get_questions()
get_levels = utils.get_user_level(ask_level, json_questions)
get_words = utils.base_program(get_levels)
get_answers = str(utils.get_result(get_words))


with open("questions.json", encoding="utf-8") as levels:
    level_data = json.load(levels)
    for i in level_data:
        levels_dict = i.get("levels")

print(f"Ваш ранг: {levels_dict.get(get_answers)}")
