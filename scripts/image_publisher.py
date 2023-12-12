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

        share_pkg_filepath = get_package_share_directory("opencv_and_ros")
        image_filename = "test_image.jpg"
        image_filepath = os.path.join(share_pkg_filepath, "images", image_filename)
        self.cv_image = cv2.imread(image_filepath, 0)
        print("Image openned!")

        self.image_pub = self.create_publisher(Image, "/image", 10)
        self.image_timer = self.create_timer(0.5, self.publish_image)
    
    def publish_image(self):
        self.ros_image = self.cv_bridge.cv2_to_imgmsg(self.cv_image, "passthrough")
        self.image_pub.publish(self.ros_image)
        print("Image published!")

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