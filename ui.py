# -*- coding: utf8 -*-

import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import utility
import converter

in_dir_path = ''
out_dir_path = ''

# イベント処理関数
def select_slide_dir(edit_box):
    global in_dir_path
    edit_box.delete(0, tk.END)
    in_dir_path = filedialog.askdirectory(initialdir=in_dir_path)
    edit_box.insert(tk.END, in_dir_path)


def select_out_slide_dir(edit_box):
    global out_dir_path
    edit_box.delete(0, tk.END)
    out_dir_path = filedialog.askdirectory(initialdir=out_dir_path)
    edit_box.insert(tk.END, out_dir_path)


def convert_clicked(self, slide_title):
    global in_dir_path
    global out_dir_path

    if slide_title is '':
        messagebox.showerror(
            title='タイトル未入力',
            message='スライド名を入力してください'
        )
        return
    self.configure(state=tk.DISABLED)

    in_dir_path = in_dir_path.replace('/','\\')
    out_dir_path = out_dir_path.replace('/','\\')
    converter.convert(in_dir_path, out_dir_path, slide_title)
    self.configure(state=tk.NORMAL)
    

if __name__ == "__main__":

    # GUIの初期処理
    root = tk.Tk()
    root.title('VRCプレゼンスライドコンバーター')
    root.geometry("400x200")

    # ラベル
    label1 = tk.Label(text='スライドが入ったフォルダの選択')
    label1.place(x=5, y=5)

    # パス入力ボックス
    path_edit_box = tk.Entry(width=50)
    path_edit_box.insert(tk.END, utility.get_current_path())
    path_edit_box.place(x=5, y=30)

    in_dir_path = path_edit_box.get()

    # フォルダパス選択ボタン
    select_button = tk.Button(
        text='フォルダを選択', 
        command= lambda : select_slide_dir(path_edit_box)
    )
    select_button.place(x=310, y=25)

    # スライド名入力
    label2 = tk.Label(text='コンバート後のスライド名')
    label2.place(x=5, y=55)

    title_edit_box = tk.Entry(width=20)
    title_edit_box.place(x=5, y=80)

    slide_name = title_edit_box.get()
    
    # 出力パス入力ボックス
    label3 = tk.Label(text='コンバートされたファイルの保存先')
    label3.place(x=5, y=105)
    out_path_edit_box = tk.Entry(width=50)
    out_path_edit_box.insert(tk.END, utility.get_current_path())
    out_path_edit_box.place(x=5, y=130)

    out_dir_path = out_path_edit_box.get()

    # 出力フォルダパス選択ボタン
    out_select_button = tk.Button(
        text='フォルダを選択', 
        command= lambda : select_out_slide_dir(out_path_edit_box)
    )
    out_select_button.place(x=310, y=125)

    # 変換ボタン
    convert_button = tk.Button(
        text='コンバート',
        width=50,
        command= lambda : convert_clicked(convert_button, title_edit_box.get())
    )
    convert_button.place(x=20, y=165)

    root.mainloop()