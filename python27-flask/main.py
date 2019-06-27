#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.api import urlfetch
import json
from flask import Flask, render_template, request
import sys
stdin = sys.stdin
stdout = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdin = stdin
sys.stdout = stdout

app = Flask(__name__)
app.debug = True

networkJson = urlfetch.fetch("http://tokyo.fantasy-transit.appspot.com/net?format=json").content  # ウェブサイトから電車の線路情報をJSON形式でダウンロードする
network = json.loads(networkJson.decode('utf-8'))  # JSONとしてパースする（stringからdictのlistに変換する）

@app.route('/')
# / のリクエスト（例えば http://localhost:8080/ ）をこの関数で処理する。
# ここでメニューを表示をしているだけです。
def root():
  return render_template('hello.html')

@app.route('/pata')
# /pata のリクエスト（例えば http://localhost:8080/pata ）をこの関数で処理する。
# これをパタトクカシーーを処理するようにしています。
def pata():
  # とりあえずAとBをつなぐだけで返事を作っていますけど、パタタコカシーーになるように自分で直してください！
  a = request.args.get('a', '')
  b = request.args.get('b', '')
  pata = ''
  max_length = (max(len(a), len(b)))
  max_length = (max(len(a), len(b)))
  for i in range(max_length):
    if(i < len(a)):
       pata += a[i]
    if(i < len(b)):
      pata += b[i]
    
  # pata.htmlのテンプレートの内容を埋め込んで、返事を返す。
  return render_template('pata.html', pata=pata)

@app.route('/norikae')
# /norikae のリクエスト（例えば http://localhost:8080/norikae ）をこの関数で処理する。
# ここで乗り換え案内をするように編集してください。
def norikae():
  network = [{"Name":"山手線","Stations":["品川","大崎","五反田","目黒","恵比寿","渋谷","原宿","代々木","新宿","新大久保","高田馬場","目白","池袋","大塚","巣鴨","駒越","田端駅","西日暮里","日暮里","鶯谷","上野","御徒町","秋葉原","神田","東京","有楽町","新橋","浜松町","田町","品川"]},{"Name":"東横線","Stations":["横浜","反町","東白楽","白楽","妙蓮寺","菊名","大倉山","綱島","日吉","元住吉","武蔵小杉","新丸子","多摩川","田園調布","自由が丘","都立大学","学芸大学","祐天寺","中目黒","代官山","渋谷"]},{"Name":"目黒線","Stations":["日吉","元住吉","武蔵小杉","新丸子","多摩川","田園調布","奥沢","大岡山","洗足","西小山","武蔵小山","不動前","目黒"]},{"Name":"池上線","Stations":["蒲田","蓮沼","池上","千鳥町","久が原","御嶽山","雪が谷大塚","石川台","洗足池","長原","旗の台","荏原中延","戸越銀座","大崎広小路","五反田"]},{"Name":"多摩川線","Stations":["多摩川","沼部","鵜の木","下丸子","武蔵新田","矢口渡","蒲田"]},{"Name":"大井町線","Stations":["二子玉川","上野毛","等々力","尾山台","九品仏","自由が丘","緑が丘","大岡山","北千束","旗の台","荏原町","中延","戸越公園","下神明","大井町"]},{"Name":"日比谷線","Stations":["中目黒","恵比寿","広尾","六本木","神谷町","霞ケ関","日比谷","銀座","東銀座","築地","八丁堀","茅場町","人形町","小伝馬町","秋葉原","仲御徒町","上野","入谷","三ノ輪","南千住","北千住"]}]
  return render_template('norikae.html', network=network)
