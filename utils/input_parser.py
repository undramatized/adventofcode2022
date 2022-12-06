def txt_to_list(filepath):
    file = open(filepath, 'r')
    return file.readlines()


def txt_to_str(filepath):
    file = open(filepath, 'r')
    return file.readable()