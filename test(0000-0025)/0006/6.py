from nltk.corpus import stopwords  # stopwords 是一个列表，包含了英文中那些频繁出现的词，如am, is
'''
第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，
为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''

# 代码只完成了单个txt提取，同时时根据例题4统计之后的词频进行提取。
# 默认去除常用词后词频越高越重要。多个txt使用题目5中多文件加载进行操作即可，未写

stoplist = stopwords.words('english')
# print(stoplist)
# text = "this is just a test"
# cleanwordlist = [word for word in text.lower().split() 
# if word not in stoplist]
with open('../0004/results.txt', 'r') as file:
    content = file.readlines()
    print(len(content))
    for each in content:
        if each.split(',')[0] in stoplist:
            content.remove(each)
    print(len(content))
    for each in range(5):
        print(content[each].split(',')[0])
