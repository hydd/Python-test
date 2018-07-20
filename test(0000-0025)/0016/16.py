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
    with open('16.txt', 'r') as file:
        content = file.read()
        # print(content)
        # print(type(content))

        word = eval(content)
        # print(word)
        # print(word.keys())
        # for each in word.keys():
        #     print(each)
        #     print(word[each])
        # print(word.values())
        # print(type(word))
        # print(word)
        for each in word:
            words.append(each)
    print(words)
    return words


def write_list(list):  # 写入excel文件
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'test'
    value = list
    for i in range(0, len(value)):
        for j in range(0, len(value[i])):
            sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))
    wb.save('numbers.xlsx')
    print("写入数据成功！")


if __name__ == '__main__':
    # read_file()
    write_list(read_file())
