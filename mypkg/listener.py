import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.create_subscription(Int16, 'countup', self.cb, 10)

    def cb(self, msg):
        self.get_logger().info(f'Listene: (msg.data)')

def main():
    rclpy.init()
    listener = Listener()
    rclpy.spin(listener)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
