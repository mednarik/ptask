import json, curses

def get_data() -> dict:
    with open("data.json", "r") as file:
        data = json.load(file)
    return data
    

def get_draw_string(data: dict):
    string = ""
    for task in data:
        string += f"{task} {data[task]['deadline']}\n"
    return string


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(get_draw_string(get_data()))

    while True:
        key = stdscr.getch()

        if key == ord("n"):
            break
        
curses.wrapper(main)
