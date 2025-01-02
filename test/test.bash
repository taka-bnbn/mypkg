#!/bin/bash
# SPDX-FileCopyrightText: 2024 Takaya Mizuzmaki 
# SPDX-License-Identifier: BSD-3-Clause

# ディレクトリ設定（引数があれば指定されたディレクトリに移動）
dir=~
[ "$1" != "" ] && dir="$1"

# ROS2のワークスペースディレクトリに移動してビルド
cd $dir/ros2_ws
colcon build

# 環境変数をソース
source $dir/.bashrc

# 10秒間、ROS2ノード（launchファイル）を実行
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

# 現在の日本時間を取得（HHMMSS形式）
timejp=$(TZ='Asia/Tokyo' date +%H%M%S)

# 時間を2秒引いて検索に使用
timejp=$((timejp - 2))

# ログファイルから指定された時間のニュースを検索して表示
cat /tmp/mypkg.log | grep "${timejp}"

