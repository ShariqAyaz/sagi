"""
    Copyright (c) 2023 Muhammad Shariq Ayaz
    All rights reserved.
    
    This code is the intellectual property of Muhammad Shariq Ayaz, and it is protected by
    copyright law. Unauthorized use or copying of this code, in whole or in part,
    is strictly prohibited without the express written consent of "Muhammad Shariq Ayaz".
    
    For inquiries about licensing or use of this code, please contact:
    
    Github: /shariqayaztech
    Email: gr8shariq@gmail.com
"""
import time
import asyncio
#import aiohttp
import redis
import json
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random
import string
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    user = "userone@userx.com"
    door = user + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    json_data = json.dumps({
        "user":user,
        "remote_address": request.remote_addr,
        "message":message,
        "door_name": door
    })
    
    redis_conn = redis.StrictRedis(host='127.0.0.1', port=6379)
    redis_conn.publish('Gateway_Knock',json_data)
    
    p = redis_conn.pubsub()
    p.subscribe(door)    
    for x in p.listen():
        d = x['data']
        if isinstance(d, bytes):
            d = base64.b64encode(d).decode('utf-8')  # Convert the bytes to a base64-encoded string
            decoded_data = base64.b64decode(d).decode('utf-8')
            print(decoded_data)

            emit('message', decoded_data)

if __name__ == '__main__':
    socketio.run(app)
