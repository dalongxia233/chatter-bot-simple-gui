#coding=gbk
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer

chatbot = ChatBot('cshrimp')
trainer = ListTrainer(chatbot)


#����
file0 = open(r'./train.txt',encoding="utf-8")
print('��ʼ���������¼')

corpus0 = []
while 1:
    try:
        line = file0.readline()
        if not line:
            break
        
        if line.startswith('202') == True :
            continue
        if line.startswith('[ͼƬ]') == True:
            continue
        if line == "\n":
            continue
        if line.find("@") != -1:
            continue
        if line.find("������һ") != -1:
            continue

        corpus0.append(line.strip('\n'))

    except:
        pass

file0.close()


print('������ɣ���ʼѵ��ģ��')
#��ʼѵ��ģ��
trainer.train(corpus0)
print('���ģ��ѵ��')