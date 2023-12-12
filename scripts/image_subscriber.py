#!/usr/bin/env python3
# ROS2 Libraries
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
# OpenCV Libraries
import cv2
from cv_bridge import CvBridge
# Python Libraries
from ament_index_python import get_package_share_directory
import os

class ImagePublisher(Node):
    def __init__(self):
        super().__init__("image_publisher")
        self.cv_bridge = CvBridge()

        self.image_sub = self.create_subscription(
            Image, 
            "/image", 
            self.subscribe_to_image,
            10
        )
    
    def subscribe_to_image(self, image_msg):
        self.cv_image = self.cv_bridge.imgmsg_to_cv2(image_msg, "passthrough")
        cv2.imshow("Image Window", self.cv_image)
        print("Image Showed!")
        cv2.waitKey(3)

def main(args= None):
    rclpy.init(args= args)
    image_publisher_node = ImagePublisher()
    try:
        rclpy.spin(image_publisher_node)
    except KeyboardInterrupt:
        image_publisher_node.destroy_node()
        rclpy.try_shutdown()

if __name__ == "__main__":
    main()