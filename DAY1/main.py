from utils.input_parser import txt_to_list

INPUT_PATH = "./input"
SAMPLE_PATH = "./sample"


def get_max_calories(input):
    max_val = 0
    curr_sum = 0
    elf_calories = {}
    elf_count = 1

    for i, val in enumerate(input):
        if val in ['\n', '\r\n']:
            elf_calories[i] = curr_sum
            max_val = curr_sum if curr_sum > max_val else max_val
            curr_sum = 0
            elf_count += 1
        else:
            curr_sum += int(val.strip())

    return max_val


def get_top_three_calories(input):
    curr_sum = 0
    all_calories = []
    elf_calories = {}
    elf_count = 1

    for i, val in enumerate(input):
        if val in ['\n', '\r\n']:
            elf_calories[i] = curr_sum
            all_calories.append(curr_sum)
            curr_sum = 0
            elf_count += 1
        else:
            curr_sum += int(val.strip())

    elf_calories[i] = curr_sum
    all_calories.append(curr_sum)

    top_three = sorted(all_calories, reverse=True)[0:3]
    return top_three


if __name__ == '__main__':
    result = get_top_three_calories(txt_to_list(INPUT_PATH))
    print(sum(result))