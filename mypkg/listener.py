import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" & msg.data)

def main():
    rclpy.init()
    global node
    node = Node("listener")
    sub = node.create_subscrition(Int16, "countup", cb, 10)
    rclpy.spin(node)

if __name__ =='__main__':
    main()
