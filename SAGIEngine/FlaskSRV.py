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
import os
import multiprocessing
from flask import make_response,Flask, request, render_template, session,redirect, url_for,jsonify
import logging
import redis
from asgiref.wsgi import WsgiToAsgi
from flask_cors import CORS
from flask_socketio import SocketIO, emit

class FlaskSRV():
    
    def __init__(self):
        self.RUNNING_STATE=False
        self.redis_conn = redis.StrictRedis(host='127.0.0.1', port=6379)
        self.p = self.redis_conn.pubsub()
        self.p.subscribe('websock_server')
    
    def _run_flask(queue):
        app = Flask(__name__)
        socketio = SocketIO(app)

        CORS(app, origins={
            r"/*": {
                "origins": ["http://localhost:5000", "http://127.0.0.1:5000","*"],
                "headers": ["Content-Type", "Authorization"],
                "methods": ["GET", "POST","PATCH", "PUT", "DELETE"]
            }
        })
        
        # Disable the log on console, and broadcase on Redis instead
        log = logging.getLogger('werkzeug')
        
        log.disabled = True
        
        logger = logging.getLogger(__name__)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        app.logger.handlers = logger.handlers
        app.logger.setLevel(logger.level)
        
        @app.errorhandler(404)
        def page_not_found(error):
            FlaskSRV.publish_log('404 Not Found: The requested URL was not found on the server.' + str(404))
            return '404 Not Found: The requested URL was not found on the server.', 404

        @socketio.on("connect")
        def on_connect():
            print("Client connected")

        @socketio.on("message")
        def on_message(message):
            print("Received message:", message)
        
        @app.route('/', methods=['GET'])
        def hello():
            
            ip_address = request.remote_addr
            method = request.method
            port = request.environ.get('SERVER_PORT')
            param_name = request.args.get('param_name')
            query_param = request.args.get('query_param')
            
            log_message = f'{ip_address} - "{method} / HTTP/1.1" {port} - param_name="{param_name}" query_param="{query_param}"'

            logger.info(log_message)
    
            FlaskSRV.publish_log(log_message)
            
            return 'Hellso, Wsosrld!'

        try:
            socketio.run(app, host="127.0.0.1", port=5000)
            ## app.run()
            app = WsgiToAsgi(app)
            
        except Exception as e:
            queue.put(e)
            FlaskSRV.publish_log(str(e))
        
        @app.errorhandler(404)
        def handle_not_found(e):
            ip_address = request.remote_addr
            method = request.method
            port = request.environ.get('SERVER_PORT')
            log_message = f'{ip_address} - "{method} {request.full_path} HTTP/1.1" {port} - 404 Not Found'
            
            logger.warning(log_message)
            FlaskSRV.publish_log(log_message)
            
            return '404 Not Found'
            
    @staticmethod
    def publish_log(msg):
        redis_conn = redis.StrictRedis(host='127.0.0.1', port=6379)
        redis_conn.publish('websock_server', msg)

    def running_state(self):
        return self.RUNNING_STATE
