#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import clasehola
class TestMyModule(unittest.TestCase):

    def test_interfaz(self):
        self.assertEqual(clasehola.hello_world(), 'Hola es una aplicación de Python!')
if __name__ == "__main__":
    unittest.main()
