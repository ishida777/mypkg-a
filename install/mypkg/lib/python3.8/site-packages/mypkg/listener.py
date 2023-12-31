import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.pub = self.create_subscription(Int16, 'countup', self.cb, 10)

    def cb(self, msg):
        self.get_logger().info("Listener:%d"%msg.data)

    rclpy.init()
    node = Listener()
    rcloy.spin(node)
