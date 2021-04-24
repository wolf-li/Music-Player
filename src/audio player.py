# 脚本名称： 音频播放器
# 时间： 2021、4、20
# 参考内容来源链接 https://www.youtube.com/watch?v=uziilzjhf_g

# 需要用的模块
# pygame 需要下载，pip install pygame
# pygame 文档链接：https://www.pygame.org/docs/ref/mixer.html
#                https://www.pygame.org/docs/ref/key.html
# tkinter 为python标准接口，具体文档阅读，https://docs.python.org/zh-cn/3.7/library/tkinter.html
import tkinter as tkr
import pygame
import os


# 创建窗口
player = tkr.Tk()
player.title("音乐播放器")


# 窗口设置
# 设置名称
player.title("音乐播放器")
# 设置窗口大小
player.geometry("300x445")
player.resizable(0,0)

# 播放音乐的路径，默认实在本脚本文件夹下搜索，可以使用相对路径或绝对路径获取。
filename = "1.mp3"

# 音乐播放列表，路径要将 \ 换成 /
os.chdir("C:/Users/Public/Music")
songlist = os.listdir()

pygame.init()
pygame.mixer.init()
v=tkr.StringVar()

# 创建事件函数
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

# 暂停和播放没有联动
def Stop():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

def Pause():
    pygame.mixer.music.pause()
    pygame.mixer.music.unload()

def Volume(numb):
    n = int(numb)
    pygame.mixer.music.set_volume(n/100)

# 注册按钮
var=tkr.StringVar()
label1 = tkr.Label(player,textvariable = var ,height=2)
# label1.pack(fill="x")
button1 = tkr.Button(player, height =2, text = "播放", command = Play)
# button1.pack(side = 'left',  expand='no')
button2 = tkr.Button(player, height = 2, text = "结束", command = Stop)

button3 = tkr.Button(player, height = 2, text ="暂停", command = Pause)

label2 = tkr.Label(player,text=" 音量 ",width= 10,height=2)

scale1 = tkr.Scale(player, from_=0,to=100,variable=v,length=75,command=Volume,orient = 'horizontal')

playlist = tkr.Listbox(player, highlightcolor="blue", selectmode=tkr.SINGLE)
for item in songlist:
    pos = 0
    playlist.insert(pos,item)
    pos += 1

# 对界面进行布局 tkinter 有三种布局方式 pack、grid、place 不能混用
label1.grid(columnspan=4)
button1.grid(row=1,column =0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
label2.grid(row=1,column=3)
scale1.grid(row=1,column=4)
playlist.grid(columnspan=5,pady=10,ipadx=50,ipady=40)



# 开启程序
player.mainloop()

