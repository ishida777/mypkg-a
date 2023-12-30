#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bahsrc
timeout 10 ros2 launch mypkg talk_listen.launch > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen: 10'
