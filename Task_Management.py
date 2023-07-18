''' ############## Task Management 2023/06/23 #######################
【作品名】Task Management
【概要・目的】
タスクを管理するデスクトップタスク管理アプリ​。
就職課都度におけるエントリーシートや面接の締め切り日・実施日を管理し、忘れないようにすることが目的。

【アピールポイント】
1. テキストファイルをプログラムで書き換え読み込むことによって、必要に応じてタスクを追加できるようにした。
2. 締め切り期限が過ぎたタスクはウインドウやテキストファイルから削除し、未達成のタスクを見やすくした。
3. メモ機能を搭載し、タスクに関連する簡単なメモを残すことを可能にした。
4. タスクやメモをテキストファイルから読み込ませることで、次回アプリ起動時にもデータを持ち越せるようにした。
############################################################################'''

# ------------------ メソッド定義1  タスクリストをタスクタブに表示させる ------------------
def TaskList():
    task_num = 0 ## タスク番号
    now = datetime.datetime.now()
    
    ## 日本語の曜日名
    weekday_names = ["月","火","水","木","金","土","日"]
    weekday_index = now.weekday()
    week_name = weekday_names[weekday_index]
    
    window["todays_date"].update(f"{now:%Y / %m / %d}（ {week_name} ）")
    note = ""
    dl_note = ""
    
    for task in tasks:
        td = now.replace(year=task[1], month=task[2], day=task[3], hour=task[4], minute=task[5], second=0) - now
        tasks.sort (key=itemgetter(1,2,3,4,5)) ## タスクの日付を昇順で並び替え
        
        if td.total_seconds() > 0:
            task_num += 1
            
            ## ↓↓カウントダウン時間(変数td)を加工して配列化する操作↓↓
            pre = []
            pre.append(str(td)) ## tdを文字列化し、pre配列に追加
            deadline = "".join(pre) ## pre配列の中身を連結して、文字列に変換
            
            ## 締め切り期限が１日未満の場合の処理。
            if not "day" in deadline:
                deadline = "0 day," + deadline
            
            ## dayを空の文字列に置き換え
            deadline = deadline.replace("day", "") 
            
            ##  2日以上はdaysのsが残るため、sも空の文字列に置き換える。
            if "s" in deadline:
                deadline = deadline.replace("s", "")
            
            deadline = deadline.replace(" ","").split(",") ## 空白を消し、「,」で区切る。
            trash = deadline[1] ## 「時間:分:秒」を変数trashへ格納する
            deadline = deadline[:-1] ## 配列内「時間:分:秒」を削除
            deadline += trash.split(":") ## 「時間:分:秒」を「:」で区切ってdeadlineへ追加。
            
            if now.year  < task[1]:
                note +=  f"{task_num:02d}.【{task[1]:02d} / {task[2]:02d} / {task[3]:02d}  {task[4]:02d} : {task[5]:02d}】{task[0]}\n"
            else:
                note += f"{task_num:02d}.【{task[2]:02d} / {task[3]:02d}  {task[4]:02d} : {task[5]:02d}】{task[0]}\n"
            
            dl_note += f"あと{deadline[0]}日と{deadline[1]}時間{deadline[2]}分\n"
        else:
            ## 締め切り期限が切れたものは表示させない。(noteを空のままにする)
            note = ""
            tasks.remove(task) ## 締め切り期限が過ぎた配列を除去
            rewrinting_txt() ## 上記の操作で書き換えた配列をテキストファイルにも転記するため、メソッド定義2使用
    window["notice"].update(note)
    window["dl_notice"].update(dl_note)

# ------------------- メソッド定義2  タスクリストのテキストファイルを書き換える ------------------
def rewrinting_txt():
    with open("data_file/Task_Management.txt", "wt", encoding="Shift-jis") as f:
        tasks.sort (key=itemgetter(1,2,3,4,5)) ## タスクの日付を昇順で並び替え
        for task in tasks:
            task = str(task) ## 全体を文字列型に変換
            ## 角カッコ「[」「]」、シングルクォーテーション「'」、半角空白「 」を削除
            task = task.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
            f.write(task + "\n") ## テキストファイルへ書き出し

# -----------------------------------------------------------------------------------------

import PySimpleGUI as sg
import datetime
from operator import itemgetter

## テーマデザイン指定
sg.theme("LightBrown1")

## タスクリストとタスク追加のタブ定義
TaskList_tab = sg.Tab
TaskAdd_tab = sg.Tab

## タスクリストタブのレイアウト
TaskList_tab_layout = [
    [sg.Text("Today's Date", font=("Arial",24,"bold"), key="todays_date")],
    [sg.Multiline("Now Loading..", font=("Arial",17), size=(49,22), key="notice"),
    sg.Multiline("Now Loading..", font=("Arial",17), size=(21,22), key="dl_notice")],
    [sg.Text("Produced by A.M.", font=("Arial",12), text_color="black")] ## 制作者クレジット
]

## ↓↓年月日時間リスト＆タスク・メモ追加タブのレイアウト↓↓
year = [2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033] ## 年度リスト
month = [1,2,3,4,5,6,7,8,9,10,11,12] ## 月リスト
day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31] ## 日リスト
hour = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] ## 時刻リスト
minutes = [0,5,10,15,20,25,30,35,40,45,50,55,59] ## 分刻リスト (５分間隔)

