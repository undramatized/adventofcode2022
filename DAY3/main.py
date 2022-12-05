from utils.input_parser import txt_to_list

SAMPLE_PATH = "./sample"
INPUT_PATH = "./input"

def get_priority(char):
    char_int = ord(char)
    if char_int <= 90:  # uppercase
        return char_int - 64 + 26
    else:               # lowercase
        return char_int - 96

def get_common_char(str_a, str_b):
    print(str_a, str_b)
    list_a = [*str_a]
    for char in str_b:
        if char in list_a:
            return char
    return False

def get_common_item(bag_str):
    item_cnt = len(bag_str)
    half_cnt = int(item_cnt/2)
    comp_a = bag_str[0:half_cnt]
    comp_b = bag_str[half_cnt:item_cnt]
    return get_common_char(comp_a, comp_b)

def get_total_priority(input):
    total_priority = 0
    for bag in input:
        comm_char = get_common_item(bag.strip())
        total_priority += get_priority(comm_char)

    return total_priority

def get_group_badge(str_a, str_b, str_c):
    list_a = [*str_a]
    comm_chars = []
    for char in str_b:
        if char in list_a:
            comm_chars.append(char)

    for char in str_c:
        if char in comm_chars:
            return char

    return False

def get_group_priorities(input):
    total_priority = 0
    for i in range(0, len(input), 3):
        comm_char = get_group_badge(input[i], input[i+1], input[i+2])
        print(comm_char)
        total_priority += get_priority(comm_char)

    return total_priority



if __name__ == '__main__':
    # char_list = ["a", "b", "y", "z", "A", "B", "Y", "Z"]
    # for char in char_list:
    #     print(get_priority(char))

    # print(get_total_priority(txt_to_list(INPUT_PATH)))

    print(get_group_priorities(txt_to_list(INPUT_PATH)))
