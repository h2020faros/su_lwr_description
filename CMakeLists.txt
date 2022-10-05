cmake_minimum_required(VERSION 3.5)
project(lwr_description)

# find dependencies
find_package(ament_cmake REQUIRED)
  
# install
install(
  DIRECTORY gazebo launch meshes robots urdf
  DESTINATION share/${PROJECT_NAME}
  PATTERN ".svn" EXCLUDE
)

# Exports
ament_package()