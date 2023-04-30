''' ############### けふも、けふとて、京都で。 2022/11/22 #####################
【作品名】けふも、けふとて、京都で。
【概要・目的】
郵便番号を入力して京都府の地名を表示する検索アプリです。
検索したい郵便番号を数字ボタンから入力しPUSHボタンを押すと画面上部に該当する京都府の地名が登場します。
京都府以外の郵便番号は表示されませんが、"京都人"以外は嫌味を言われたり強制終了させられたりするお遊びができます。
レイアウトや色合いをおしゃれにして、見ているだけで心が弾むような"京都人"のために作りました。

【アピールポイント】
1. テキストボックスを郵便番号7桁がちょうど収まるサイズにして、郵便番号の数が足りているか一目で把握できるようになっています。
2. 数字ボタン、リセットボタン、終了ボタンを作り、キーボード入力以外の方法を作りました。
3. 京都をコンセプトに作っているため、京都府伝統色の紫と古都を彷彿とさせる深みのある赤を基調としました。
4. アプリ名は語呂を重視し「けふも、けふとて、京都で。」と口に出すと趣を感じられる言葉遊びを取り入れました。
5. 京都府以外の郵便番号を入力すると嫌味を言われて強制終了することで、エラーやバグを出さないように工夫しました。
6. 「京都市に住んでいるのが真の京都人だ」という言説があるため京都市以外の京都府民にも嫌味を言って、コンセプトを大事にしました。
############################################################################'''

#-----------メソッド定義1 テキストボックスから京都府の市区町村を表示---------------
def search():
    mail_num = int(txtbox.get())
    df = pd.read_csv("data_file/Kyo_mo_Kyoto_de.CSV", header=None, encoding="shift_jis") ## データフレームを読み込む
    results = df[df[2] == mail_num] ##「2」の列から住所を抽出して表示
    
    ## datafameの値（values）の各列を文字列(astype(str))してリスト化(tolist())
    lists = results[[2,6,7,8]].values.astype(str).tolist()
    ## 各行を結合する（join）この際、各列が同じデータ型である必要あり（そのための astype(str)）
    lists = [" ".join(x) for x in lists]
    address = "\n".join([x for x in lists]) ## 結果が縦に表示されるように改行コード（\n）でjoin
    
    ## 京都人かどうか判定
    if "京都市" in address:
        explanation_lbl.configure(text="\n\n" + address)
    elif "京都府" in address:
        messagebox.showinfo("京都人を気取らんといて。", "このあたりでは見いひん顔やね。") ## ここで京都市民以外の京都府民に嫌味を言って結果表示。
        explanation_lbl.configure(text="\n\n" + address)
    else:
        messagebox.showerror("おかえりください。", "ぶぶづけでもどうどすか？") ## ここで他都道府県民や存在しない郵便番号を入力した人に嫌味を言って強制終了。
        root.destroy()

#-----------メソッド定義2 自作数字キーボードからテキストボックスへ入力--------------
def num_input(num):
    txtbox.insert(tk.END, num) ## 後ろに数字(or文字)をつけ足していく
#-------メソッド定義3 自作数字キーボードからテキストボックスの内容を削除・初期化------
def num_delete():
    txtbox.delete(0, tk.END)
    explanation_lbl.configure(text="\n\n郵便番号を入力しボタンを押してください。【ハイフンなし】", font=("MSゴシック", "10"), bg="Lavender", fg="black")
#--------------------------メソッド定義3 確認して終了-----------------------------
def destroy():
    check = messagebox.askyesnocancel("確認","このまま終了しますか。")
    if check == True:
        messagebox.showinfo("またお会いましょう。", "おおきに。さいなら。")
        root.destroy()
#-------------------------------------------------------------------------------

import tkinter as tk
import pandas as pd
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x550")
root.configure(bg="Lavender")
root.title("けふも、けふとて、京都で。【2023ver.】")

