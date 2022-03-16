import unittest

from main import single_letters


class SingleLetterTest(unittest.TestCase):
    def test(self):
        for k, v in {
            "a": "a",
            "raaaamen": "ramen",
            "sraaamennnn": "sramen",
        }.items():
            self.assertEqual(single_letters(k), v)


if __name__ == "__main__":
    unittest.main()
