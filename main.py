import json

def draw(data: dict):
    for task in data:
        print(f"{task} {data[task]["deadline"]}")

with open("data.json", "r") as file:
    data = json.load(file)

draw(data)
