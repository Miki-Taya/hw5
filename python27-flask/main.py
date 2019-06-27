#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.api import urlfetch
import json
from flask import Flask, render_template, request

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
  print(pata)
    
  # pata.htmlのテンプレートの内容を埋め込んで、返事を返す。
  return render_template('pata.html', pata=pata)

@app.route('/norikae')
# /norikae のリクエスト（例えば http://localhost:8080/norikae ）をこの関数で処理する。
# ここで乗り換え案内をするように編集してください。
def norikae():
  return render_template('norikae.html', network=network)