TaskAdd_tab_layout = [
    [sg.Text("１．追加したいタスク名を入力してください。", font=("メイリオ",13))],
    [sg.Input(font=("メイリオ",13), text_color="slategray", key="input_title")],
    
    [sg.Text("２．年月日と時刻をそれぞれ選択してください。", font=("メイリオ",13))],
    
    [sg.Text("                          "),
    sg.Listbox(year, size=(15, 5), key="input_year"), 
    sg.Text("年", font=("メイリオ",13)),
    
    sg.Listbox(month, size=(8, 5), key="input_month"),
    sg.Text("月", font=("メイリオ",13)),
    
    sg.Listbox(day, size=(8, 5), key="input_day"),
    sg.Text("日", font=("メイリオ",13),),
    sg.Text("      "),
    
    sg.Listbox(hour, size=(8, 5), key="input_hour"),
    sg.Text("時", font=("メイリオ",13)),
    
    sg.Listbox(minutes, size=(8, 5), key="input_minutes"),
    sg.Text("分", font=("メイリオ",13))],
    [sg.Button("タスク追加", font=("明朝体",12,"bold") ,button_color="tan", size=(115,2))],
    
    [sg.Text("\nMEMO", font=("メイリオ",13))],
    [sg.Multiline("Now Loading..", font=("メイリオ",14), text_color="slategray", size=(78,10), key="input_memo")],
    
    [sg.Button("メモをセーブ", font=("明朝体",12,"bold"), button_color="goldenrod", size=(47,2)),
    sg.Button("メモを全て削除する", font=("明朝体",12,"bold"), button_color="peru", size=(46,2))]
]

## ウインドウレイアウト
window_layout = [[sg.TabGroup([[sg.Tab(" タスクリスト ", TaskList_tab_layout), sg.Tab(" タスク追加 ", TaskAdd_tab_layout)]])]]

## ウインドウ定義
window = sg.Window("Task Management", window_layout, default_element_size=(120, 1), size=(1000,700))

## タスクリスト初期設定 (タスクを書いたテキストファイルを配列化)
with open("data_file/Task_Management.txt", encoding="Shift-jis") as f:
    tasks = []
    for line in f:
        line = line.replace("\n", "").split(",") ## 改行コード「\n」を削除し「,」で区切る。
        line[1] = int(line[1]) ## 年度を数値型に変換
        line[2] = int(line[2]) ## 月を数値型に変換
        line[3] = int(line[3]) ## 日にちを数値型に変換
        line[4] = int(line[4]) ## 時刻を数値型に変換
        line[5] = int(line[5]) ## 分刻を数値型に変換
        tasks.append(line)

## メモ初期設定 (メモを書いたテキストファイルを配列化)
with open("data_file/Task_Management_MEMO.txt", encoding="Shift-jis") as f:
    memos = []
    for line in f:
        memos.append(line)

## ウインドウループ
status = 0
while True:
    ## event読取
    event, values = window.read(timeout=500)
    
    ## xボタンでプログラム終了
    if event == None:
        break
    
    ## ↓↓「タスク追加」ボタンが押されると、valuesの内容がタスクリストに追加＋表示される操作↓↓
    if event == "タスク追加" :
        if values["input_title"] and values["input_year"] and values["input_month"] and values["input_day"] and values["input_hour"] and values["input_minutes"]:
            ## 各valuesを変数に代入する
            input_title = values["input_title"]
            input_year = values["input_year"]
            input_month = values["input_month"]
            input_day = values["input_day"]
            input_hour = values["input_hour"]
            input_minutes = values["input_minutes"]
            
            ## ↓↓タスク配列追加処理 (数字は[0]と付け書き換えないと二重配列のままとなり、タスクとして追加できなくなる。)↓↓
            task_add = []
            task_add.append(input_title)
            task_add.append(input_year[0])
            task_add.append(input_month[0])
            task_add.append(input_day[0])
            task_add.append(input_hour[0])
            task_add.append(input_minutes[0])
            tasks.append(task_add) ## タスク名、年月日が揃った配列をさらにtasks配列に追加
            
            ## 追加したタスク配列をテキストファイルにも転記し、次回起動時にもデータを持ち越せるようにする処理 (メソッド定義2)
            rewrinting_txt()
            
            sg.popup_auto_close("タスクを追加しました。", title="", location=(1100,300))
            window["input_title"].update("") ## タスク名入力後、入力したタスク名をウインドウから削除する。
        else:
            sg.popup_auto_close("タスクを追加できません。", title="Error", location=(1100,300))
        
    ## ↓↓メモをテキストファイルに追加する操作↓↓
    if event == "メモをセーブ":
        with open("data_file/Task_Management_MEMO.txt", "wt", encoding="Shift-jis") as f:
            input_memo = values["input_memo"]
            f.write(input_memo)
            sg.popup_auto_close("メモをセーブしました。", title="", location=(450,750))
    
    ## ↓↓メモをウインドウに表示させる操作 (ループすると新規でメモ記入できなくなるため実行は1度きり)↓↓
    if status == 0:
        memos = "".join(memos) ## memos配列の中身を連結して、文字列に変換
        window["input_memo"].update(memos) ## メモに前回のデータを表示
        status += 1
    
    ## ↓↓メモ欄の内容を一括削除する操作↓↓
    if event == "メモを全て削除する":
        window["input_memo"].update("")
    
    TaskList() ## タスクリストタブを表示実行するため、メソッド定義1使用
