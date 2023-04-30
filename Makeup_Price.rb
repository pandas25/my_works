=begin
################## Makeup Price 2023/01/17 ######################
【作品名】 Makeup Price
【概要】
その日使用した化粧品を選択肢から選び、その日の化粧品の総額を計測し表示するプログラム。
化粧品情報が入力されたCSVファイルを読みこませプログラムを起動し、質問に答えていくと最後に総額を教えてくれます。

【目的】
高価なものを身に着けると気分が良くなる点に着目し、
「その日使った化粧品の値段を可視化する」ことでわかりやすく気分を上げたり自信を付けられたらと思い作りました。
ユーザーはメイクにこだわりがある人やコスメ収集癖のあるコレクター層、マニア層を想定しており、
そのような人たちのテンションを丸1日上げるプログラムです。

【アピールポイント】
[1] 手持ちの化粧品が増えたり減ったりしても、CSVファイルを編集するだけでプログラムがまた正常に作動してくれます。
    (Excelから直接編集すると文字化けする可能性があるためVSCode等からの編集を推奨)
[2] 文字のカラーや太線等を指定したり画面を切り替えたりして、見やすさやわかりやすさを重視したデザインにしました。
[3] 使用した化粧品が複数ある場合でも1度にまとめて入力できるようにして、ユーザーの手間を省きました。
[4] 使用した化粧品番号を入力後、化粧品の名称と値段を一旦表示することで選択間違いを防止できるように工夫しました。
[5] 総額が0円だった場合はユーザーを肯定してあげる一言を実装し、落ち込ませないようにしました。
[6] 選択肢にない番号を入力した際は再チャレンジを促してからプログラムを終了させて、バグが起きないようにしました。
[7] 化粧品の選択肢番号にインデックス番号を使用することでどの化粧品が選択されたのか、取り出しやすくなりました。
###################################################################
=end
#--------------------- メソッド定義1   使用した化粧品の詳細を尋ねる -----------------------------
def makeup_tools(genre)
    require "tty" ## 文字の色、下線斜線太線を指定可能にする
    cur = TTY::Cursor
    reader = TTY::Reader.new
    pastel = Pastel.new
    
    comma = pastel.bright_red ("半角コンマ(,)")
    puts "\n"
    puts pastel.bold.yellow ("*****************************************************************")
    puts "使用された化粧品の「番号」を「半角数字」で入力してお答えください。"
    puts "複数ある場合は「#{comma}」で区切ってください。"
    puts pastel.bold.yellow ("*****************************************************************")
    puts "\n"
    
    File.open ("data_file/Makeup_Price.csv") do |f|
        f.each_with_index do |line, n| ## 一行ずつデータとともにインデックス番号も取り出す
            line.chomp!
            dat = line.split(",")
            puts "[#{n+1}] " + dat[1] if genre == dat[0]   ## 分類ごとに化粧品を表示させる
        end
    end
end
#------------------------- メソッド定義2     プログラム終了前の演出 -----------------------------------
def ending(scene)
    require "tty" ## 文字の色、下線斜線太線を指定可能にする
    cur = TTY::Cursor
    reader = TTY::Reader.new
    pastel = Pastel.new
    
    ##### ↓↓↓2秒後に強制終了↓↓↓ #####
    puts "該当する番号がありません。\n強制終了します。" if scene == "error"
    puts "\n"
    square = pastel.red ("◆")
    sleep (0.5)
    puts "." + square
    sleep (0.5)
    puts ".." + square
    sleep (0.5)
    puts "..." + square
    sleep (0.5)
    print cur.clear_screen ## 画面切り替え
    
    ## "error"の場合、最初からやり直すことを促す。
    ## "finish"の場合(else)、カーソルのみ指定。(このあと総額発表)
    if scene == "error"
        print cur.move_to(10,3)
        puts pastel.underline.italic ("最初からやり直してください。")
        print cur.move_to(6,6)
        puts pastel.bold.underline.italic.magenta ("- Thank you. Produced by A.M. -") ## 制作者クレジット
        puts "\n"
    else
        print cur.move_to(1,3)
    end
end
#-------------------------------------------------------------------------------------------

require "tty" ## 文字の色、下線斜線太線を指定可能にする
cur = TTY::Cursor
reader = TTY::Reader.new
pastel = Pastel.new

cosme_group = []
cosme_price = {}
index_cosme = {}
sum = 0

