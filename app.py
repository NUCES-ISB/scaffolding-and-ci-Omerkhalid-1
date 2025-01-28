from flask import Flask, jsonify, render_template



app = Flask(__name__)

def add(x, y):
    return x + y


def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y  

def mod(x, y):
    return x % y

