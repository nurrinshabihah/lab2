import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int8


class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(String, 'chatter', self.listener_callback, 10)
        self.subscription_num = self.create_subscription(Int8, 'numeric_chatter', self.listener_callback_num, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data!r}')
    def listener_callback_num(self, num_msg):
        self.get_logger().info(f'I heard numeric: {num_msg.data!r}')


def main(args=None):
    rclpy.init(args=args)
    listener = Listener()
    rclpy.spin(listener)


if __name__ == '__main__':
    main()
