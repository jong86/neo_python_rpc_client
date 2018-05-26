from neorpc.Client import RPCClient
client = RPCClient()

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/validate_address")
def validateAddress():
  address = request.args['address']
  return jsonify(client.validate_addr(address))

if __name__ == "__main__":
  app.run(port=7000)