title_lbl = tk.Label(text="けふも、けふとて、京都で。", font=("MSゴシック", "20", "bold"), relief=tk.RIDGE, width=30, fg="white", bg="#B1063A") ## タイトル定義
explanation_lbl = tk.Label(text="\n\n郵便番号を入力しボタンを押してください。【ハイフンなし】", font=("MSゴシック", "10"), bg="Lavender", fg="black") ## ↓↓↓ラベル定義↓↓↓
alart_lbl = tk.Label(text="⚠データが更新されていない場合、正しく表示されないことがあります⚠", font=("MSゴシック", "8", "bold"), bg="Lavender", fg="#B1063A")
credit_lbl = tk.Label(text="Produced by A.M.", bg="Lavender", fg="black")
txtbox = tk.Entry(width=7, relief=tk.FLAT) ## テキストボックス定義
push_btn = tk.Button(text="PUSH", font=("MSゴシック", "12", "bold"), relief=tk.RIDGE, bg="#B1063A", fg="white", width=10, height=1, command = lambda:search()) ## PUSHボタン定義
reset_btn = tk.Button(text="RESET", font=("4"), relief=tk.RIDGE, bg="white", fg="black", width=10, height=1, command = lambda:num_delete()) ## RESETボタン定義
end_btn = tk.Button(text="END", font=("4"), relief=tk.RIDGE, bg="white", fg="black", width=10, height=1, command = lambda:destroy()) ## ENDボタン定義

btn1 = tk.Button(text="1", font=("4"), relief=tk.RIDGE, bg="white", fg="#B1063A", width=10, height=1, command = lambda:num_input(1)) ## ↓↓↓数字ボタン定義↓↓↓
btn2 = tk.Button(text="2", font=("4"), relief=tk.RIDGE, bg="white", fg="#B1063A",  width=10, height=1, command = lambda:num_input(2))
btn3 = tk.Button(text="3", font=("4"), relief=tk.RIDGE, bg="white", fg="#B1063A", width=10, height=1, command = lambda:num_input(3))
btn4 = tk.Button(text="4", font=("4"), relief=tk.RIDGE, bg="white", fg="#B1063A", width=10, height=1, command = lambda:num_input(4))
btn5 = tk.Button(text="5", font=("4"), relief=tk.RIDGE, bg="white", fg="#B1063A", width=10, height=1, command = lambda:num_input(5))
btn6 = tk.Button(text="6", font=("4"), relief=tk.RIDGE, bg="white", fg="#B1063A", width=10, height=1, command = lambda:num_input(6))
btn7 = tk.Button(text="7", font=("4"), relief=tk.RIDGE, bg="white", fg="#B1063A", width=10, height=1, command = lambda:num_input(7))
btn8 = tk.Button(text="8", font=("4"), relief=tk.RIDGE, bg="white", fg="#B1063A", width=10, height=1, command = lambda:num_input(8))
btn9 = tk.Button(text="9", font=("4"), relief=tk.RIDGE, bg="white", fg="#B1063A", width=10, height=1, command = lambda:num_input(9))
btn0 = tk.Button(text="0", font=("4"), relief=tk.RIDGE, bg="white", fg="#B1063A", width=10, height=1, command = lambda:num_input(0))

title_lbl.pack() ## タイトル表示
explanation_lbl.pack() ## ラベル表示(入力、検索結果)
push_btn.place(x=200, y=150) ## ボタン表示(PUSH)
txtbox.place(x=230, y=100) ## テキストボックス表示
btn1.place(x=80, y=200) ## ↓↓↓数字ボタン表示
btn2.place(x=200, y=200)
btn3.place(x=320, y=200)
btn4.place(x=80, y=250)
btn5.place(x=200, y=250)
btn6.place(x=320, y=250)
btn7.place(x=80, y=300)
btn8.place(x=200, y=300)
btn9.place(x=320, y=300)
btn0.place(x=200, y=350)
reset_btn.place(x=80, y=350) ## ボタン表示(RESET)
end_btn.place(x=320, y=350) ## ボタン表示(END)
alart_lbl.place(x=30, y=420) ## ラベル表示(注意喚起)
credit_lbl.place(x=200, y=500) ## ラベル表示(制作者クレジット)
tk.mainloop() ## ウィンドウ表示
