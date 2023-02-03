#coding=gbk
from time import time
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
#################################
#        ����Chatterbot         #
#################################
chatbot = ChatBot('cshrimp')
trainer = ListTrainer(chatbot)
#################################
#   ͨ�������Դ����Ͽ�ѵ��ģ��    #
#################################
trainer1 = ChatterBotCorpusTrainer(chatbot)
trainer1.train("chatterbot.corpus.chinese")
trainer1.train("chatterbot.corpus.chinese.greetings")
trainer1.train("chatterbot.corpus.chinese.conversations")
#################################
#   ����С�Ƽ����Ͽ�ѵ��ģ��    #
#################################
#�������Ͽ�
file0 = open(r'model/xiaohuangji-40w/xiaohuangji50w_nofenci.conv',encoding='utf-8')
print('��ʼ����С�Ƽ����Ͽ�')
#���ز��������Ͽ�
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
print('С�Ƽ����Ͽ������ɣ���ʼѵ��ģ��')
#��ʼѵ��ģ��
trainer.train(corpus0)
print('���ģ��ѵ��')
time.sleep(1)
print('������ʼѵ����һ��ģ��')
#################################
#     �����������Ͽ�ѵ��ģ��    #
#################################
#�������Ͽ�
file1 = open(r'model/qingyun-11w/12��Ի��������ƿ�.csv',encoding='utf-8')
print('��ʼ�����������Ͽ�')
#���ز��������Ͽ�
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
print('�������Ͽ������ɣ���ʼѵ��ģ��')
#��ʼѵ��ģ��
trainer.train(corpus1)
print('���ģ��ѵ��')
time.sleep(1)
print('������ʼѵ����һ��ģ��')
#################################
#  ����subtitle���Ͽ�ѵ��ģ��   #
#################################
#�������Ͽ�
file2 = open(r'model/subtitle-useless/dgk_shooter_min.conv',encoding='utf-8')
print('��ʼ����subtitle���Ͽ�')
#���ز��������Ͽ�
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
print('subtitle���Ͽ������ɣ���ʼѵ��ģ��')
#��ʼѵ��ģ��
trainer.train(corpus2)
print('���ģ��ѵ��')
time.sleep(1)
print('������ʼѵ����һ��ģ��')