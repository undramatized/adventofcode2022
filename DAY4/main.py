from utils.input_parser import txt_to_list

INPUT_PATH = "./input"
SAMPLE_PATH = "./sample"

def get_range_from_str(range_str):
    str_split = range_str.split("-")
    return range(int(str_split[0]), int(str_split[1]))

def is_subset(rangeA, rangeB):
    if rangeA.start >= rangeB.start and rangeA.stop <= rangeB.stop:
        return True
    else:
        return False

def has_subset(rangeA, rangeB):
    # print(rangeA, rangeB)
    return is_subset(rangeA, rangeB) or is_subset(rangeB, rangeA)

def get_total_subsets(input):
    total_count = 0

    for pair in input:
        pair_split = pair.split(",")
        rangeA = get_range_from_str(pair_split[0])
        rangeB = get_range_from_str(pair_split[1])
        if has_subset(rangeA, rangeB):
            print(rangeA, rangeB)
            total_count += 1

    return total_count

def has_overlap(rangeA, rangeB):
    if rangeA.start > rangeB.stop or rangeB.start > rangeA.stop:
        return False
    else:
        return True

def get_total_overlaps(input):
    total_count = 0

    for pair in input:
        pair_split = pair.split(",")
        rangeA = get_range_from_str(pair_split[0])
        rangeB = get_range_from_str(pair_split[1])
        if has_overlap(rangeA, rangeB):
            print(rangeA, rangeB)
            total_count += 1

    return total_count

if __name__ == '__main__':
    print(get_total_overlaps(txt_to_list(INPUT_PATH)))