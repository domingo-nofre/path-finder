# Project Title

Path finding for knights

## Motivation

This simple project contains a program that finds the shortest path for a knight to take between two points
on a standard 8x8 chessboard.

## Installation

In the requirements.txt file you will find all necessary dependencies

## Usage

Execute the following command inside the project pathFinder folder
python pathFinder.py

The program reads instructions from standard input (stdin).
Instructions are lines (separated by newlines) in the following format:

D4 G7

D4 D5


The first of the space-separated values is the knight's starting position, the second is the knight's target position.
For each line in the input, the program prints (to standard out) the shortest path it found.
So for the example above, it should print e.g.:

D4 F5 G7

D4 E2 F4 D5


## Running the tests

For running the functional tests you only need to execute the following sentence
python runner.py



