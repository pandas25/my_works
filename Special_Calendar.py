''' ############### Special Calendar 2024 2022/10/18 #####################
【作品名】Special Calendar 2024
【概要・目的】
月名ボタンを押すと画面上部に月ごとのカレンダーが表示されるカレンダーアプリです。
画面下部1番下の「memo✿」ボタンを押すとメモ帳が別ウィンドウで出てきます。
アプリをPCに起動させたまま、学生や社会人が何か手元のテキストで勉強するというシチュエーションを想定しています。

【アピールポイント】
1. 作業中デスクトップに表示されるのはカレンダーだけ、メモしたいことがあればすぐにメモを取れます。
2. 作業中気が散らないように画面のデザインはシンプルに仕上げ、見やすさ重視で配色とボタンの大きさ等決めました。
3. 全てのカレンダーを一度に表示させるのではなく、月ごとのボタンをそれぞれ用意し必要なカレンダーのみ表示させます。
4. カレンダーを日曜日始まりに設定し、皆さんの持っているカレンダーと合わせました。
5. メモ帳で長文を打つ場合でも文章が画面から途切れないように、折り返し機能を実装しました。
6. アプリに必要な機能の定義だけして、最後にまとめて表示させることでソースコードを見やすくしました。
############################################################################'''

#------------------------------ メソッド定義 カレンダー表示 --------------------------------
def cal(month):
    calendar.setfirstweekday(calendar.SUNDAY) ##日曜日始まりに変更
    explanation_lbl.configure(text=calendar.month(2024,month,w=6, l=2))
#----------------------------- メソッド定義2 メモ帳表示(おまけ機能) --------------------------
def memo():
    root = tk.Tk() #↓↓↓メモ帳ウィンドウ作成↓↓↓
    root.geometry("700x500")
    root.title("Special Tool")
    text_widget = tk.Text(root, wrap=tk.CHAR) ##文章折り返し可
    text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W)) ##テキスト配置
    root.columnconfigure(0, weight=1) ##↓↓↓テキスト部分伸縮↓↓↓
    root.rowconfigure(0, weight=1)
#-----------------------------------------------------------------------------------------

import tkinter as tk
import calendar

root = tk.Tk()
root.geometry("600x950")
root.title("Special Calendar")

title_lbl = tk.Label(text="CALENDAR 2024", font=("MSゴシック", "20", "bold"),width=20,fg="pink") ##タイトルラベル定義
explanation_lbl = tk.Label(text="Click the Button!",font=("3"),fg="gray") ##↓↓↓説明ラベル定義↓↓↓
comment_lbl = tk.Label(text="Have a good day.",fg="blue")
credit_lbl = tk.Label(text="Produced by A.M.",fg="gray")
btn1 = tk.Button(text="January",font=("4"),width=20,height=2, command = lambda:cal(1)) ##↓↓↓月の名前ボタン↓↓↓
btn2 = tk.Button(text="February",font=("4"),width=20,height=2, command = lambda:cal(2))
btn3 = tk.Button(text="March",font=("4"),width=20,height=2, command = lambda:cal(3))
btn4 = tk.Button(text="April",font=("4"),width=20,height=2, command = lambda:cal(4))
btn5 = tk.Button(text="May",font=("4"),width=20,height=2, command = lambda:cal(5))
btn6 = tk.Button(text="June",font=("4"),width=20,height=2, command = lambda:cal(6))
btn7 = tk.Button(text="July",font=("4"),width=20,height=2, command = lambda:cal(7))
btn8 = tk.Button(text="August",font=("4"),width=20,height=2, command = lambda:cal(8))
btn9 = tk.Button(text="September",font=("4"),width=20,height=2, command = lambda:cal(9))
btn10 = tk.Button(text="October",font=("4"),width=20,height=2, command = lambda:cal(10))
btn11 = tk.Button(text="Nobember",font=("4"),width=20,height=2, command = lambda:cal(11))
btn12 = tk.Button(text="December",font=("4"),width=20,height=2, command = lambda:cal(12))
memo_btn = tk.Button(text="memo✿",font=("4"), command = memo) ##メモ帳ボタン

title_lbl.pack() ##タイトル表示
explanation_lbl.pack() ##↓↓↓ラベル表示↓↓↓
comment_lbl.pack()
btn1.pack() ##↓↓↓ボタン表示↓↓↓
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()
btn8.pack()
btn9.pack()
btn10.pack()
btn11.pack()
btn12.pack()
memo_btn.pack()
credit_lbl.pack() ##ラベル表示(制作者クレジット)
tk.mainloop() ##ウィンドウ表示
