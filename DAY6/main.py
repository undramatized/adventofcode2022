INPUT_PATH = "./input"
SAMPLE_PATH = "./sample"


def get_marker(stream):
    curr_marker = 0
    curr_window = []
    for char in stream:
        curr_marker += 1
        if len(curr_window) < 14:
            curr_window.append(char)
            continue
        else:
            curr_window.pop(0)
            curr_window.append(char)
            if all_unique(curr_window):
                break

    return curr_marker


def all_unique(window):
    return len(set(window)) == len(window)


if __name__ == '__main__':
    with open(INPUT_PATH, 'r') as file:
        data = file.read().replace('\n', '')
        print(get_marker(data))
