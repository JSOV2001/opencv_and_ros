cmake_minimum_required(VERSION 3.8)
project(opencv_and_ros)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Defining ROS2 packages
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)

# Installing custom ROS2 Python codes
ament_python_install_package(scripts)
install(PROGRAMS
  scripts/image_publisher.py
  scripts/image_subscriber.py
  DESTINATION lib/${PROJECT_NAME}
)

# Installing additional directories for the ROS2 package
install(
  DIRECTORY images
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
