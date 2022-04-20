#!/bin/bash

make
./a.out < input.txt > output.txt
python3 error_count.py 
