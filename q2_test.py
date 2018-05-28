import q2_code

def test_q2_code_1():
    assert(q2_code.power(5, 1) == 5)

def test_q2_code_2():
    assert(q2_code.power(5, 2) == 25)

def test_q2_code_3():
    assert(q2_code.power(10, 4) == 10000)

def test_q2_code_4():
    assert(q2_code.power(0, 0) == 1)

def test_q2_code_5():
    assert(q2_code.power(1, 0) == 1)

def test_q2_power_6():
    assert(q2_code.power(2, 8) == 256)

