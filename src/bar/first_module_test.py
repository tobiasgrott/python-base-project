from src.bar.first_module import example, example2


def test_example():
    output = example()
    assert output == "Hi from bar"


def test_example2():
    output = example2()
    assert output == "Hi again, this is from bar by the way!"
