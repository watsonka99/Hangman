from words import Word


def test_unknown_word():
    word1 = Word("a")
    assert word1.unknown_word == ['*']
    word2 = Word("mississippi")
    assert word2.unknown_word == ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    word3 = Word("engine")
    assert word3.unknown_word == ['*','*','*','*','*','*']


def test_guess_letter():
    word2 = Word("mississippi")
    word2.guess_letter('m')
    assert word2.unknown_word == ['m', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    word2.guess_letter('i')
    assert word2.unknown_word == ['m', 'i', '*', '*', 'i', '*', '*', 'i', '*', '*', 'i']
    word2.guess_letter('p')
    assert word2.unknown_word == ['m', 'i', '*', '*', 'i', '*', '*', 'i', 'p', 'p', 'i']
    word2.guess_letter('s')
    assert word2.unknown_word == ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']


def test_check_win():
    word2 = Word("mississippi")
    word2.guess_letter('m')
    assert word2.win_check() == False
    word2.guess_letter('i')
    assert word2.win_check() == False
    word2.guess_letter('p')
    assert word2.win_check() == False
    word2.guess_letter('s')
    assert word2.win_check() == True
