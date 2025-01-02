#!/bin/bash
# SPDX-FileCopyrightText: 2024 Takaya Mizuzmaki
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

timejp=$(TZ='Asia/Tokyo' date +%H%M%S)
timejp=$((timejp - 2))

grep "${timejp}" /tmp/mypkg.log

