import os
from flask import Flask

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/")
def hello():
    return "Hello from Python!"

# launch
if __name__ == "__main__":
    port = os.getenv('PORT', '5000') 
    if name == "main": app.run(host='0.0.0.0', port=int(port))