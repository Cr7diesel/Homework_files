import os

DIR_NAME = 'texts'
BASE_PATH = os.getcwd()
files = os.listdir(DIR_NAME)


def txt_merge():
    lines = []
    files_dict = {}

    for file in files:
        with open(os.path.join(BASE_PATH, DIR_NAME, file), encoding='utf-8') as f:
            file_list = f.readlines()
            lines.append(len(file_list))
            files_dict[len(file_list)] = (file, file_list)

    lines.sort()

    with open(os.path.join(BASE_PATH, DIR_NAME, 'final.txt'), 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(files_dict[line][0])
            f.write('\n')
            f.write(str(line))
            f.write('\n')
            f.writelines(files_dict[line][1])
            f.write('\n')


txt_merge()
