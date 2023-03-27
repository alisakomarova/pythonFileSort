
files = ['1.txt', '2.txt', '3.txt']


def line_count(file):
    res = sum(1 for line in open(file, encoding='utf-8'))
    return res

files_sorted = sorted(files, key=line_count)

f_sum = open("summarized.txt", "w", encoding='utf-8')

for file in files_sorted:
    f_sum.write(file)
    f_sum.write('\n')
    f_sum.write(str(line_count(file)))
    f_sum.write('\n')
    file_opened = open(file, 'r', encoding='utf-8')
    if int(line_count(file)) == 1:
    # иначе не удавалось убрать пустую строгу после строки "Тревога началась.."
        line = file_opened.readline()
        f_sum.write(line)
    else:
        for i in range(0, int(line_count(file))):
            line = file_opened.readline()
            f_sum.write(line)
        f_sum.write('\n')
    file_opened.close()

f_sum.close()

with open('summarized.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)
