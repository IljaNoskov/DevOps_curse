import pytest

from calc import calc_f

@pytest.mark.parametrize(
    ('string', 'answer'),
    [
        ('2', 2),
        ('44 + 22', 66),
        ('10 / 5', 2),
        ('20 * 4', 80)
    ]
)
def test_calc_f(string, answer):
    assert calc_f(string) == answer


def test_calc_f_errors():
    str1 = '23,5 + 54'
    str2 = 'just a text'
    with pytest.raises(TypeError):
        calc_f(str1)

    with pytest.raises(SyntaxError):
        calc_f(str2)
