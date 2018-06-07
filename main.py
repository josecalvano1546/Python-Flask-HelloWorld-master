#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
    def hello_world():
      return 'Hola es una aplicación de Pythones!'
if __name__ == '__main__':
  app.run()
