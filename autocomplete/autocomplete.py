import re
import unicodedata


class AutoComplete(object):

    CHO = (
        'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
        'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    )

    JOONG = (
        'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
        'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
    )

    JONG = (
        '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ',
        'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
        'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    )

    JAMO = CHO + JOONG + JONG[1:]


    def __init__(self):
        self.sentence = None
        self.keyword = None


    def is_korean_char(self, ch):
        """한국어 여부 확인 (http://www.unicode.org/reports/tr44/#GC_Values_Table)"""

        category = unicodedata.category
        if category(ch)[0:2] == 'Lo':
            if 'HANGUL' in unicodedata.name(ch):
                return True
        return False


    def separate_letter(self, ch, cho_only=False):
        """한글 한글자를 초성, 중성 종성으로 분리하여 리턴

        Args:
            ch (str): 길이가 1인 한글 문자 (ex. 양)
            cho_only (bool): 자음 초성만 확인할지 여부

        Returns:
            tuple: 초성 혹은 초성, 중성 종성으로 분리된 문자열 튜플 (ex. ('ㅇ', 'ㅑ', 'ㅇ'))

        """
        first_hangul_unicode = 0xAC00
        unicode_idx = ord(ch) - first_hangul_unicode

        jong_idx = unicode_idx % 28
        joong_idx = ((unicode_idx - jong_idx) // 28) % 21
        cho_idx = ((unicode_idx - jong_idx) // 28) // 21

        if cho_only:
            return self.CHO[cho_idx]

        return self.CHO[cho_idx], self.JOONG[joong_idx], self.JONG[jong_idx]


    def break_word_into_letter(self, word, cho_only=False):
        """한글 단어를 초성, 중성, 종성으로 분리하여 리턴

        Args:
            word (str): 한글 단어 (ex. 고양이)
            cho_only (bool): 자음 초성만 확인할지 여부

        Returns:
            str: 초성 혹은 초성, 중성 종성으로 분리된 문자열 (ex. 'ㄱㅗㅇㅑㅇㅇㅣ')

        """
        result = ''

        for ch in list(word):
            if self.is_korean_char(ch):
                if ch in self.JAMO:
                    result = result + ch
                else:
                    result = result + ''.join(self.separate_letter(ch, cho_only))

        return result


    def break_sentence_into_words(self):
        """문장을 한글 단어로 분리하여 리스트로 리턴

        Examples: "동해물과 백두aa산이" => ["동해물과", "백두산이"]

        """
        word_li = []
        for word in self.sentence.split(' '):
            word_li.append(re.sub(r'[^ㄱ-힣]', '', word))

        return word_li


    def check_cho_only(self, separated_char):
        """초성 자음으로만 이루여졌는지 여부 확인"""

        if all(k in self.CHO for k in separated_char):
            return True
        else:
            return False


    def find_keyword(self, input_string, keyword):
        """주어진 문자열에서 keyword 단어를 확인

        Args:
            input_string (str): 검색 대상이 되는 문자열
            keyword (str): 검색어

        Returns:
            list: 검색결과 리스트

        """
        self.sentence = input_string
        self.keyword = keyword
        result = []

        # keyword 자소분리
        keyword_letter = self.break_word_into_letter(self.keyword)

        # 초성 자음검색 여부 확인
        cho_only_option = self.check_cho_only(keyword_letter)

        # 검색대상 문자열 자소분리
        word_li = self.break_sentence_into_words()
        word_letter_list = []

        for word in word_li:
            word_letter = self.break_word_into_letter(word, cho_only=cho_only_option)
            word_letter_list.append(word_letter)

        # 검색
        for idx, word_letter in enumerate(word_letter_list):
            if word_letter.startswith(keyword_letter):
                result.append(word_li[idx])

        return result
