def get_user_level(ask_level, levels):
    if ask_level == "легкий":
        words = levels[0]
    elif ask_level == "средний":
        words = levels[1]
    elif ask_level == "тяжелый":
        words = levels[2]
    else:
        words = levels[0]
    return words, ask_level


def base_program(words):
    answers = {}

    for key, value in words.items():
        print("Угадайте слово".center(40, "*"))
        asking = input(f"{key}, {len(value)} букв, начинается на "
                       f"{value[0]}...\n").strip().lower()

        if asking == value:
            answers[key] = True
            print(f"Верно, {key} — это {asking}.")
        else:
            answers[key] = False
            print(f"Неверно. {key} — это {value}.")
    return answers


def get_result(answers):
    correct_answers = 0
    right_answers = []
    wrong_answers = []

    for k, v in answers.items():
        if v is True:
            right_answers.append(k)
            correct_answers += 1
        elif v is False:
            wrong_answers.append(k)

    print("Правильно отвечены слова:")
    for rights in right_answers:
        print(rights)
    print()

    print("Неправильно отвечены слова:")
    for wrongs in wrong_answers:
        print(wrongs)
    print()
    return correct_answers, right_answers, wrong_answers


