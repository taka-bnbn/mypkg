#!/bin/bash
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki
# SPDX-License-Identifier: BSD-3-Clause

# デフォルトの作業ディレクトリ
dir=~
[ "$1" != "" ] && dir="$1"

# ROS 2 ワークスペースのビルド
cd "$dir/ros2_ws" || { echo "Failed to change directory to $dir/ros2_ws"; exit 1; }

# ROS 2環境を設定
if [ -f "$dir/.bashrc" ]; then
    source "$dir/.bashrc"
else
    echo "No .bashrc file found in $dir"
    exit 1 
fi

# ROS 2ノードを起動
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log || { echo "Failed to launch ROS 2 node"; exit 1; }

# ニュースのキーワードを取得（例: 定義済みのキーワード）
news="example_keyword"

# ログ内でニュースキーワードを検索
if grep -q "$news" /tmp/mypkg.log; then
    echo "Found keyword '$news' in log file"
else
    echo "Keyword '$news' not found in log file"
fi

