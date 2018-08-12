import re
import unicodedata


class AutoComplete(object):

    CHO = (
        u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ',
        u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ'
    )

    JOONG = (
        u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ',
        u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ'
    )

    JONG = (
        u'', u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ',
        u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ',
        u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ'
    )

    JAMO = CHO + JOONG + JONG[1:]


    def is_korean_char(self, ch):
        """한국어 여부 확인 (http://www.unicode.org/reports/tr44/#GC_Values_Table)"""

        category = unicodedata.category
        if category(ch)[0:2] == 'Lo':
            if 'HANGUL' in unicodedata.name(ch):
                return True
        return False


    def separate_char(self, ch, cho_only=False):
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


    def separate_word(self, word, cho_only=False):
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
                    result = result + ''.join(self.separate_char(ch, cho_only))

        return result


    def check_cho_only(self, separated_char):
        """초성 자음으로만 이루여졌는지 여부 확인"""

        if all(k in self.CHO for k in separated_char):
            return True
        else:
            return False


    def find_keyword(self, sentence, keyword):
        """주어진 문자열에서 keyword 단어를 확인

        Args:
            sentence (str): 검색 대상이 되는 문자열
            keyword (str): 검색어

        Returns:
            list: 검색결과 리스트

        """

        result = []
        separated_word_li = []
        word_li = sentence.split(' ')

        # keyword 자소분리
        separated_keyword = self.separate_word(keyword)

        # 초성 자음검색 여부 확인
        cho_only_option = self.check_cho_only(separated_keyword)

        for word in word_li:
            separated_word = self.separate_word(word, cho_only=cho_only_option)
            separated_word_li.append(separated_word)

        # 검색
        for idx, word in enumerate(separated_word_li):
            if word.startswith(separated_keyword):
                target = re.sub('[^\w]+', '', word_li[idx])
                result.append(target)

        return result
