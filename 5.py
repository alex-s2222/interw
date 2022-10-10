import os


def task1():
    # в папке test найти все файлы filenames вывести колличество
    dir_name = 'C:/Users/Admin/Desktop/пустяки/interview/test'

    res = []
    for (dir_path, dir_names, file_names) in os.walk(dir_name):
        res.extend(file_names)

    count_filenames = res.count('filenames.txt')
    print(f'count filenames {count_filenames}')


def task2():
    # в папке test найти все email адреса записанные в файлы
    dir_name = 'C:/Users/Admin/Desktop/пустяки/interview/test'

    for (dir_path, dir_names, file_names) in os.walk(dir_name):
        if file_names:
            for file in file_names:
                dir_file = dir_path+"/"+file
                if os.path.getsize(dir_file) > 0:
                    with open(dir_path+"/"+file) as f:
                        lines = f.readlines()
                        for line in lines:
                            if '@' in line:
                                print(line, end='')


def main():
    task1()
    task2()


if __name__ == '__main__':
    main()
