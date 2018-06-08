#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import interfaz
class TestMyModule(unittest.TestCase):

    def test_interfaz(self):
        self.assertEqual(interfaz.hello_world(), 'Hola es una aplicación de Python!')
if __name__ == "__main__":
    unittest.main()
