import unittest

from code_test_leehyunjoo.autocomplete.autocomplete import AutoComplete


class AutoCompleteTestCase(unittest.TestCase):

    def setUp(self):
        self.auto_complete = AutoComplete()
        self.sentence = "동해물과 백두aa산이 마nn르고 닳dd도록, 하a느b님이 보c우bird하사 우리 나라 만세~"

    def test_find_keyword(self):
        self.assertEqual(self.auto_complete.find_keyword(input_string=self.sentence, keyword="ㅂㄷㅅ"), ["백두산이"])
        self.assertEqual(self.auto_complete.find_keyword(input_string=self.sentence, keyword="한"), ["하느님이"])
        self.assertEqual(self.auto_complete.find_keyword(input_string=self.sentence, keyword="ㅁ"), ["마르고", "만세"])
        self.assertEqual(self.auto_complete.find_keyword(input_string=self.sentence, keyword="록한"), [])

    def test_is_korean_char(self):
        self.assertTrue(self.auto_complete.is_korean_char("고"))
        self.assertFalse(self.auto_complete.is_korean_char("g"))

    def test_break_word_into_letter_단어의_초성_중성_종성_확인(self):
        self.assertEqual(self.auto_complete.break_word_into_letter("고양이"), "ㄱㅗㅇㅑㅇㅇㅣ")
        self.assertNotEqual(self.auto_complete.break_word_into_letter("고양이"), "ㄱㅗㅇㅑㅇ")

    def test_separate_word_단어의_초성_자음만_확인(self):
        self.assertNotEqual(self.auto_complete.break_word_into_letter("고양이", cho_only=True), "ㄱㅗㅇㅑㅇㅇㅣ")
        self.assertEqual(self.auto_complete.break_word_into_letter("고양이", cho_only=True), "ㄱㅇㅇ")

    def test_check_cho_only(self):
        self.assertTrue(self.auto_complete.check_cho_only("ㄱㅇㅇ"))
        self.assertFalse(self.auto_complete.check_cho_only("ㄱㅗㅇㅑㅇㅇㅣ"))
