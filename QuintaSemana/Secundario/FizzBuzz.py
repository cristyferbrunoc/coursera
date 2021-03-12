def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 != 0:
        return "Fizz"
    elif numero % 5 == 0 and numero % 3 != 0:
        return 'Buzz'
    elif numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'
    else:
        return numero


def test_fizzbuzz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(4) == 4


