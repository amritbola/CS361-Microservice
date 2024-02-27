import json
import random

random.seed()

with open('exercises.json') as fp:
    data = json.load(fp)

def exercise_randomizer():
    random_num = random.randint(0, 872)
    response = data["exercises"][random_num]
    return response

