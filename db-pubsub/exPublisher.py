import redis
import json
import sys
# from datetime import datetime
import time

redisHost = "localhost"
redisPort = 6379
channel = sys.argv[1]
op = sys.argv[2]
msg = sys.argv[3]

r = redis.Redis(host=redisHost, port=redisPort, charset="utf-8", decode_responses=True, password="testpassword")

def pub():
    data = {
        "op": op,
        "messages": msg,
        "timestamp": time.time()
        # "timestamp": datetime.timestamp(datetime.now())
    }
    r.publish(channel, json.dumps(data))

def main():
    pub()

if __name__ == "__main__":
    main()
