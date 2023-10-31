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

class TheFactory():
    
    """
        Factory is responsible for understand symentax context of content
        followed by lookup
    """
    def lookup(self,ascii_text):
                
        if "3 seconds" in ascii_text:
            print(ascii_text)
            time.sleep(3)
        elif "5 seconds" in ascii_text:
            print(ascii_text)
            time.sleep(5)
        
        # Layer breakdown
        
        # NLU - Natural Language Understanding

        # NLP - Natural Language Processing
        
        # NLG - Natural Language Generation
        
        return ascii_text
            