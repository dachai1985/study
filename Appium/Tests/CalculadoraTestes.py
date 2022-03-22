import unittest

import sys
import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
print('Import path' + BASE)

from pageobjects.Calc import Calculator
from webdriver.Webdriver import Driver


class CalculadoraTestes(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_soma(self):
        print('1111111111')
        calculadora = Calculator(self.driver)
        calculadora.somando(1, 2)

    def test_multiplicacao(self):
        print('22222222222')
        calculadora = Calculator(self.driver)
        calculadora.multiplicando(2, 3)

    def tearDown(self):
        self.driver.instance.quit()

if __name__ == '__main__':
    #unittest.main()
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(CalculadoraTestes('test_soma'))
    suite.addTest(CalculadoraTestes('test_multiplicacao'))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)