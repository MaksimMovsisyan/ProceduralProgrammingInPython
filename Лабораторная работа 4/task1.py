# TODO решите задачу
import json

def task() -> float:
    file_name = 'input.json'
    with open(file_name) as file:
        data = json.load(file)
    return sum([dict_['score']*dict_['weight'] for dict_ in data])



print(f'{task():0.3f}')
