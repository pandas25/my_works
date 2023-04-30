''' ############## Korean Spots Searcher 2023/01/17 #######################
【作品名】Korean Spots Searcher  ～ 韓国旅行スポット可視化 ～
【概要・目的】
韓国の巡りたい場所をリストアップするとマップにピンが立つプログラムです。
CSVファイルにユーザーが書き込み、プログラムを実行することでHTMLが生成され見ることができます。
韓国旅行を計画している人たちをユーザーとして想定しています。
「旅行計画話し合いの段階」で、「行きたい地点とそれぞれの場所関係」をわかりやすく「可視化・整理」することを目的に開発しました。

【アピールポイント】
1. 韓国で巡りたいスポットをまとめてCSVファイルを自作
        緯度、経度、ジャンル、名称、コメントで分けています。
        観光場所を追加・削除したい場合はCSVファイルを変更するだけです。
2. 空港、宿泊ホテル、映えスポット、カフェ・飲食店でマップ記号・色をそれぞれ指定
        行きたいと思っている場所関係が一目でわかるようになります。
3. 場所クリックして吹き出しを出し（ポップアップ）簡単な情報を表示
        「ここどんな場所だったっけ？」とならないようにする工夫です。
4. クリックでその座標を吹き出し（ポップアップ）に表示
        ピンの場所が微妙にズレていて修正したいときに活用可能です。
5. 初めて見た人にもわかりやすい説明
        CSVファイルの中に「CSVファイルの手引き・注意点」を設けました。
        初めて使う人でもエラーを出させないようにする工夫です。
###############################################################################'''

import pandas as pd
import folium

## データフレームを読み込む
df = pd.read_csv("data_file/Korean_Spots_Searcher.csv", encoding="UTF-8")

## 観光したい地点のジャンル、緯度、経度、名称、コメントをリスト化する
Korea_list = df[["ジャンル","緯度","経度","名称","コメント"]].values

## マップ作成 (中心をソウルに設定)
m = folium.Map(location=[37.5665, 126.9779], zoom_start=10)

## マップに書き出し
for data in Korea_list:
    
    ## コメントを吹き出し表示するように定義
    popup = folium.Popup(data[4])
    
    ## ジャンルによってマップアイコンを指定するためif文を使う
    if data[0] == "空港":
        folium.Marker(
        [data[1], data[2]],    ## 緯度と経度を読み込んで座標表示
        tooltip = data[3],     ## 名称を表示
        icon = folium.Icon(color="blue", icon="plane"),  ## マップアイコン指定して表示
        popup = popup          ## コメントを吹き出し表示
		).add_to(m)
    
    elif data[0] == "ホテル":
        folium.Marker(
        [data[1], data[2]], 
        tooltip = data[3],
        icon = folium.Icon(color="green", icon="home"),
        popup = popup
		).add_to(m)
    
    elif data[0] == "KPOP":
        folium.Marker(
        [data[1], data[2]], 
        tooltip = data[3],
        icon = folium.Icon(color="pink", icon="music"),
        popup = popup
		).add_to(m)
    
    elif data[0] == "カフェ・飲食":
        folium.Marker(
        [data[1], data[2]], 
        tooltip = data[3],
        icon = folium.Icon(color="purple", icon="cutlery"),
        popup = popup
		).add_to(m)
    
    elif data[0] == "観光地":
        folium.Marker(
        [data[1], data[2]], 
        tooltip = data[3],
        icon = folium.Icon(color="orange", icon="camera"),
        popup = popup
		).add_to(m)
    
    elif data[0] == "その他":
        folium.Marker(
        [data[1], data[2]], 
        tooltip = data[3],
        icon = folium.Icon(color="black", icon="check"),
        popup = popup
		).add_to(m)
    
    else:
        break

## とある地点をクリックすると座標が吹き出しで出てくる
folium.LatLngPopup().add_to(m)

## HTMLとして保存
m.save("Korean_Spots_Searcher.html")
