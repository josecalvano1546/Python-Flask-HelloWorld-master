from flask import Flask
app = Flask name__)

@app.route('/')
def hello_world():
  return 'Hola es la aplicación de Python!'

if __name__ == '__main__':
  app.run()
