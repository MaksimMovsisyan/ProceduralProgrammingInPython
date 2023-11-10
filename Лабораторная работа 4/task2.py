# TODO импортировать необходимые молули
import json, csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as file_csv:
        reader = csv.DictReader(file_csv, delimiter=',', quotechar='"')
        json_data = [row for row in reader]
     # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as file_json:
        json.dump(json_data, file_json, indent=4)
task()

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
