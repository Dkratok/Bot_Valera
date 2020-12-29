def read_whole_file(filename):
    with open(filename, mode='r', encoding='utf-8') as fl:
        return fl.read()
