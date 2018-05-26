from neorpc.Client import RPCClient
client = RPCClient()
blockchain_height = client.get_height()
print(blockchain_height)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
    