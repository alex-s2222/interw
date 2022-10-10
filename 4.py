import json


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    number_questions = 0
    for i in data['game']['rounds']:
        for j in i['questions']:
            number_questions += 1

    print(f'number of correct answers {number_questions}')


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    for i in data['game']['rounds']:
        for j in i['questions']:
            print(f'right answer {j["correct_answer"]}')


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    max_time_to_answer = []

    for i in data['game']['rounds']:
        for j in i['questions']:
            if 'time_to_answer' in j:
                max_time_to_answer.append(j['time_to_answer'])
        for j in list(i.values()):
            if type(j) == dict:
                max_time_to_answer.append(j['time_to_answer'])

    print(max(max_time_to_answer))


def main(args):
    # data = {} # загрузить данные из test.json файла

    with open(args + '.json') as f:
        data = json.load(f)

    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    file_name = str(input())
    main(file_name)
