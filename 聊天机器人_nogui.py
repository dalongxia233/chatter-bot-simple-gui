#coding=utf-8
from chatterbot import ChatBot

chatbot = ChatBot('cshrimp')

print('开始和bot聊天吧！')

while True:
    print(chatbot.get_response(str(input('>'))))
