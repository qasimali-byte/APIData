from flask import Flask, jsonify, abort, make_response, request,render_template
import sys, sqlite3, requests, datetime, time, re, json, optparse
import xmltodict
import helpers
import platform
app = Flask(__name__)

start = int(round(time.time()))
print("api running")
@app.route("/", methods=['GET', 'POST'])
def func():
    return 'hello_world'

@app.route("/parse_xml", methods=['GET', 'POST'])
def parse_xml():
    content_dict = xmltodict.parse(request.data)
    print(type(content_dict))
    return content_dict

if __name__ == '__main__':
    print("Starting python app")
    app.run(host='0.0.0.0', port=8080, debug=False)
