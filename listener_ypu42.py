#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ListenerNode_ypu42(Node):
    def __init__(self):
        super().__init__('listener_ypu42')
        self.subscription_ = self.create_subscription(
            String,
            'chatter_ypu42',
            self.on_msg,
            10
        )

    def on_msg(self, msg):
        self.get_logger().info(f"Heard: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = ListenerNode_ypu42()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
