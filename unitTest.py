import unittest
class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()



#program 2
import unittest
class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertTrue(False)

if __name__=="__main__":
    unittest.main()


#program 3

#program 2
import unittest
class SimpleTest(unittest.TestCase):
    def test(self):
        i=10
        j=20
        if(i==0 or j==0):
            self.assertFalse(True)

        
if __name__=="__main__":
    unittest.main()