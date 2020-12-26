from buzz import generator


def test_sample_single_word():
    letssample = ('foo', 'bar', 'foobar')
    word = generator.sample(letssample)
    assert word in letssample

def test_sample_multiple_words():
    letssample = ('foo', 'bar', 'foobar')
    words = generator.sample(letssample, 2)
    assert len(words) == 2
    assert words[0] in letssample
    assert words[1] in letssample
    assert words[0] is not words[1]

def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
