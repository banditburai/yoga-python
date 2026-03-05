cmake_minimum_required(VERSION 3.15)
project(yoga_python)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(PYBIND11_FINDPYTHON ON)

set(yoga_BUILD_TESTS OFF CACHE BOOL "Build Yoga tests" FORCE)

# Use local reference yoga if present, otherwise fetch from GitHub
if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/reference/yoga/CMakeLists.txt)
  message(STATUS "Using local reference yoga")
  find_package(pybind11 REQUIRED)
  add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/reference/yoga ${CMAKE_BINARY_DIR}/yoga-build EXCLUDE_FROM_ALL)
else()
  message(STATUS "Fetching yoga from GitHub...")
  include(FetchContent)
  FetchContent_Declare(
    yoga
    GIT_REPOSITORY https://github.com/facebook/yoga.git
    GIT_TAG cfdacac0e3c2e91ab15939027688756271a66025
    GIT_PROGRESS TRUE
  )
  FetchContent_MakeAvailable(yoga)
  set(yoga_SOURCE_DIR ${yoga_SOURCE_DIR})
endif()

find_package(pybind11 REQUIRED)
pybind11_add_module(yoga src/yoga/yoga.cpp)
target_include_directories(yoga PRIVATE ${yoga_SOURCE_DIR})
target_link_libraries(yoga PRIVATE yogacore)

# Install the compiled extension to the yoga package directory
install(TARGETS yoga DESTINATION "yoga")
