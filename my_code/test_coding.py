from .coding import *

def test_convert():
    assert convert('12346') == 12346
    assert convert('-12346') == -12346
    assert convert('-2147483648') == -2147483648
    assert convert('-2147483647') == -2147483647

    assert convert('-012346') == 0
    assert convert('-A') == 0
    assert convert('0') == 0
    assert convert('-') == 0
    assert convert('2147483648') == 0
    assert convert('-2147483649') == 0
    assert convert('4.3') == 0


def test_replace():
    assert replace('123abc', 'abc', '4567') == '1234567'
    assert replace('123', 'abc', '456') == '123'
    assert replace('123abcabc', 'abc', 'X') == '123X'
    assert replace('abcabc123', 'abc', 'X') == 'X123'


def test_get_count_string():
    assert get_count_string('aabbbcccf') == 'a_2_b_3_c_3_f_1'
    assert get_count_string('aaabcccff') == 'a_3_b_1_c_3_f_2'
    assert get_count_string('   ') == ''


def test_is_uniquel():
    assert is_uniquel(['a', 'b', 'c']) == True
    assert is_uniquel(['1', '2', '1']) == False

def test_get_index():
    assert get_index(['', 'a', 'a', '', 'b'], 'a') == 1
    assert get_index(['', 'a', 'a', '', 'b'], 'c') == -1


def test_rotate_word():
    assert rotate_word('pig loves dog') == 'dog loves pig'
    assert rotate_word('I`m a student.') == 'student. a I`m'
