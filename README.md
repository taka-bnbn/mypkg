
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![ROS2 Node Test](https://github.com/taka-bnbn/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/taka-bnbn/mypkg/actions/workflows/test.yml)
# <font color="##ff1493">ヤフーニュース送信出力</font>

## 概要
このプログラムは，ヤフーニュースのトピックを出力送信するROS2のパッケージです.

## Node
ノード名: announcer
<br>Yahooニュースの見出しを1秒ごとに取得し, ROS2のStringメッセージとして/news トピックに配信します.
<br>トピックを購読することで, リアルタイムでニュースを受信することができます.

## Topic
トピック名: news
<br>/news トピックには， Stringメッセージが送信されます．
<br>このメッセージは， Yahooニュースの見出しが含まれています.

## 使用例
- 送信側
```bash
$ ros2 run mypkg announcer 
```
- 受信側
もう一つ端末を立ち上げ，次のように入力する．
```bash
$ ros2 topic echo /news
```
```bash
![gif](https://github.com/user-attachments/assets/25cc85c1-5396-465d-bb8a-235741be8efe)
```
## 動作環境
- Python
- テスト済みバージョン: 3.11 
- Ubuntu 22.04 LTS
- ROS2 humble 
- テストで利用したコンテナhttps://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2

## Yahoo Newsのトピック利用に関して
Yahoo NEWSの[robots.txt](https://news.yahoo.co.jp/robots.txt)のSitemapに，"https://news.yahoo.co.jp/sitemaps/topicsList.xml" と, "https://news.yahoo.co.jp/sitemaps/pickup.xml" との記述があったため， 使用してもよいと判断しました．

## 注意事項
本ツールは, ヤフーニュースのコンテンツを自動的に収集するために作成されたものであり, ヤフー株式会社とは一切の関係はありません.
<br>本ツールはニュースの表示やデータ収集を目的としていますが, 収集されるニュースコンテンツに関する著作権は, ヤフー株式会社またはその関連会社に帰属します.
<br>コンテンツの利用にあたっては, 著作権法等の法的規制を遵守してください.

## ライセンス
- 3条項BSDライセンスの下，再頒布及び使用が許可されます．
- このコマンドのデータの取得方法および表示方法は以下のサイトを利用しました．
- http://vividhobby.blog.fc2.com/blog-entry-553.html
- http://ibarenai.seesaa.net/article/470489281.html
- https://torisky.com/python%EF%BC%9Ayahoo%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E3%83%88%E3%83%94%E3%83%83%E3%82%AF%E3%82%B9%E3%82%92%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB%E3%81%AB%E8%A1%A8%E7%A4%BA%E3%81%99/
- https://zenn.dev/autumn_nsn/articles/298f579784305a

## Copyright
© 2024 Takaya Mizumaki 水牧鷹哉

