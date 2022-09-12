from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    
  return '<h1><center>Demo Flask Application Version1</center></h1>'

if __name__ == "__main__":
  
  app.run(port=5000,host='0.0.0.0')
