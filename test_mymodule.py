#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import mymodule
class TestMyModule(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(mymodule.sum(5, 6), 12)
if __name__ == "__main__":
    unittest.main()
