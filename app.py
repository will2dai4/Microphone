from flask import Flask, request, response, make_response, jsonify
import discord

PORT = 3000

app = Flask(__name__)

