#!/bin/bash
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki 
# SPDX-License-Identifier: BSD-3-Clause
dir=~
[ "$1" != "" ] && dir="$1"

# ROS2ワークスペースディレクトリに移動してビルド
cd $dir/ros2_ws || { echo "ROS2 workspace not found!"; exit 1; }
source /opt/ros/humble/setup.bash
colcon build || { echo "Build failed!"; exit 1; }

# 環境変数をソース
source $dir/ros2_ws/install/setup.bash

# 10秒間、ROS2ノードを実行
timeout 10 ros2 run mypkg news_publisher > /tmp/mypkg.log 2>&1

# 現在の日本時間を取得（HHMMSS形式）
timejp=$(TZ='Asia/Tokyo' date +%H%M%S)

# 時間を2秒引いて検索に使用
timejp=$((timejp - 2))

# ログファイルから指定された時間のニュースを検索して表示
if [ -f /tmp/mypkg.log ]; then
    cat /tmp/mypkg.log | grep "${timejp}" || echo "No matching log entries found."
else
    echo "Log file not found!"
fi
