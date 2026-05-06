#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class AvoidTugbot(Node):
    def __init__(self):
        super().__init__('avoid_tugbot')
        self.pub = self.create_publisher(Twist, '/model/tugbot/cmd_vel', 10)
        self.sub = self.create_subscription(
            LaserScan,
            '/world/world_demo/model/tugbot/link/scan_front/sensor/scan_front/scan',
            self.laser_callback,
            10
        )

    def laser_callback(self, scan):
        valeurs = [v for v in scan.ranges if not math.isinf(v) and not math.isnan(v) and v > 0.05]

        msg = Twist()

        if len(valeurs) == 0:
            msg.linear.x = 0.25
            msg.angular.z = 0.0
        else:
            distance_min = min(valeurs)

            if distance_min < 0.8:
                msg.linear.x = 0.0
                msg.angular.z = 0.7
            else:
                msg.linear.x = 0.35
                msg.angular.z = 0.0

        self.pub.publish(msg)

def main():
    rclpy.init()
    node = AvoidTugbot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
