import uuid
uuid.uuid4()
import random
import time
print("""                                                      
                                                           
                                                                ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗        
                                                                ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ██╗
                                                                ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║    ╚═╝
                                                                ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║    ██╗
                                                                ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝    ╚═╝
                                                                 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝        
                                                                                           

                                                                                    
   """)
time.sleep(1.5)
print(f""" 
                                                                ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗
                                                                ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝
                                                                ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝ 
                                                                ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗ 
                                                                ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗
                                                                ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝

 
                                                    
       
                                                                par Timeo | by Timeo 
""")



time.sleep(1.0)

import threading

def hello():
    print(f"""
                                                                 ██████╗  ██████╗ 
                                                                ██╔════╝ ██╔═══██╗
                                                                ██║  ███╗██║   ██║
                                                                ██║   ██║██║   ██║
                                                                ╚██████╔╝╚██████╔╝
                                                                 ╚═════╝  ╚═════╝ 

""")
t=threading.Timer(5.0, hello)
t.start() 
 
for i in range(5,0,-1):
    print(                                 i)
    time.sleep(1)
 
time.sleep(1.8) 
while True:
    id = str(uuid.uuid4())
    trimmed = id[:random.randint(0, len(id) - 1)]
    space = " " * random.randint(0, 15)
    print(f"""                                                  {space}{trimmed}""")
    print(f"""{space}{trimmed}""")
    print(f"""                                                                                                               {space}{trimmed}""")
    print(f"""                                                                                                                                                                               {space}{trimmed}""")