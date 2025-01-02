#!/bin/bash
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki 
# SPDX-License-Identifier: BSD-3-Clause

# ROS2ワークスペースの設定
dir=~
[ "$1" != "" ] && dir="$1"

# ROS2のワークスペースに移動してビルド
cd $dir/ros2_ws || exit 1
colcon build

# ROS2環境変数をソース
source $dir/.bashrc

# ノードのテスト実行（10秒間）
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

# 現在の日本時間を取得（HHMMSS形式）
timejp=$(TZ='Asia/Tokyo' date +%H%M%S)

# 時間を2秒引いて検索用の時間を準備
timejp=$((10#$timejp - 2))  # 10#でゼロ埋めの除去を防止

# ログファイルから指定時間のメッセージを検索して表示
cat /tmp/mypkg.log | grep "${timejp}"

