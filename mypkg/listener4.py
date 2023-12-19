# SPDX-FileCopyrightText; 2023 Ryosuke Suzuki ryo135791113@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random

class Listen4():
    def __init__(self, node):
        self.sub = node.create_subscription(Float64, "countup3", self.cb, 10)
        self.pub = node.create_publisher(Float64, "countup4", 10)
        self.total = 0.0
        self.prev = 0.0

    def cb(self, msg):
        global node
        if msg.data == 0:
            msg.data = float(random.randint(10, 100))
        if self.total <= 1:
            self.total = 1000
        self.total = self.prev / msg.data
        self.prev = msg.data
        node.get_logger().info("Listen4: %f" % self.total)
        self.pub.publish(Float64(data=self.total))

rclpy.init()
node = Node("Listen4")
Listen4 = Listen4(node)
rclpy.spin(node)
