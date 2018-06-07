#!/usr/bin/env python
# -*- coding: utf-8 -*-
import clasehola
from flask import Flask
app = Flask(__name__)

@app.route('/')
    clasehola.hello_world()
if __name__ == '__main__':
  app.run()
