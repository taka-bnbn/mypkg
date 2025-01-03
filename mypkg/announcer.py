import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
from bs4 import BeautifulSoup
import re

class NewsPublisher(Node):
    def __init__(self):
        super().__init__('news_publisher')
        self.publisher_ = self.create_publisher(String, '/news', 10)
        self.timer = self.create_timer(1.0, self.publish_news)  # 1秒ごとにニュースを配信
        self.get_logger().info('News Publisher Node has started.')
        self.news_url = 'https://news.yahoo.co.jp'
        self.headlines = []  # ニュースの見出しを格納するリスト
        self.index = 0  # 配信するニュースのインデックス

    def fetch_news(self):
        try:
            # Yahooニュースのページを取得
            response = requests.get(self.news_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # pickupニュース
            elems = soup.find_all('a', href=re.compile("news.yahoo.co.jp/pickup"))
            headlines = []
            for elem in elems:
                # 見出し（テキスト）を抽出し、HTMLタグを取り除く
                headline = elem.get_text(strip=True)
                link = elem.attrs['href']
                headlines.append(f"{headline} - {link}")

            # トップニュース
            elems = soup.find_all('a', href=re.compile("news.yahoo.co.jp/topics"))
            for elem in elems:
                headline = elem.get_text(strip=True)
                link = elem.attrs['href']
                headlines.append(f"{headline} - {link}")

            # その他のニュース
            elems = soup.find_all('a', href=re.compile("news.yahoo.co.jp/articles"))
            for elem in elems:
                headline = elem.get_text(strip=True)
                link = elem.attrs['href']
                headlines.append(f"{headline} - {link}")

            # ニュースの見出しリストを保存
            self.headlines = headlines
        except Exception as e:
            self.get_logger().error(f"Failed to fetch news: {e}")

    def publish_news(self):
        if not self.headlines:
            # ニュースがまだ取得されていなければ、ニュースを取得
            self.fetch_news()

        if self.index < len(self.headlines):
            # リストから1つのニュースを取得して配信
            msg = String()
            msg.data = self.headlines[self.index]
            self.publisher_.publish(msg)
            self.index += 1  # インデックスを1つ進める
        else:
            # すべてのニュースを配信したら終了
            self.index = 0  # インデックスをリセット
            self.fetch_news()  # 再度ニュースを取得

def main(args=None):
    rclpy.init(args=args)
    node = NewsPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down News Publisher Node.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

