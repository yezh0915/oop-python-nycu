import pytest
import lec3_strings_algos as lec3
import math


def test_cube_root():
    assert lec3.cube_root(27)    == 3
    assert lec3.cube_root(125)   == 5
    assert lec3.cube_root(1331)  == 11
    assert lec3.cube_root(64)   == 4
    assert lec3.cube_root(512)  == 8
    assert lec3.cube_root(1000)  == 10
    assert lec3.cube_root(-27)   == None  ## The function do not allow negative numbers


def test_approximate_root():
    assert lec3.approximate_root(125,  0.01) == (500,  4.999999999999938)
    assert lec3.approximate_root(0.7,  0.1)  == (70,  -1)
    assert lec3.approximate_root(0,    0.1)  == (0,   0.0)
    assert lec3.approximate_root(125,  0.001) == (500,  4.999999999999938)
    assert lec3.approximate_root(1331, 0.01) == (1100, 10.99999999999981)


#####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
#####################
def while_to_for():
    an_letters = "aefhilmnorsxAEFHILMNORSX"
    word = input("I will cheer for you! Enter a word: ")
    times = int(input("Enthusiasm level (1-10): "))

    i = 0
    for i in range(len(word)):
        char = word[i]
        if char in an_letters:
            print("Give me an " + char + "! " + char)
        else:
            print("Give me a  " + char + "! " + char)
    print("What does that spell?")
    for i in range(times):
        print(word, "!!!")

