from tkinter import *
import random
root=Tk()
root.geometry('400x200')
root.title('猜数字游戏')
def Label_range():
    L2['text']='目前范围是[%d,%d]'%(x,y)
def Label_change():
    L1['text']='请输入数字100-999'
def Change_num():
    global num
    global x
    global y
    global summ
    num=random.randint(100,999)
    x=100
    y=999
    summ=0
def Close_game(event):
    root.destroy()
def Restart_game(event):
    Change_num()
    Label_change()
    Label_range()
    Entry_num.delete(0,END)
def Compare_num(event):
    global num
    global x
    global y
    global summ
    summ+=1
    if(num==int(Entry_num.get())):
        L1['text']='恭喜你答对了'
        L2['text']='一共用了%d次'%summ
    elif(num<int(Entry_num.get())):
        L1['text']='再小点'
        if(int(Entry_num.get())<y):
            y=int(Entry_num.get())
        Label_range()
    else:
        L1['text']='再大点'
        if(int(Entry_num.get())>x):
            x=int(Entry_num.get())
        Label_range()
Change_num()
L1=Label(root,text='请输入数字100-999')
L2=Label(root,text='目前范围是[%d,%d]'%(x,y))
L1.pack()
L2.pack()

fram1=Frame(root)
Entry_num=Entry(fram1,width=20)
butt1=Button(fram1,text='确定')
Entry_num.pack(side='left')
butt1.bind('<Button-1>',Compare_num)
Entry_num.bind('<Return>',Compare_num)
butt1.pack()
fram1.pack()

fram2=Frame(root)
butt2=Button(fram2,text='关闭')
butt3=Button(fram2,text='重新开始')
butt2.pack(side='left')
butt2.bind('<Button-1>',Close_game)
butt3.bind('<Button-1>',Restart_game)
butt3.pack()
fram2.pack()


root.mainloop()
