#coding=gbk
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer

chatbot = ChatBot('cshrimp')
trainer = ListTrainer(chatbot)


#加载
file0 = open(r'./train.txt',encoding="utf-8")
print('开始加载聊天记录')

corpus0 = []
while 1:
    try:
        line = file0.readline()
        if not line:
            break
        
        if line.startswith('202') == True :
            continue
        if line.startswith('[图片]') == True:
            continue
        if line == "\n":
            continue
        if line.find("@") != -1:
            continue
        if line.find("撤回了一") != -1:
            continue

        corpus0.append(line.strip('\n'))

    except:
        pass

file0.close()


print('加载完成，开始训练模型')
#开始训练模型
trainer.train(corpus0)
print('完成模型训练')