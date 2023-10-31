"""
    Copyright (c) 2023 Muhammad Shariq Ayaz
    All rights reserved.
    
    This code is the intellectual property of Muhammad Shariq Ayaz, and it is protected by
    copyright law. Unauthorized use or copying of this code, in whole or in part,
    is strictly prohibited without the express written consent of "Muhammad Shariq Ayaz".
    
    For inquiries about licensing or use of this code, please contact:
    
    Github: /shariqayaz
    Email: gr8shariq@gmail.com
"""
import time
import redis
from TheFactory import TheFactory

class Reception():
    
    def FirstEntry(self,msg):
        print("Wellcome to the Reception of DotsGateway")
        print(type(msg))
        do_door = redis.StrictRedis(host='127.0.0.1', port=6379)
        
        if isinstance(msg, dict):
            #print("Dict Detected")
            user = msg.get('user')
            message = msg.get('message')
            door_name  = msg.get('door_name')
        
        return_response = TheFactory.lookup(self,message)
        
        # Return to the actor who gives input token
        do_door.publish(door_name,return_response)