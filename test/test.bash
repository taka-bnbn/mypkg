#!/bin/bash
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws" || { echo "Failed to change directory to $dir/ros2_ws"; exit 1; }

if [ -f "$dir/.bashrc" ]; then
    source "$dir/.bashrc"
else
    echo "No .bashrc file found in $dir"
    exit 1
fi

timezone=$(date +'%Z')

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log || { echo "Failed to launch ROS 2 node"; exit 0; }

echo "Timezone: $timezone" >> /tmp/mypkg.log

news="example_keyword"

if grep -q "$news" /tmp/mypkg.log; then
    echo "Found keyword '$news' in log file"
else
    echo "Keyword '$news' not found in log file"
fi

