from src.P1_10.P1_10_Act1 import mayor
import pytest

def test_mayor():
    assert mayor(5, 2) == 5
    assert mayor(5, 5) == 0
    assert mayor(2, 9) == 9
    
@pytest.mark.parametrize(
    "num0, num01, expected",
    [
        (10, 5, 10),
        (4, 4, 0),
        (7, 5, 7),
        (1, 5, 5)
    ]
)
def test_mayor_parametrize(num0, num01, expected):
    assert mayor(num0, num01) == expected
    
    
    
    
