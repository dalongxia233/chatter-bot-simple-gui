#coding=gbk

# ����chatterbot
from chatterbot import ChatBot

# ����wxgui��
import wx

# ����bot
chatbot = ChatBot('cshrimp')

# ������ʷ��Ϣ��¼�б�
history = []

# һ�����з���
symbol="\n"

# �½�һ����
class newframe(wx.Frame):
    
    # ��ʼ��
    def __init__(self, parent, title):

        # һЩ���ڵ���Ϣ
        super(newframe,self).__init__(parent, title=title,size=(960, 540))

        # ������С
        self.SetMinSize((960,540))
        self.SetMaxSize((960,540))

        # �������
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX)
        
        # �½�panel
        panel = wx.Panel(self)

        # �û������
        self.user_input = wx.TextCtrl(panel,pos=(0,450),size=(800,50),style=wx.TE_PROCESS_ENTER)
        # �󶨻س�����
        self.Bind(wx.EVT_TEXT_ENTER,self.send,self.user_input)

        # ai�ش������
        self.ai_response_out = wx.TextCtrl(panel,-1,pos=(0,0),size=(800,450),style=wx.TE_MULTILINE|wx.TE_READONLY)

        # ���Ͱ�ť
        self.send_button = wx.Button(panel,-1,u"����",pos=(800,450),size=(160,50))
        # ���¼�
        self.Bind(wx.EVT_BUTTON,self.send,self.send_button)

        # ���岻����ai״̬
        self.ai_now = wx.StaticText(panel,-1,u"ai��������",pos=(800,50))

        # �˳���ť
        self.button = wx.Button(panel,-1,u"�˳�",pos=(800,0),size = (160,50))
        # ���˳��¼�
        self.Bind(wx.EVT_BUTTON,self.exit,self.button)

        # ��ʾ����
        self.Show(True)

    def exit(self,event):
        # �ر�
        self.Close(True)

    def send(self,event):
        
        # �����������ݵ��б�
        history.append("��:" + str(self.user_input.GetValue()))
        
        # ����tmp������
        tmp = str(self.user_input.GetValue())
        
        # ��������
        self.user_input.Clear()
        
        # ��ʾ�û���������
        self.ai_response_out.SetValue(symbol.join(history))
        
        # ����ָʾ��
        self.ai_now.SetLabel("ai����˼��ing")
        
        # ����ai�ش����ݵ��б�
        history.append("ai:" + str(chatbot.get_response(tmp)))
        
        # ��ʾai�ش�����
        self.ai_response_out.SetValue(symbol.join(history))
        
        # �ָ�ָʾ��
        self.ai_now.SetLabel("ai��������")

def main():

    # �½�app
    app = wx.App()

    # �½����崫�����
    newframe(None,"����BOT")

    # ��ʾ����
    app.MainLoop()

if __name__ == '__main__':

    # ��ʼִ��
    main()






