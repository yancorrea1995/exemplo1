import pytest
from principal import multiplicar

def test_multiplicar():
	assert multiplicar(2,4) == 8
	assert multiplicar(3,3) == 10
	assert multiplicar(3,4) == 15
	assert multiplicar(7,5) == 35


