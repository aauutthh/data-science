# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.9

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/almac/workspace/sfu-fall2017-assignments/cmpt479/callgraph-profiler-template

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild

# Include any dependencies generated for this target.
include lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/depend.make

# Include the progress variables for this target.
include lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/progress.make

# Include the compile flags for this target's objects.
include lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/flags.make

lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o: lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/flags.make
lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o: /home/almac/workspace/sfu-fall2017-assignments/cmpt479/callgraph-profiler-template/lib/callgraph-profiler-inst/ProfilingInstrumentationPass.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o"
	cd /home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild/lib/callgraph-profiler-inst && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o -c /home/almac/workspace/sfu-fall2017-assignments/cmpt479/callgraph-profiler-template/lib/callgraph-profiler-inst/ProfilingInstrumentationPass.cpp

lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.i"
	cd /home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild/lib/callgraph-profiler-inst && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/almac/workspace/sfu-fall2017-assignments/cmpt479/callgraph-profiler-template/lib/callgraph-profiler-inst/ProfilingInstrumentationPass.cpp > CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.i

lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.s"
	cd /home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild/lib/callgraph-profiler-inst && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/almac/workspace/sfu-fall2017-assignments/cmpt479/callgraph-profiler-template/lib/callgraph-profiler-inst/ProfilingInstrumentationPass.cpp -o CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.s

lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o.requires:

.PHONY : lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o.requires

lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o.provides: lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o.requires
	$(MAKE) -f lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/build.make lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o.provides.build
.PHONY : lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o.provides

lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o.provides.build: lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o


# Object files for target callgraph-profiler-inst
callgraph__profiler__inst_OBJECTS = \
"CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o"

# External object files for target callgraph-profiler-inst
callgraph__profiler__inst_EXTERNAL_OBJECTS =

lib/libcallgraph-profiler-inst.a: lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o
lib/libcallgraph-profiler-inst.a: lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/build.make
lib/libcallgraph-profiler-inst.a: lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library ../libcallgraph-profiler-inst.a"
	cd /home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild/lib/callgraph-profiler-inst && $(CMAKE_COMMAND) -P CMakeFiles/callgraph-profiler-inst.dir/cmake_clean_target.cmake
	cd /home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild/lib/callgraph-profiler-inst && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/callgraph-profiler-inst.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/build: lib/libcallgraph-profiler-inst.a

.PHONY : lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/build

lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/requires: lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/ProfilingInstrumentationPass.cpp.o.requires

.PHONY : lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/requires

lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/clean:
	cd /home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild/lib/callgraph-profiler-inst && $(CMAKE_COMMAND) -P CMakeFiles/callgraph-profiler-inst.dir/cmake_clean.cmake
.PHONY : lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/clean

lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/depend:
	cd /home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/almac/workspace/sfu-fall2017-assignments/cmpt479/callgraph-profiler-template /home/almac/workspace/sfu-fall2017-assignments/cmpt479/callgraph-profiler-template/lib/callgraph-profiler-inst /home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild /home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild/lib/callgraph-profiler-inst /home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild/lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/callgraph-profiler-inst/CMakeFiles/callgraph-profiler-inst.dir/depend

