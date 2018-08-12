import unittest

from autocomplete.autocomplete import AutoComplete
from read_numbers.read_numbers import read_numbers


class AutoCompleteTestCase(unittest.TestCase):

    def setUp(self):
        self.auto_complete = AutoComplete()
        self.sentence = "오늘날 대부분의 프로그래머는 고생하며 얻은 귀중한 경험과 지식을 공유하고, " \
                        "남의 고생을 덜어주고, 얻기 이전에 가치 있는 것을 남들에게 나누어 주려 노력하는 이들에게 빚지고 있다"

    def test_find_keyword(self):
        self.assertEqual(self.auto_complete.find_keyword(sentence=self.sentence, keyword="ㅍㄹㄱ"), ["프로그래머는"])
        self.assertEqual(self.auto_complete.find_keyword(sentence=self.sentence, keyword="갗"), ["가치"])
        self.assertEqual(self.auto_complete.find_keyword(sentence=self.sentence, keyword="ㅈ"), ["지식을", "주려"])
        self.assertEqual(self.auto_complete.find_keyword(sentence=self.sentence, keyword="는곳"), [])

    def test_is_korean_char(self):
        self.assertTrue(self.auto_complete.is_korean_char("고"))
        self.assertFalse(self.auto_complete.is_korean_char("g"))

    def test_separate_word_단어의_초성_중성_종성_확인(self):
        self.assertEqual(self.auto_complete.separate_word("고양이"), "ㄱㅗㅇㅑㅇㅇㅣ")
        self.assertNotEqual(self.auto_complete.separate_word("고양이"), "ㄱㅗㅇㅑㅇ")

    def test_separate_word_단어의_초성_자음만_확인(self):
        self.assertNotEqual(self.auto_complete.separate_word("고양이", cho_only=True), "ㄱㅗㅇㅑㅇㅇㅣ")
        self.assertEqual(self.auto_complete.separate_word("고양이", cho_only=True), "ㄱㅇㅇ")

    def test_check_cho_only(self):
        self.assertTrue(self.auto_complete.check_cho_only("ㄱㅇㅇ"))
        self.assertFalse(self.auto_complete.check_cho_only("ㄱㅗㅇㅑㅇㅇㅣ"))
