# Install script for directory: /home/mrey49/sor_ws/src/sor-ros-session1/erc_sor_ros_session1

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/mrey49/sor_ws/src/sor-ros-session1/install/erc_sor_ros_session1")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1" TYPE DIRECTORY FILES
    "/home/mrey49/sor_ws/src/sor-ros-session1/erc_sor_ros_session1/launch"
    "/home/mrey49/sor_ws/src/sor-ros-session1/erc_sor_ros_session1/worlds"
    "/home/mrey49/sor_ws/src/sor-ros-session1/erc_sor_ros_session1/rviz"
    "/home/mrey49/sor_ws/src/sor-ros-session1/erc_sor_ros_session1/urdf"
    "/home/mrey49/sor_ws/src/sor-ros-session1/erc_sor_ros_session1/meshes"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/erc_sor_ros_session1")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/erc_sor_ros_session1")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1/environment" TYPE FILE FILES "/opt/ros/jazzy/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1/environment" TYPE FILE FILES "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1/environment" TYPE FILE FILES "/opt/ros/jazzy/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1/environment" TYPE FILE FILES "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_environment_hooks/path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1" TYPE FILE FILES "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_environment_hooks/local_setup.bash")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1" TYPE FILE FILES "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_environment_hooks/local_setup.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1" TYPE FILE FILES "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1" TYPE FILE FILES "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1" TYPE FILE FILES "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_environment_hooks/package.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_index/share/ament_index/resource_index/packages/erc_sor_ros_session1")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1/cmake" TYPE FILE FILES
    "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_core/erc_sor_ros_session1Config.cmake"
    "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/ament_cmake_core/erc_sor_ros_session1Config-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/erc_sor_ros_session1" TYPE FILE FILES "/home/mrey49/sor_ws/src/sor-ros-session1/erc_sor_ros_session1/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/mrey49/sor_ws/src/sor-ros-session1/build/erc_sor_ros_session1/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
