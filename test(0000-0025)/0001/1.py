# -*- coding: utf-8 -*-
'''
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
import uuid  # 通过uuid生成唯一密钥


def gen(num):  # 生成指定数量密钥
    code = []
    for i in range(0, num):
        code.append(str(uuid.uuid1()))
        # uuid1()——基于时间戳，uuid2()——基于分布式计算环境DCE（Python中没有这个函数），
        # uuid3()——基于名字的MD5散列值，uuid4()——基于随机数，uuid5()——基于名字的SHA-1散列值
        # 首先，Python中没有基于DCE的，所以uuid2可以忽略；
        # 其次，uuid4存在概率性重复，由无映射性，最好不用；
        # 再次，若在Global的分布式计算环境下，最好用uuid1；
        # 最后，若有名字的唯一性要求，最好用uuid3或uuid5。
    return code


def code_save(code):  # 将密钥进行存储
    with open('code.txt',
              'w') as code_file:  # 为方便文件中只有200个密钥，使用w方式进行更新，a+de话会多余20
        # 使用coderunner运行有问题，文件会产生与test文件夹下，而不是/test/test()/0001下，需要在cmd窗口运行即可
        # 可能是因为codderrunner命令实在test目录下调用python，同时使用绝对路径运行.py，导致虽然可以运行.py但是产生
        # 文件和命令中相对路径均为调用python命令时的路径，即test，而非.py所在路径
        for cod in code:
            code_file.write(cod + '\n')


def gen_all(num):
    code = gen(num)
    code_save(code)


if __name__ == '__main__':
    gen_all(200)
