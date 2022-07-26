cmake_minimum_required(VERSION 3.5.1)

project(04_assign)

# in case you decide to use gcc
IF(CMAKE_COMPILER_IS_GNUCC)
   SET(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} "--std=c++14 -pedantic -Wall -Wextra")
ENDIF(CMAKE_COMPILER_IS_GNUCC)

# make Visual studio and Xcode output the binaries in the same build directory
SET( CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG "${CMAKE_BINARY_DIR}")
SET( CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE "${CMAKE_BINARY_DIR}")

set(binary scrabble)

add_executable(${binary} ${binary}.cpp main.cpp)


target_compile_features(${binary} PRIVATE cxx_decltype_auto cxx_auto_type)


enable_testing()

# set the binary to bes tested in each of the tests below. 
set(test_cmd ${CMAKE_BINARY_DIR}/${binary}${CMAKE_EXECUTABLE_SUFFIX})
set(tester   ${CMAKE_CURRENT_SOURCE_DIR}/tester-scrabble.cmake)
set(loc ${CMAKE_CURRENT_SOURCE_DIR})


add_test(
    NAME test01 
    COMMAND ${CMAKE_COMMAND} -DEXE=${test_cmd} -D ID=01 -DLOC=${loc} -P ${tester}
)

add_test(
    NAME test02
    COMMAND ${CMAKE_COMMAND} -DEXE=${test_cmd} -D ID=02 -DLOC=${loc} -P ${tester}
)

add_test(
    NAME test03 
    COMMAND ${CMAKE_COMMAND} -DEXE=${test_cmd} -D ID=03 -DLOC=${loc} -P ${tester}
)

add_test(
    NAME test04
    COMMAND ${CMAKE_COMMAND} -DEXE=${test_cmd} -D ID=04 -DLOC=${loc} -P ${tester}
)

add_test(
    NAME test05
    COMMAND ${CMAKE_COMMAND} -DEXE=${test_cmd} -D ID=05 -DLOC=${loc} -P ${tester}
)
add_test(
    NAME test06
    COMMAND ${CMAKE_COMMAND} -DEXE=${test_cmd} -D ID=06 -DLOC=${loc} -P ${tester}
)
