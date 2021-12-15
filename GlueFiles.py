from operator import itemgetter


def num_lines_in_file(filename):
    i = 0
    with open(filename, encoding="utf-8") as f:
        for i, _ in enumerate(f):
            pass
    return i + 1


def glue_files_sorted(files, destination_file):
    file_sizes = []
    for file in files:
        file_sizes.append((file, num_lines_in_file(file)))

    file_sizes.sort(key=itemgetter(1))

    with open(destination_file, "w", encoding="utf-8") as result_file:
        for file, file_size in file_sizes:
            result_file.write(file + "\n")
            result_file.write(str(file_size) + "\n")
            with open(file, encoding="utf-8") as source_file:
                line = source_file.readline()
                while line != "":
                    result_file.write(line)
                    line = source_file.readline()
                result_file.write("\n")


file_names = ["1.txt", "2.txt", "3.txt"]

glue_files_sorted(file_names, "result.txt")

