#!/bin/bash
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki
# SPDX-License-Identifier: BSD-3-Clause

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
        self.timer = self.create_timer(1.0, self.publish_news)
        self.get_logger().info('ノードを開始するお.')
        self.news_url = 'https://news.yahoo.co.jp'
        self.headlines = []
        self.index = 0

    def fetch_news(self):
        try:
            response = requests.get(self.news_url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')

            elems = soup.find_all('a', href=re.compile("news.yahoo.co.jp/pickup"))
            headlines = []
            for elem in elems:
                headline = elem.get_text(strip=True)
                link = elem.attrs['href']
                headlines.append(f"{headline} - {link}")

            elems = soup.find_all('a', href=re.compile("news.yahoo.co.jp/topics"))
            for elem in elems:
                headline = elem.get_text(strip=True)
                link = elem.attrs['href']
                headlines.append(f"{headline} - {link}")

            self.headlines = headlines
        except Exception as e:
            self.get_logger().error(f"ニュースが見つからん(´;ω;｀): {e}")

    def publish_news(self):
        if not self.headlines:
            self.fetch_news()

        if self.index < len(self.headlines):
            msg = String()
            msg.data = self.headlines[self.index]
            self.publisher_.publish(msg)
            self.index += 1
        else:
            self.index = 0
            self.fetch_news()

def main(args=None):
    rclpy.init(args=args)
    node = NewsPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('ノードを終了したお')
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
if __name__ == '__main__':
    main()

