import redis
import json
import logging
import os
import db

# redis_host = "localhost"
redis_host = "redis-server"
redis_port = 6379
redis_password = "testpassword"
channel = os.environ.get("CHANNEL")

def redis_connect():
    logging.warning("redis connect")
    conn = redis.Redis(host=redis_host, 
        port=redis_port,
        charset="utf-8",
        decode_responses=True,
        password=redis_password
    )
    return conn

r = redis_connect()

def subscriber():
    pubsub = r.pubsub()
    pubsub.subscribe(channel)
    logging.warning(f'Connect to host: {redis_host} channel: {channel}')
    logging.warning('waiting for Publisher...')

    for message in pubsub.listen():
        # print(message)
        if message["type"] == "message":
            data = json.loads(message["data"])
            # print(data["op"])

            if data["op"] == "insert":
                payload = [
                    data["cardid"],
                    data["studentname"],
                    data["studentid"],
                    data["studentaccount"]
                ]

                logging.warning(payload)
                db.insert_db(payload)

            if data["op"] == "select":
                logging.warning("OP: select -> show data")
                db.select_db() 

