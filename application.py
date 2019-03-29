#!/usr/bin/python

from flask import Flask, redirect

application = Flask(__name__)

@application.route("/")
def hello():
    return redirect("http://www.cloudavail.com", code=301)
