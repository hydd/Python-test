'''
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，
则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
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
    # flag = False
    new_word = input('请输入内容:')
    # print(new_word)
    for word in words:
        if word in new_word:
            new_word = new_word.replace(word, '**')
            # print(new_word)
            # flag = True
            break
        else:
            continue
    print(new_word)
    # if flag:
    #     print('Freedom')
    # else:
    #     print('Human Rights')


if __name__ == '__main__':
    # read_file()
    de_word(read_file())
