# -*- coding: utf-8 -*-
#標準ライブラリのimport
from datetime import datetime
from pickle import dump, load

#GUIライブラリをimport
from tkinter import *
import tkinter.messagebox

#データ用のクラスをimport
from todoitem import ToDoItem
from todocontainer import ToDoContainer

#データ保存用ファイル名
DUMPFILE = 'todo.dat'

class ToDoApp(Frame):
    """
    ToDo GUIアプリ用のクラス
    """
    def __init__(self, master=None):
        """
            初期化メソッド - ウィジェットやToDoのデータを初期化
            """
        Frame.__init__(self, master, padx=8, pady=4)
        self.pack()
        self.createwidgets()        # ウィジェットを作る
        t = self.winfo_toplevel()
        t.resizable(False, False)   # Windowをサイズ変更できなくする
        self.load()                 # データをロードする
        sec = datetime.now().second # タイマーを設定
        self.after((60-sec)*1000, self.refreshitems)
        self.sel_index = -1

    def createwidgets(self):
        """
        ボタンとかのウィンドウ部分を作る
        :return:
        """
        #スクロールバー付きリストボックス
        self.frame1 = Frame(self)
        frame = self.frame1

        self.listbox = Listbox(frame,height=10,width=30,selectmode=SINGLE,takefocus=1)
        self.yscroll = Scrollbar(frame, orient=VERTICAL)

        #配置を決める
        self.listbox.grid(row=0,column=0,sticky=NS)
        self.yscroll.grid(row=0,colmn=1,sticky=NS)

        #動きとコードを繋げる
        self.yscroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.yscroll.set)
        self.listbox.bind("<ButtonRelease-1>", self.selectitem)

        self.frame1.grid(row=0,column=0)

    def setlistitems(self):
        """
        ToDoのうち未消化分をリストに表示
        :return:
        """
        self.listbox.delete(0,END)
        for todo in self.todos.get_remaining_todos():
            d = todo.duedate
            t = todo.title.ljust(20)
            if todo.duedate < datetime.now():
                t='*'+t                         #起源を過ぎると項目に「*」が表示される
            item = "{}{:4}/{:02}/{:02}{:02}:{:02}".format(
                t, d.year, d.mouth, d.day, d.hour, d.minute
            )
        self.listbox.insert(END, item)

    def refrectententries(self,todo):
        """
        フィールドに入力された文字列をToDoItemインスタンスに反映
        :param todo:
        :return:
        """
        todo.title=self.title_e.get()
        todo.description=self.description_e.get()
        dt =datetime.strptime(self.duedate_e.get()+':00','%Y/%m/%d %H:%M:%S')
        todo.duedate=dt
        if self.finished_v.get()!=0:
            todo.finish()

    def createitem(self):
        """
        新しいToDoアイテムを作る
        :return:
        """
        todo=ToDoItem('','',datetime.now())
        self.refrectententries(todo)
        self.todos += todo
        self.clearentries()
        self.setlistitems()
        self.sel_index = -1
        self.save()

    def refreshitems(self):
        """
        タイマーで定期的に呼び出されるメソッド
        ToDoのうち時間になったものがあればダイアログで知らせる
        :return:
        """
        dirty = False
        for todo in self.todos.get_remaining_todos():
            td=datetime.now()
            d=todo.duedate
            if (d.year == td.year ==td.year and d.mouth == td.mouth and d.day ==td.day and d.hour ==td.hour and d.minute == td.minute):
                msg="{}の時間です\n{}".format(todo.title,todo,description, todo.duedate.strftime('%Y/%m%d %H:%M'))
                tkinter.messagebox.showwarning("時間です",msg)
                dirty = True
                sec = datetime.now().second
                self.after((60-sec)*1000,self.refreshitems)

                if dirty:
                    self.setlistitems()

    def load(self):
        """
        ToDoのデータをファイルから読み込む
        :return:
        """
        try:
            f=open(DUMPFILE,'rb')
            self.todos=load(f)
        except IOErrer:
            self.todos=ToDoContainer()

    def save(self):
        """
        ToDoのデータをファイルに書き出す
        :return:
        """
        f=open(DUMPFILE,'wb')
        dump(self.todos,f)
