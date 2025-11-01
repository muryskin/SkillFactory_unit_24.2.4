import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        """Проверка правильного сложения"""
        assert self.calc.adding(self,1,1)==2

    def test_adding_unsuccess(self):
        """Проверка неправильного сложения"""
        assert self.calc.adding(self,1,1)==3

    def test_zero_division(self):
        """Проверка деления на ноль"""
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1,0)

    def test_multiply_success(self):
        """Проверка правильного умножения"""
        assert self.calc.multiply(self,2,3)==6

    def test_division_unsuccess(self):
        """Проверка неправильного умножения"""
        assert self.calc.division(self,6,3)==2

    def test_subtract_success(self):
        """Проверка правильного вычитания"""
        assert self.calc.subtraction(self,10,4)==6

    def test_subtract_unsuccess(self):
        """Проверка неправильного вычитания"""
        assert self.calc.subtraction(self,10,5)==6

    def teardown(self):
        print("Выполнение метода Teardown")
