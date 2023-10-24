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
import redis
import json
import ast
import multiprocessing
from Reception import Reception

class Manager():
    
    def __init__(self):
        self.redis_conn = redis.StrictRedis(host='127.0.0.1', port=6379)
        self.p = self.redis_conn.pubsub()
        self.p.subscribe('Gateway_Knock')
        print("Manager Speaking")
        self.capture_message()

    def capture_message(self):
        while True:
            for m in self.p.listen():
                d = str(m['data']).replace('b\'', '\'')
                if not d:
                    continue
                try:
                    data = str(ast.literal_eval(d))
                    msg = json.loads(data)
                    print(msg)
                    if isinstance(msg, dict):
                        user = msg.get('user')
                        message = msg.get('message')
                        door_name  = msg.get('door_name')
                        
                        if user is not None:
                            
                            queue_job = multiprocessing.Queue()
                            
                            queue_job_process = multiprocessing.Process(
                                target=Reception.FirstEntry, args=(queue_job,msg))
                            
                            queue_job_process.start()
                            
                        else:
                            print("Key 'user' not found in the JSON object")
                    else:
                        print("Invalid JSON object")
                        
                        
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    continue
                