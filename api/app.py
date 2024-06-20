from flask import Flask, request, send_file
import math
from io import BytesIO
import base64
import sys

sys.set_int_max_str_digits(0)

BYTE_CONST = 2.408116385911179

app = Flask(__name__)


@app.route("/file2int", methods=["POST"])
def file2int():
    file = request.files["file"]
    file_bytes = file.stream.read()
    file.close()
    integers = int.from_bytes(file_bytes, "big")
    return str(integers)


@app.route("/int2file", methods=["POST"])
def int2file():
    integers = request.files["intfile"]
    # filename = request.args.get("filename", "pic.png")
    mime = request.args.get("mime", "image/png")

    data_str = integers.stream.read()
    integer_length = len(data_str)
    data = int(data_str)

    byte_length = math.floor(integer_length / BYTE_CONST)

    file_bytes = data.to_bytes(byte_length, byteorder="big")
    buffer = BytesIO(file_bytes)
    send_file(buffer, mimetype=mime)

    return file_bytes


@app.route("/int2base64", methods=["POST"])
def int2base64():
    integers = request.files["intfile"]
    filename = request.args.get("filename", "pic.png")
    mime = request.args.get("mime", "image/png")

    data_str = integers.stream.read()
    integer_length = len(data_str)
    data = int(data_str)

    byte_length = math.floor(integer_length / BYTE_CONST)
    file_bytes = data.to_bytes(byte_length, byteorder="big")
    
    base64_encoded = base64.b64encode(file_bytes)

    return {"mime": mime, "filename": filename, "data": base64_encoded.decode()}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
