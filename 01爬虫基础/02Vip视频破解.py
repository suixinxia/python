import tkinter.messagebox as msgbox
import tkinter as tk
import webbrowser
import re


class APP:
    def __init__(self, width=500, height=300):  # 适当增大窗口宽度以容纳新按钮
        self.w = width
        self.h = height
        self.title = ' 视频爬取助手'
        self.root = tk.Tk(className=self.title)
        # 定义button控件上的文字
        self.url = tk.StringVar()
        # 定义选择哪个播放源
        self.v = tk.IntVar()
        # 默认为1
        self.v.set(1)
        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)
        frame_4 = tk.Frame(self.root)  # 新增框架放置网站跳转按钮
        # Menu菜单
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        moviemenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='友情链接', menu=moviemenu)
        # 各个网站链接（保持原菜单功能）
        moviemenu.add_command(label='腾讯视频', command=lambda: webbrowser.open('http://v.qq.com/'))
        moviemenu.add_command(label='搜狐视频', command=lambda: webbrowser.open('http://tv.sohu.com/'))
        moviemenu.add_command(label='芒果TV', command=lambda: webbrowser.open('http://www.mgtv.com/'))
        moviemenu.add_command(label='爱奇艺', command=lambda: webbrowser.open('http://www.iqiyi.com/'))
        moviemenu.add_command(label='PPTV', command=lambda: webbrowser.open('http://www.bilibili.com/'))
        moviemenu.add_command(label='优酷', command=lambda: webbrowser.open('http://www.youku.com/'))
        moviemenu.add_command(label='乐视', command=lambda: webbrowser.open('http://www.le.com/'))
        moviemenu.add_command(label='土豆', command=lambda: webbrowser.open('http://www.tudou.com/'))
        moviemenu.add_command(label='A站', command=lambda: webbrowser.open('http://www.acfun.tv/'))
        moviemenu.add_command(label='B站', command=lambda: webbrowser.open('http://www.bilibili.com/'))

        # 控件内容设置
        group = tk.Label(frame_1, text='请选择一个视频播放通道：', padx=10, pady=10)
        tb1 = tk.Radiobutton(frame_1, text='通道一', variable=self.v, value=1, width=5, height=3)
        tb2 = tk.Radiobutton(frame_1, text='通道二', variable=self.v, value=2, width=5, height=3)
        tb3 = tk.Radiobutton(frame_1, text='通道三', variable=self.v, value=3, width=5, height=3)
        tb4 = tk.Radiobutton(frame_1, text='通道四', variable=self.v, value=4, width=5, height=3)
        tb5 = tk.Radiobutton(frame_1, text='通道五', variable=self.v, value=5, width=5, height=3)

        self.site_buttons = [
            tk.Button(frame_4, text="爱奇艺", font=('楷体', 10), fg='green', width=10,
                    command=lambda: webbrowser.open("https://www.iqiyi.com/")),
            tk.Button(frame_4, text="优酷", font=('楷体', 10), fg='blue', width=10,
                    command=lambda: webbrowser.open("https://www.youku.com/ku/weblive")),
            tk.Button(frame_4, text="腾讯视频", font=('楷体', 10), fg='red', width=10,
                    command=lambda: webbrowser.open("https://v.qq.com/")),
            tk.Button(frame_4, text="哔哩哔哩", font=('楷体', 10), fg='pink', width=10,
                    command=lambda: webbrowser.open("https://www.bilibili.com/")),
            tk.Button(frame_4, text="芒果TV", font=('楷体', 10), fg='orange', width=10,
                    command=lambda: webbrowser.open("https://www.mgtv.com/show/?hk=p69ci"))
        ]

        label1 = tk.Label(frame_2, text="请输入视频链接：")
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        label2 = tk.Label(frame_2, text=" ")
        play = tk.Button(frame_2, text="播放", font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)
        label3 = tk.Label(frame_2, text=" ")
        label_explain = tk.Label(frame_3, fg='green', font=('楷体', 16), text='\n注意：支持大部分主流视频网站的视频播放！\n此软件仅用于交流学习，请勿用于任何商业用途！')
        label_warning = tk.Label(frame_3, fg='blue', font=('楷体', 20), text='\n作者：天新\n')

        # 控件布局
        frame_1.pack()
        frame_4.pack(pady=10)  # 放置网站按钮框架
        frame_2.pack()
        frame_3.pack()

        group.grid(row=0, column=0)
        tb1.grid(row=0, column=1)
        tb2.grid(row=0, column=2)
        tb3.grid(row=0, column=3)
        tb4.grid(row=0, column=4)
        tb5.grid(row=0, column=5)

        # 布局五个网站按钮（横向排列）
        for btn in self.site_buttons:
            btn.pack(side=tk.LEFT, padx=5)

        label1.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        play.grid(row=0, column=3, ipadx=10, ipady=10)
        label3.grid(row=0, column=4)
        label_explain.grid(row=1, column=0)
        label_warning.grid(row=2, column=0)

    """
    函数说明:视频播放
    """
    def video_play(self):
        # 视频解析网站地址
        port_1 = 'https://jx.xyflv.cc/?url='
        port_2 = 'https://jx.m3u8.tv/jiexi/?url='
        port_3 = 'https://yparse.ik9.cc/index.php?url='
        port_4 = 'https://jx.nnxv.cn/tv.php?url='
        port_5 = 'https://jx.playerjy.com/?url='

        # 正则表达是判定是否为合法链接
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            if self.v.get() == 1:
                webbrowser.open(port_1 + self.url.get())
            elif self.v.get() == 2:
                webbrowser.open(port_2 + self.url.get())
            elif self.v.get() == 3:
                webbrowser.open(port_3 + self.url.get())
            elif self.v.get() == 4:
                webbrowser.open(port_4 + self.url.get())
            elif self.v.get() == 5:
                webbrowser.open(port_5 + self.url.get())
        else:
            msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')

    """
    函数说明:tkinter窗口居中
    """
    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws / 2) - (self.w / 2))
        y = int((hs / 2) - (self.h / 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    """
    函数说明:loop等待用户事件
    """
    def loop(self):
        # 禁止修改窗口大小
        self.root.resizable(False, False)
        # 窗口居中
        self.center()
        self.root.mainloop()


if __name__ == '__main__':
    app = APP()			# 实例化APP对象
    app.loop()			# loop等待用户事件