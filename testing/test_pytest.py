from python.calc import Calc
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.run(order=-1)
    def test_add(self):
        assert self.calc.add(1, 2) == 3

    def test_div(self):
        assert self.calc.div(1, 2) == 0.5

    def test_params(self):
        data = (1, 2)
        self.calc.add2(data)
        self.calc.add(*data)

    @pytest.mark.run(order=1)
    def test_zadd(self):
        assert self.calc.add(1, 2) == 3

    def test_1add(self):
        assert self.calc.add(1, 2) == 3

    @pytest.mark.demo
    @pytest.mark.parametrize("a,b", [
        (1, 2),
        (2, 3),
        (3, 4)
    ])
    def test_parmas1(self, a, b):
        data = (a, b)
        self.calc.add2(data)
