import q1_code

def test_q1_code_1():
    assert(q1_code.swap_max_min([1, 2, 3, 4]) == [4, 2, 3, 1])

def test_q1_code_2():
    assert(q1_code.swap_max_min([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3]) == [7, 2, 3, 4, 5, 6, 1, 6, 5, 4, 3])


    
