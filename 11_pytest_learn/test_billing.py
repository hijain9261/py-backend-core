from billing import calculate_total
import pytest 

def test_calculate_total_success():
    result = calculate_total(100.0, 15.0)
    assert result == 85.0

def test_calculate_total_zero_discount():
    assert calculate_total(50.0, 0.0) == 50.0

def test_calculate_total_negative_values():
    with pytest.raises(ValueError, match = "Inputs cannot be negative"):
        calculate_total(-10.0, 5.0)

