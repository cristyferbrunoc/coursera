def maximo(n1, n2, n3):
    return max(n1, n2, n3)


def test_maximo():
    assert maximo(30, 14, 10) == 30
    assert maximo(0, -1, 1) == 1
