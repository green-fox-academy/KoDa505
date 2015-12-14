import unittest
from ball import Ball

class TestBall(unittest.TestCase):
    def test_exists(self):
        ball = Ball(40, 50, 10)

unittest.main()
