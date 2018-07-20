'''
第 0011 题： 敏感词文本文件 filtered_words.txt，
里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
'''


def read_file():
    words = []
    with open('filtered_words.txt', 'r') as file:
        # words = file.readlines()
        for word in file.readlines():
            word = word.replace('\n', '')
            # word = str.replace(word, '\n', '')
            words.append(word)
            # print(word)
        # print(words)
        # print(len(words))
    return words


def de_word(words):
    flag = False
    new_word = input('请输入内容:')
    # print(new_word)
    for word in words:
        if word in new_word:
            flag = True
            break
        else:
            continue
    if flag:
        print('Freedom')
    else:
        print('Human Rights')


if __name__ == '__main__':
    # read_file()
    de_word(read_file())