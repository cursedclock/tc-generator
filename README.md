# T-C Generator
---
A simple script that makes test cases for coding excersizes.
This tool should work on any platform That can run python 3.

## To use:
Simple set the path to solution executable and the number of test cases you want, then define generate_input to return a random input string every time it is called in config.py. Run tc-generator.py and the script will write each input in the in directory and and it's corresponding output in the out directory.
+ sol should be the path to an executable that accepts and returns data through stdin/out.
+ make sure generate_input should returns a string and not any other data type.