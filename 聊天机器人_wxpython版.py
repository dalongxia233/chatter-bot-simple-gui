#coding=gbk

# 导入chatterbot
from chatterbot import ChatBot

# 导入wxgui库
import wx

# 创建bot
chatbot = ChatBot('cshrimp')

# 创建历史消息记录列表
history = []

# 一个换行符（
symbol="\n"

# 新建一个类
class newframe(wx.Frame):
    
    # 初始化
    def __init__(self, parent, title):

        # 一些窗口的信息
        super(newframe,self).__init__(parent, title=title,size=(960, 540))

        # 锁定大小
        self.SetMinSize((960,540))
        self.SetMaxSize((960,540))

        # 禁用最大化
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX)
        
        # 新建panel
        panel = wx.Panel(self)

        # 用户输入框
        self.user_input = wx.TextCtrl(panel,pos=(0,450),size=(800,50),style=wx.TE_PROCESS_ENTER)
        # 绑定回车发送
        self.Bind(wx.EVT_TEXT_ENTER,self.send,self.user_input)

        # ai回答输出框
        self.ai_response_out = wx.TextCtrl(panel,-1,pos=(0,0),size=(800,450),style=wx.TE_MULTILINE|wx.TE_READONLY)

        # 发送按钮
        self.send_button = wx.Button(panel,-1,u"发送",pos=(800,450),size=(160,50))
        # 绑定事件
        self.Bind(wx.EVT_BUTTON,self.send,self.send_button)

        # 意义不明的ai状态
        self.ai_now = wx.StaticText(panel,-1,u"ai正在摸鱼",pos=(800,50))

        # 退出按钮
        self.button = wx.Button(panel,-1,u"退出",pos=(800,0),size = (160,50))
        # 绑定退出事件
        self.Bind(wx.EVT_BUTTON,self.exit,self.button)

        # 显示窗口
        self.Show(True)

    def exit(self,event):
        # 关闭
        self.Close(True)

    def send(self,event):
        
        # 新增输入内容到列表
        history.append("您:" + str(self.user_input.GetValue()))
        
        # 丢到tmp函数内
        tmp = str(self.user_input.GetValue())
        
        # 清空输入框
        self.user_input.Clear()
        
        # 显示用户输入内容
        self.ai_response_out.SetValue(symbol.join(history))
        
        # 更新指示器
        self.ai_now.SetLabel("ai正在思考ing")
        
        # 新增ai回答内容到列表
        history.append("ai:" + str(chatbot.get_response(tmp)))
        
        # 显示ai回答内容
        self.ai_response_out.SetValue(symbol.join(history))
        
        # 恢复指示器
        self.ai_now.SetLabel("ai正在摸鱼")

def main():

    # 新建app
    app = wx.App()

    # 新建窗体传入标题
    newframe(None,"聊天BOT")

    # 显示窗体
    app.MainLoop()

if __name__ == '__main__':

    # 开始执行
    main()






