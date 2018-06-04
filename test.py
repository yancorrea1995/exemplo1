import pytest
from principal import multiplicar

def test_multiplicar():
	assert multiplicar(2,4) == 6
	assert multiplicar(3,3) == 9
	assert multiplicar(3,4) == 12
	assert multiplicar(7,5) == 35


