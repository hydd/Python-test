import glob
'''
第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''

kong_num = 0
zhu_num = 0
val_num = 0


def cont_code(url):
    print('cont_code has called')
    for each in url:
        # print(each)
        with open(each, encoding='utf-8') as file:
            content = file.readlines()
            global kong_num
            global zhu_num
            global val_num
            # print(content)
            for cont in content:
                # print(cont.split())
                if not cont.split(
                ):  # 关于'if not x:' 和 'if x is None:' 和 'if not x is None:'的区别
                    # https://blog.csdn.net/Sasoritattoo/article/details/12451359
                    kong_num += 1
                elif cont.split()[0] == '#':
                    zhu_num += 1
                else:
                    val_num += 1
    print('全部空行数：' + str(kong_num))
    print('全部注释行数：' + str(zhu_num))
    print('全部代码行数：' + str(val_num))


def get_file(url):
    print('get_file has called')
    file = glob.glob(path)
    # print(file)
    return file


if __name__ == '__main__':
    path = '../0003/*.py'
    file = get_file('path')
    cont_code(file)
