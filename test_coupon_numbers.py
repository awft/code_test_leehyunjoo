import unittest

from coupon_numbers.coupon_numbers import CouponGenerator


class CouponGeneratorTestCase(unittest.TestCase):

    def setUp(self):
        self.coupon_generator = CouponGenerator(100000)

    def test_initialize(self):
        with self.assertRaises(ValueError):
            CouponGenerator(-1)
        with self.assertRaises(ValueError):
            CouponGenerator('100')
        with self.assertRaises(ValueError):
            CouponGenerator(100001)

        self.assertEqual(self.coupon_generator.num_coupon, 100000)
        self.assertEqual(self.coupon_generator.offset, 10000)

    def test_get_random_number(self):
        self.coupon_generator.offset_area_number = 1
        random_num = self.coupon_generator.get_random_number()

        self.assertEqual(self.coupon_generator.offset_area_number, 2)
        self.assertIsInstance(random_num, int)
        self.assertTrue(20000 <= random_num <= 30000)

    def test_get_unique_number(self):
        self.coupon_generator.offset_area_number = 1
        unique_num = self.coupon_generator.get_unique_number()

        self.assertIsInstance(unique_num, int)
        self.assertTrue(10000 <= unique_num <= 20000)

    def test_generate_coupon_list_쿠폰생성_갯수_및_중복여부_확인(self):
        cg = iter(self.coupon_generator)
        coupon_list = [coupon for coupon in cg]
        coupon_set = set(coupon_list)

        self.assertEqual(len(coupon_list), 100000)
        self.assertEqual(len(coupon_set), 100000)





