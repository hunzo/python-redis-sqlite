import redis
import json
import sys
# from datetime import datetime
import time
import random
import uuid
import names

redisHost = "localhost"
redisPort = 6379

r = redis.Redis(host=redisHost, port=redisPort, charset="utf-8", decode_responses=True, password="testpassword")

def initdata():
    ch = ["CH1", "CH2", "CH3"]
    # ch = ["CH1", "CH1", "CH1"]
    op = ["insert"]
    for i in range(1, 10000):
        fname = names.get_first_name()
        lname = names.get_last_name()
        account = f"{fname}@email.com"
        data = {
            "op": "insert",
            "cardid": str(uuid.uuid1()),
            "studentname": names.get_full_name(),
            "studentid": str(uuid.uuid1()),
            "studentaccount": account
        }
        r.publish(random.choice(ch), json.dumps(data))

def show(ch):
    data = {
        "op": "select"
    }
    r.publish(ch, json.dumps(data))
    

def main():
    if sys.argv[1] == "adddata":
        initdata()

    if sys.argv[1] == "CH1":
        show("CH1")
    
    if sys.argv[1] == "CH2":
        show("CH2")
    
    if sys.argv[1] == "CH3":
        show("CH3")
 
    
    print("success")

if __name__ == "__main__":
    main()
