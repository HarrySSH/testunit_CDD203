import utils

def test_total():
    actual_value = utils.total(3, 5)
    expected_value = 8
    assert actual_value == expected_value

def test_multiply():
    actual_value = utils.multiply(3, 5)
    expected_value = 15
    assert actual_value == expected_value
