cmake_minimum_required(VERSION 2.8)
project(proc)

set(CMAKE_CXX_FLAGS "-std=c++11 -Wall ${CMAKE_CXX_FLAGS}")
set(CMAKE_INSTALL_PREFIX ${CMAKE_BINARY_DIR}/run)

add_executable(ece650-a2 ece650-a2.cpp)
add_executable(proc proc.cpp)

install(TARGETS ece650-a2 proc RUNTIME DESTINATION bin)
