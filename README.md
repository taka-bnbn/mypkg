
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![ROS2 Node Test](https://github.com/taka-bnbn/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/taka-bnbn/mypkg/actions/workflows/test.yml)
### <font color="##ff1493">今話題に上がっているニュースが気になりませんか？</font>

## 概要
- yahooニュースのトピックを出力送信

## 使用例
- 送信側
```bash
$ ros2 run mypkg talker
```
- 受信側
```bash
$ ros2 topic echo /news
data: 3公民館での飲酒が禁止に、町内会に広がる波紋「交流の機会減る」 広島県府中市中国新聞デジタル1/2(木)10:48 - https://news.yahoo.co.jp/articles/d556b45d82bcadf1b6c097d1fdafe78c68...
---
data: 1中村陽喜 7歳＆夏幹 4歳　父・中村獅童の家での姿に次々止まらないクレーム日テレNEWS NNN1/2(木)21:404:41 - https://news.yahoo.co.jp/articles/d58808f1a6e47ececda5c9e701a...
---
data: 2市川ぼたん 13歳「二人がいるとより笑えるし、楽しい」　團十郎、新之助への思い日テレNEWS NNN1/2(木)22:054:09 - https://news.yahoo.co.jp/articles/a918c3dabb97b83bec8757171...
---
data: 3ロープウェーで異臭騒ぎ　「液体をまかれた」と通報テレビ朝日系（ANN）1/3(金)0:200:57 - https://news.yahoo.co.jp/articles/01f65d9f4f53c264a171460c4ce8aa54fd04a8e0
---
data: 1「陸上人生で初…なんだコレ」青学大・原晋監督“じつは異常事態だった”3区、失速の原因は？ それでも箱根駅伝で負けない異様さ…TV解説者の“発言”Number Web1/2(木)20:02 - https://news.yahoo.co.jp/articl...
---
data: 2橋本環奈＆伊藤沙莉『紅白』司会コンビの衣装に “待遇の差” で視聴者困惑…「生放送の経験値の差」も影響かSmartFLASH1/2(木)14:38 - https://news.yahoo.co.jp/articles/8c9da75b6362d6707...
---
```
- 実行例

![gif]((https://github.com/user-attachments/assets/25cc85c1-5396-465d-bb8a-235741be8efe)

## 動作環境
- テスト済みバージョン: 3.7~3.11
- Ubuntu 22.04 LTS

## ライセンス

- 3条項BSDライセンスの下，再頒布及び使用が許可されます．
- このコマンドのデータの取得方法および表示方法は[このサイト](http://vividhobby.blog.fc2.com/blog-entry-553.html)や，[このサイト](http://ibarenai.seesaa.net/article/470489281.html)や，[このサイト](https://torisky.com/python%EF%BC%9Ayahoo%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E3%83%88%E3%83%94%E3%83%83%E3%82%AF%E3%82%B9%E3%82%92%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB%E3%81%AB%E8%A1%A8%E7%A4%BA%E3%81%99/)
を基にコードを書いています．

## Copyright
© 2024 Takaya Mizumaki 水牧鷹哉
