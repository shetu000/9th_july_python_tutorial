from automation_testing-via_code import greet

def test_greet_fname_lname():
    assert greet('shetu','das')
def test_greet_fname():
    assert greet('shetu')


if __name__=='__main__': #this is to run those two functions
    test_greet_fname_lname()
    test_greet_fname()