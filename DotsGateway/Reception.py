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