from math_func_testing import fib , next_collatz_element

def test_fib_basic_initial():
    assert fib(0)==0
    assert fib(1)==1

#you have to install pytest
#pip install pytest
#week 1 day 5 video , timing: 4:55:20
#how to run -> go to terminal -> type -> pytest .\math_func_testing_client.py

def test_fib_2():
    assert fib(2)==1


def test_fib_3():
    assert fib(3)==2

def test_collatz_1():
    assert next_collatz_element(1)==4
def test_collatz_2():
    assert next_collatz_element(5)==16

#there is another to test pip install pytest-cov
# pytest coverage
# go to terminal 
# write-> coverage run -m pytest .\math_func_testing_client.py -> enter
#it will generate a coverage file in your folder


#there is another to test pip install pytest-cov
# pytest coverage
# go to terminal 
# write-> coverage html --include=.\math_func_testing_client.py -> enter
#it will create coverage html file in curreent folder
# open in browser to check


#there is another to test pip install pytest-cov
# pytest coverage
# go to terminal 
# write-> coverage html --include=.\math_func_testing.py -> enter
#it will create coverage html file in curreent folder
# open in browser to check
