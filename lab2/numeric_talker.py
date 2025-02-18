import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int8

#include publisher publishing to /numeric_chatter with a message type Int8
#talker keep counter start from 0 and reset back at 127 and publish to /numeric_chatter 
class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.num_publisher = self.create_publisher(Int8, 'numeric_chatter', 10)


        timer_in_seconds = 0.5
        self.timer = self.create_timer(timer_in_seconds, self.talker_callback)
        self.timer_num = self.create_timer(timer_in_seconds, self.talker_callback_num)
        self.counter = 0

    def talker_callback(self):
        msg = String()
        msg.data = f'Hello World, {self.counter}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        
    def talker_callback_num(self):
        num_msg = Int8()
        num_msg.data = self.counter 
        self.num_publisher.publish(num_msg)
        self.get_logger().info(f'Publishing numeric: {num_msg.data}')
        self.counter = (self.counter + 1) %128

        

def main(args=None):
    rclpy.init(args=args)

    talker = Talker()
    rclpy.spin(talker)


if __name__ == '__main__':
    main()