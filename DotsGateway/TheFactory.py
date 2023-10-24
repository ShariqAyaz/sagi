
import time 

class TheFactory():
    
    def lookup(self,ascii_text):
                
        if "3 seconds" in ascii_text:
            print(ascii_text)
            time.sleep(3)
        elif "5 seconds" in ascii_text:
            print(ascii_text)
            time.sleep(5)
                
        return ascii_text

        # Layer breakdown
        
        # NLU - Natural Language Understanding
        
        # NLP - Natural Language Processing
        
        # NLG - Natural Language Generation
            