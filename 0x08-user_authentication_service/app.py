#!/usr/bin/env python3
""" module routes """

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
