
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![ROS2 Node Test](https://github.com/taka-bnbn/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/taka-bnbn/mypkg/actions/workflows/test.yml)
# <font color="##ff1493">ヤフーニュース送信出力</font>

## 概要
このプログラムは， ヤフーニュースのトピックを出力送信するROS2のパッケージです.

## Node
ノード名:announcer
<br>Yahooニュースの見出しを1秒ごとに取得し, ROS2のStringメッセージとして/news トピックに配信します.
<br>トピックを購読することで, リアルタイムでニュースを受信することができます.

## Topic
Topic名:news
<br>/news トピックには， Stringメッセージが送信されます．
<br>このメッセージは， Yahooニュースの見出しが含まれています.

## 使用例
- 送信側
```bash
$ ros2 run mypkg announcer 
```
- 受信側
もう一つ端末を立ち上げ， 次のように入力する．
```bash
$ ros2 topic echo /news
```
- 実行例

![gif](https://github.com/user-attachments/assets/25cc85c1-5396-465d-bb8a-235741be8efe)

## 動作環境
- Python
- テスト済みバージョン: 3.7~3.11
- Ubuntu 22.04 LTS
- テストで利用したコンテナhttps://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2

## ライセンス

- 3条項BSDライセンスの下，再頒布及び使用が許可されます．
- このコマンドのデータの取得方法および表示方法は[このサイト](http://vividhobby.blog.fc2.com/blog-entry-553.html)や，[このサイト](http://ibarenai.seesaa.net/article/470489281.html)や，[このサイト](https://torisky.com/python%EF%BC%9Ayahoo%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E3%83%88%E3%83%94%E3%83%83%E3%82%AF%E3%82%B9%E3%82%92%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB%E3%81%AB%E8%A1%A8%E7%A4%BA%E3%81%99/)や，[このサイト](https://zenn.dev/autumn_nsn/articles/298f579784305a)
を基にコードを書いています．

### Yahoo Newsのスクレイピングについて
Yahoo Newsの[robots.txt](https://news.yahoo.co.jp/robots.txt)に， User-agent: * と記述があったのと， Disallow:/topic/の記述がないため， 使用してもよいと判断しました．

## Copyright
© 2024 Takaya Mizumaki 水牧鷹哉
