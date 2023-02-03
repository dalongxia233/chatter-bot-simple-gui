#coding=gbk
from time import time
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
#################################
#        载入Chatterbot         #
#################################
chatbot = ChatBot('cshrimp')
trainer = ListTrainer(chatbot)
#################################
#   通过加载自带语料库训练模型    #
#################################
trainer1 = ChatterBotCorpusTrainer(chatbot)
trainer1.train("chatterbot.corpus.chinese")
trainer1.train("chatterbot.corpus.chinese.greetings")
trainer1.train("chatterbot.corpus.chinese.conversations")
#################################
#   加载小黄鸡语料库训练模型    #
#################################
#加载语料库
file0 = open(r'model/xiaohuangji-40w/xiaohuangji50w_nofenci.conv',encoding='utf-8')
print('开始加载小黄鸡语料库')
#加载并处理语料库
corpus0 = []
while 1:
    try:
        line = file0.readline()
        if not line:
            break
        if line == 'E\\n':
            continue
        corpus0.append(line.split('M')[1].strip('\n'))
    except:
        pass
file0.close()
print('小黄鸡语料库加载完成，开始训练模型')
#开始训练模型
trainer.train(corpus0)
print('完成模型训练')
time.sleep(1)
print('即将开始训练下一个模型')
#################################
#     加载青云语料库训练模型    #
#################################
#加载语料库
file1 = open(r'model/qingyun-11w/12万对话语料青云库.csv',encoding='utf-8')
print('开始加载青云语料库')
#加载并处理语料库
corpus1 = []
while 1:
    try:
        line = file1.readline()
        if not line:
            break
        corpus1.append(line.split(' | ')[1].strip('\n'))
    except:
        pass
file1.close()
print('青云语料库加载完成，开始训练模型')
#开始训练模型
trainer.train(corpus1)
print('完成模型训练')
time.sleep(1)
print('即将开始训练下一个模型')
#################################
#  加载subtitle语料库训练模型   #
#################################
#加载语料库
file2 = open(r'model/subtitle-useless/dgk_shooter_min.conv',encoding='utf-8')
print('开始加载subtitle语料库')
#加载并处理语料库
corpus2 = []
while 1:
    try:
        line = file2.readline()
        if not line:
            break
        if line == 'E\\n':
            continue
        corpus2.append(line.split('M')[1].strip('\n'))
    except:
        pass
file2.close()
print('subtitle语料库加载完成，开始训练模型')
#开始训练模型
trainer.train(corpus2)
print('完成模型训练')
time.sleep(1)
print('即将开始训练下一个模型')