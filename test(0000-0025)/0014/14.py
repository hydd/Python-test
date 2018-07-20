import openpyxl  # 适用于xlsx文件
'''
纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中
'''


def read_file():
    words = []
    with open('14.txt', 'r') as file:
        content = file.readlines()
        content.pop(0)
        content.pop(-1)
        for word in content:  # 去除杂项
            word = word.replace('\t', '')
            word = word.replace(',\n', '')
            word = word.replace('\n', '')
            word = word.replace('"', '')
            word = word.replace(':', ',')
            word = word.replace('[', '')
            word = word.replace(']', '')

            # print(word)
            words.append(word)

        # print(content)
    # print(words)
    return words


def new_list(list):  # 生成代谢入二维列表
    new_list = []
    for each in list:
        each = each.split(',')
        # print(each)
        new_list.append(each)
    print(new_list)
    return new_list


def write_list(list):  # 写入excel文件
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'test'
    value = list
    for i in range(0, len(value)):
        for j in range(0, len(value[i])):
            sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))
    wb.save('student.xlsx')
    print("写入数据成功！")


if __name__ == '__main__':
    # read_file()
    write_list(new_list(read_file()))
