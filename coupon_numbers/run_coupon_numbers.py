import sys

from coupon_numbers import CouponGenerator


if __name__ == "__main__":
    try:
        coupon_num = sys.argv[1]
    except IndexError:
        coupon_num = input('코드 발급 개수를 입력해주세요 (0 ~ 100000): ')

    coupon_generator = CouponGenerator(int(coupon_num))
    coupon_generator = iter(coupon_generator)

    for coupon in coupon_generator:
        print(coupon)
