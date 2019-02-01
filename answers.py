# -*- coding: utf-8 -*-

# This is the answers file for the CMPSC 473 - Spring 2019 - Project #1
# Answers data structures
# DO NOT MODIFY THESE VARIABLES HERE
wordy = {
    "1b": None,
    "1d": None,
    "1e": None,
    "2b": None,
    "2c": None,
    "2d": None,
    "2e": None,
    "3b": None,
    "3c": None,
    "4a": None,
    "4bi": None,
    "4bii": None,
    "4biii": None,
    "4biv": None,
    "4bv": None,
    "4bvi": None
}
numerical = {
    "1a": None,
    "1c": None,
    "2ai32": None,
    "2aii32": None,
    "2aiii32": None,
    "2ai64": None,
    "2aii64": None,
    "2aiii64": None,
    "3ai32": None,
    "3aii32": None,
    "3aiii32": None,
    "3ai64": None,
    "3aii64": None,
    "3aiii64": None,
}

###########################################################
# Answer Section
# You may edit the values of variables below
###########################################################

# FILL OUT YOUR ID AND ANSWERS BELOW
# PSU ID (e.g. xyz1234)
ID = "pjs5528"

###########################################################
# (1) Stack, heap, and system calls
###########################################################

# (1.a) What is the size of the proces stack when it is
#   waiting for user input?
#   Enter your answer in bytes.
numerical["1a"] = 86016

# (1.b) Which addresses are for the local variables and
#   which ones are for the dynamically allocated variables?
#   What are the directions in which the stack and the heap
#   grow on your system?
wordy["1b"] = """The stack (7ffe39e1a000 - 7ffe39e2f000) is for local variables and grows from higher to lower addresses.
The heap (02649000 - 026c7000) is for dynamically allocated variables and grows from lower to higher addresses.""""

# (1.c) What is the size of the process heap when it
#   is waiting for user input?
#   Enter your answer in bytes.
numerical["1c"] = 516096

# (1.d) What are the address limits of the stack and the heap?
wordy["1d"] = """"Stack limits: 7ffe39e1a000 - 7ffe39e2f000.
Heap limits: 02649000 - 026c7000.
This is consistent with the results from prog1.""""

# (1.e) For each unique system call, write in your own words
#   (just one sentence should do) what purpose this system
#   call serves for this program.
wordy["1e"] = """execve(): executes the program.
brk(): .
mmap(): .
access(): .
open(): .
fstat(): .
close(): .
read(): .
mprotect(): .
arch_prctl(): .
munmap(): .
write(): ."""

###########################################################
# (2) Debugging Refresher
###########################################################

# (2.a) Observe and report the differences in the following
#   for the 32-bit and 64-bit executables

# (2.a.i.32) size of compiled code (32-bit)
#   Enter your answer in bytes.
# Size of text section
numerical["2ai32"] = 1419

# (2.a.ii.32) size of code during run time (32-bit)
#   Enter your answer in bytes.
numerical["2aii32"] = """Size of ~/473/lab1-pjs5528/part2/prog2: 4096 bytes.
Found using pmap PID while executing program in gdb in another terminal window."""

# (2.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["2aiii32"] = """Size of linked libraries found using pmap PID:
124K + 4K +4K + 1604K + 8K + 4K = 1748K -> (x1024) = 1789952 bytes"""

# (2.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
# Size of text section
numerical["2ai64"] = 1651

# (2.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["2aii64"] = """Size of ~/473/lab1-pjs5528/part2/prog2: 4096 bytes.
Found using pmap PID while executing program in gdb in another terminal window."""

# (2.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["2aiii64"] = """Size of linked libraries found using pmap PID:
128K + 4K + 4K + 1580K + 2044K + 16K + 8K = 3784K -> (x 1024) = 3874816 bytes"""

# (2.b) Use gdb to find the program statement that
#   caused the error
wordy["2b"] = """The statement in main() that causes this segmentation fault is:
   <+37>: callq 0x4005a4 <allocate>.
Found using 'disas main' after executing prog2 in gdb"""

# (2.c) Explain the cause of this error.
wordy["2c"] = """Max stack size using cat /proc/PID/limits: 10485760 bytes.
The difference between the largest stack address and the smallest stack address 
before the Seg fault occurs is: 10800432 bytes.
The Stack Addresses grew too large and caused a segmentation fault."""

# (2.d) Examine individual frames in the stack to find each
#   frame's size. Estimate the number of invocations of the
#   recursive function that should be possible. How many
#   invocations occur when you actually execute the program?
wordy["2d"] = """Each frame has a size of 1200048 bytes.
10485760 / 1200048 = 8.74.
That means 8 invocations of allocate() should be possible.
10 invocations occured when I actually executed the program."""

# (2.e) What are the contents of a frame in general?
#   Which of these are present in a frame corresponding
#   to an invocation of the recursive function and
#   what are their sizes?
wordy["2e"] = """Contents of the frame found using info frame #: 
Instruction Pointer, caller of frame (address), source language, 
argument list, address of local variables, previous frame's stack pointer, 
and saved registers (rbp and rip)."""

###########################################################
# (3) More debugging
###########################################################

# (3.a) Observe and report the differences in the following
#   for the 32-bit and 64-bit executables:

# (3.a.i.32) size of compiled code (32-bit)
#   Enter your answer in bytes.
numerical["3ai32"] = None

# (3.a.ii.32) size of code during run time (32-bit)
#   Enter your answer in bytes.
numerical["3aii32"] = None

# (3.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["3aiii32"] = None

# (3.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
numerical["3ai64"] = None

# (3.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["3aii64"] = None

# (3.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["3aiii64"] = None

# (3.b) Use valgrind to find the cause of the error
#   including the program statement causing it
wordy["3b"] = None

# (3.c) How is this error different than the one for prog2?
wordy["3c"] = None

###########################################################
# (4) And some more
###########################################################

# (4.a) Describe the cause and nature of these errors.
#   How would you fix them?
wordy["4a"] = None

# (4.b) Modify the program to use getrusage for measuring the following:

# (4.b.i) user CPU time used
wordy["4bi"] = None

# (4.b.ii) system CPU time used
#   What is the difference between (i) and (ii)?
wordy["4bii"] = None

# (4.b.iii) maximum resident set size
#   what is this?
wordy["4biii"] = None

# (4.b.iv) signals received
#   Who may have sent these?
wordy["4biv"] = None

# (4.b.v) voluntary context switches
wordy["4bv"] = None

# (4.b.vi) involuntary context switches
#   what is the difference between (v) and (vi)?
wordy["4bvi"] = None

###########################################################
# Sanity Check
# DO NOT MODIFY ANYTHING BELOW HERE
###########################################################
if ID == "":
    print("Please fill out your student ID in the variable ID")
for key in numerical:
    if type(numerical[key]) is not int:
        print("Type error of answer %s (should be a numerical value)" % key)
for key in wordy:
    if type(wordy[key]) is not str:
        print("Type error of answer %s (should be a string)" % key)