## 私物の化粧品情報が入力されているファイルを開く。
File.open ("data_file/Makeup_Price.csv") do |f|
    ##### ↓↓↓タイトル、前置き説明を表示↓↓↓ #####
    puts cur.clear_screen
    print cur.move_to(5,3)
    puts pastel.bold.underline.italic.magenta ("- Makeup Price -\n")
    puts pastel.bold.underline ("今日もお綺麗なあなたに質問です。どのような化粧品を使用なさったのでしょうか。")
    kyouchou = pastel.red ("半角数字")
    puts pastel.bold.underline ("質問には全て#{kyouchou}を入力してお答えください。\n\n")
    print pastel.bold.on_bright_black ("  Press the Key  ")
    reader.read_char ## 待機
    print cur.move_to(0,9) ## 「Press the Key」を次の質問で被せて消したいためカーソルをここに合わせる。
    
    #↑                 - Makeup Price -
    #           今日もお綺麗なあなたに質問です。どのような化粧品を使用なさったのでしょうか。
    #           質問には全て半角数字を入力してお答えください。
    #            Press the Key
    
    #::::::::【キーボード待機】::::::::#
    #::::::::ここでなにかキーを押してもらう::::::::#
    
    ##### ↓↓↓ファイルを一行ずつ処理する。split(",")で分け、配列やハッシュを作る。↓↓↓#####
    f.each_with_index do |line, n|
        line.chomp!
        dat = line.split(",")
        cosme_group.push (dat[0])
        cosme_group = cosme_group.uniq ## 化粧品の分類をまとめた配列。(重複をuniqで削除)
        cosme_price[dat[1]] = dat[2].to_i ## 商品名と値段のハッシュ
        index_cosme[n+1] = dat[1] ## インデックス番号＋１と商品名のハッシュ
    end
    
    ##### ↓↓↓配列cosme_groupから一行ずつジャンルデータとともにインデックス番号も取り出す。↓↓↓ #####
    cosme_group.each_with_index do |genre, n|
        puts "Q#{n+1}. #{genre}は使用しましたか。" ## 大まかな分類を質問する
        puts "[1]YES  [2]NO"
        print "[ANSWER] "
        input_genre = gets.to_i
        
        #ex.↑        Q1. スキンケア用品は使用しましたか。
        #            [1]YES  [2]NO
        #            [ANSWER]
        
        #:::::【キーボード数字入力待機】:::::#
        #:::::ここで[1]YES [2]NO の番号で入力してもらう:::::#
        
        if input_genre == 1
            makeup_tools(genre) ## 使った化粧品の詳細を質問するため、化粧品を表示させるメソッド1を使用
            print "[ANSWER] "
            input_index = gets.split(",").map {|x| x.to_i}
            
            #ex.↑         [1] ナチュリエ  ハトムギ化粧水
            #             [2] ちふれ  美白乳液VC
            #             [ANSWER]
            
            #:::::【キーボード数字入力待機。","で区切る。】:::::#
            #:::::ここで化粧品の選択肢番号を入力してもらう:::::#
            
            puts "\n"
            ## １．変数input_indexにキーボード入力されたn番に該当する商品(ハッシュindex_cosme使用)とその値段を表示。
            ## ２．該当商品からその商品の値段(ハッシュcosme_price使用)を変数sumに追加していく。
            
            input_index.each do |index|
                if index_cosme[index] ##「もし、index_cosmeにキーボード入力した数字(index)があれば」
                    
                    ## 正規表現「.to_s.gsub(/(\d)(?=\d{3}+$)/, "\\1,"」を使用して値段が4桁以上の場合は「,」で区切る。
                    puts "#{index_cosme[index]}  ¥#{cosme_price[index_cosme[index]].to_s.gsub(/(\d)(?=\d{3}+$)/, "\\1,")}"
                    sum += cosme_price[index_cosme[index]] ## 値段をsumに足していく。
                    
                    #ex.↑            PAUL&JOE  プロテクティングファンデーションプライマー 01〈日焼け止め用化粧下地・美容液〉  ¥3,850
                    #                Wonjungyo  トーンアップベース 01 ピーチピンク〈化粧下地〉  ¥1,430
                    
                else
                    ending("error") ## 存在しない番号が押された場合はプログラム終了する演出を表示させるため、メソッド定義2を使用
                    return ## returnを使って全ての操作を強制終了させる。(breakにすると分類の質問ループがまだ続くため。)
                end
            end
            
            puts "---------------"
            puts pastel.bright_blue (" NEXT➡ ")
            sleep (0.8)
            print cur.clear_screen ## 上記で商品の選択肢が出たら画面を切り替え、見やすくする。
            print cur.move_to(0,1)
        elsif input_genre == 2
            puts "---------------"
            puts pastel.bright_blue (" NEXT➡ ")
            sleep(0.8)
            print cur.clear_screen ## 画面切り替え
            print cur.move_to(0,1)
        else ## 存在しない番号が押された場合の処理
            puts "\n"
            ending("error") ## プログラム終了する演出を表示させるため、メソッド定義2を使用
            return ## returnを使って全ての操作を強制終了させる。(breakにすると下記のエンディングがまだ続くため。)
        end       
    end
    
    ending("finish") ## プログラム終了する演出を表示させるため、メソッド定義2を使用
    
    sum = sum.to_s.gsub(/(\d)(?=\d{3}+$)/, "\\1,") ## 正規表現でsumが4桁以上の場合は「,」で区切る。
    puts "本日のお顔  ¥#{sum} で構成されています。" ## 使用した化粧品の総額を表示
    
    ## sumが0の場合、ユーザーを肯定する簡単な一言を英語で表示
    ## sumが1以上の場合、カーソルのみ指定(このあと制作者クレジット表示)
    if sum == "0"
        print cur.move_to(10,5)
        puts pastel.italic.bright_black ("You are beautiful as you are.")
        print cur.move_to(6,8)
    else
        print cur.move_to(6,6)
    end
    
    puts pastel.bold.underline.italic.magenta ("- Thank you. Produced by A.M. -") ## 制作者クレジット
    puts "\n"
    
end