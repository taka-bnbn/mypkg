#!/bin/bash
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki
# SPDX-License-Identifier: BSD-3-Clause



import launch
from launch import LaunchDescription
from launch.actions import LogInfo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        LogInfo(
            condition=launch.conditions.LaunchConfigurationEquals('verbose', 'true'),
            msg="This is a test launch"
        ),
        Node(
            package='mypkg',
            executable='talker',  # talker ノード名
            name='talker_node',
            output='screen'
        ),
        Node(
            package='mypkg',
            executable='listener',  # listener ノード名
            name='listener_node',
            output='screen'
        ),
    ])

