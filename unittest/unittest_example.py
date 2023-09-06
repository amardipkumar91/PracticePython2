import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()

class Calculator(object):
    # @staticmethod
    def sum(self, a,b):
        # import pdb;pdb.set_trace()
        if a is None or b is None:
            raise ValueError
        return a + b
    
    def sub(self, a,b):
        if a is None or b is None:
            raise ValueError
        return a - b


class TestCalculatorSum(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
    def test_sum_equal(self):  
        self.assertEqual(9, self.calc.sum(4,5))
    
    def test_sum_non(self):
        self.assertRaises(ValueError, self.calc.sum, None, 5)

class TestCalculatorSub(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
    def test_sub_equal(self):  
        self.assertEqual(1, self.calc.sub(5,4))
    
    def test_sub_non(self):
        self.assertRaises(ValueError, self.calc.sub, None, 5)


#------------------------ Test Suite---------------------------
# def suite():
#     test_suite = unittest.TestSuite()
#     test_suite.addTest(unittest.makeSuite(TestCalculatorSub))
#     return test_suite

# mySuit=suite()
# runner=unittest.TextTestRunner()
# runner.run(mySuit)

#----------------- Multiple Class In one Test Suite-------
def suite():
    test_need_to_run = [TestCalculatorSum, TestCalculatorSub]
    test_suite = unittest.TestLoader()
    suite_list = []
    for i in test_need_to_run:
        suite = test_suite.loadTestsFromTestCase(i)
        suite_list.append(suite)
    big_suite=unittest.TestSuite(suite_list)
    return big_suite

mySuit = suite()
runner=unittest.TextTestRunner()
results = runner.run(mySuit)
