#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode_ypu42(Node):
    def __init__(self):
        super().__init__('talker_ypu42')
        self.publisher_ = self.create_publisher(String, 'chatter_ypu42', 10)
        self.counter_ = 0
        self.timer_ = self.create_timer(1.0, self.publish_msg)

    def publish_msg(self):
        msg = String()
        msg.data = f"Hello from talker_ypu42 #{self.counter_}"
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = TalkerNode_ypu42()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
