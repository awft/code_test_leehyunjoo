import random


class CouponGenerator(object):

    def __init__(self, num_coupon):
        if not isinstance(num_coupon, int) or num_coupon < 0 or num_coupon > 100000:
            raise ValueError('0 ~ 100000 사이의 숫자값을 입력해주세요')
        self.num_coupon = num_coupon
        self.li = [False for _ in range(100001)]
        self.offset = 10000
        self.offset_area_number = -1
        self.toggle = True


    def get_offset_area_number(self):
        """랜덤 탐색을 위한 offset_area_number 확인

        Returns:
            int: 0 ~ 9

        """
        self.offset_area_number += 1
        if self.offset_area_number > 9:
            self.offset_area_number = 0
        return self.offset_area_number


    def get_random_number(self):
        """랜덤 쿠폰번호 생성

        Returns:
            int: 쿠폰번호

        """
        slot = self.get_offset_area_number()
        random_num = random.randint(self.offset * slot, self.offset * (slot + 1))
        return random_num


    def is_valid(self, coupon_num):
        """쿠폰번호의 중복여부 확인

        Args:
            coupon_num (int): 쿠폰번호

        Returns:
            bool: 중복여부

        """
        if not self.li[coupon_num]:
            return True
        else:
            return False


    def get_unique_number(self):
        """고유한 쿠폰번호 생성

        Returns:
            int: 쿠폰번호

        """
        start_idx = self.offset * self.offset_area_number
        end_idx = self.offset * (self.offset_area_number + 1)
        target_li = self.li[start_idx:end_idx]

        if self.toggle:
            relative_idx = target_li.index(False)
        else:
            relative_idx = len(target_li) - target_li[::-1].index(False) - 1

        self.toggle = not self.toggle

        return start_idx + relative_idx


    def __iter__(self):
        for _ in range(self.num_coupon):

            # 랜덤 쿠폰번호 생성
            coupon_num = self.get_random_number()

            # 쿠폰번호 중복시 고유한 쿠폰번호 재생성
            if not self.is_valid(coupon_num):
                try:
                    coupon_num = self.get_unique_number()
                except ValueError:
                    continue

            self.li[coupon_num] = True
            ret = str(coupon_num).rjust(6, '0')

            yield ret
