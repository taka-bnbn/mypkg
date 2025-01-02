#!/bin/bash
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki 
# SPDX-License-Identifier: BSD-3-Clause

# スクリプトのディレクトリ
dir=~
[ "$1" != "" ] && dir="$1"

# ROS2ワークスペースに移動してビルド
cd $dir/ros2_ws || { echo "ROS2 workspace not found!"; exit 1; }
source /opt/ros/humble/setup.bash
colcon build || { echo "Build failed!"; exit 1; }

# 環境変数をソース
source $dir/ros2_ws/install/setup.bash

# ノード実行
timeout 5 ros2 run mypkg news_publisher > /tmp/mypkg.log 2>&1

# 現在の日本時間を取得（HHMMSS形式）
timejp=$(TZ='Asia/Tokyo' date +%H%M%S)

# 時間を2秒引いて検索に使用
timejp=$((timejp - 2))

# ログファイルが存在すれば結果を確認
if [ -f /tmp/mypkg.log ]; then
    # ログファイルから指定された時間を検索
    log_entry=$(grep "${timejp}" /tmp/mypkg.log)
    if [ -n "$log_entry" ]; then
        echo "ログが見つかりました: $log_entry"
    else
        echo "指定された時間のログエントリが見つかりませんでした。"
    fi
else
    echo "ログファイルが見つかりません。"
    exit 1
fi

