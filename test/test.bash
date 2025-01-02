#!/bin/bash
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki 
# SPDX-License-Identifier: BSD-3-Clause
# 初期ディレクトリの設定
dir=~
[ "$1" != "" ] && dir="$1"

# ROS 2のワークスペースに移動し、ビルドを実行
cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# ROS 2のランチファイルを指定時間実行し、ログを取得
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

# 現在の日本時間を取得し、2秒前の時刻を計算
timejp=$(TZ='Asia/Tokyo' date +%H%M%S)
timejp=$((timejp-2))

# ログから特定の時刻に対応する行を抽出
cat /tmp/mypkg.log | grep "${timejp}"
