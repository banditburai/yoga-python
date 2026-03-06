cmake_minimum_required(VERSION 3.15)
project(yoga_python)

# Allow FetchContent_Populate (we use it to add only inner yoga, not root install)
if(POLICY CMP0169)
  cmake_policy(SET CMP0169 OLD)
endif()

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
  # Populate but do not add root project (avoids root install of include/lib).
  # We only add the inner yoga library so we get yogacore without extra installs.
  FetchContent_GetProperties(yoga)
  if(NOT yoga_POPULATED)
    FetchContent_Populate(yoga)
  endif()
  set(_yoga_root ${yoga_SOURCE_DIR})
  set(yoga_SOURCE_DIR ${_yoga_root}/yoga)
  set(yoga_BUILD_TESTS OFF CACHE BOOL "Build Yoga tests" FORCE)
  add_subdirectory(${yoga_SOURCE_DIR} ${CMAKE_BINARY_DIR}/yoga-build EXCLUDE_FROM_ALL)
endif()

find_package(pybind11 REQUIRED)
pybind11_add_module(yoga src/yoga/yoga.cpp)
target_include_directories(yoga PRIVATE ${yoga_SOURCE_DIR})
target_link_libraries(yoga PRIVATE yogacore)

# Install the compiled extension to the yoga package directory
install(TARGETS yoga DESTINATION "yoga")
