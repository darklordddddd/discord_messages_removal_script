import json, requests, sys
from time import sleep
from datetime import datetime 

block=[]
length=0
last_message=""
total_length=0

block_length=50
success_code=204
delete_sleep=0.2

print("clears all of your messages in a channel")
print("in order for this script to work properly the channel id, auth token, and username id is required")
username_id = input("username id: ")
auth_token = input("auth token: ")
channel_id = input("channel id: ")
delete_from_all_users = True if input("delete messages from other users (y/n): ") == "y" else False
print("deleting all messages in " + channel_id + " from username id " + username_id + "...") if delete_from_all_users == False else print("deleting all messages in " + channel_id + "...")

def get_message_block(auth, id, b_length, last=""):
    if not last:
        messages = json.loads(requests.get("http://canary.discordapp.com/api/v6/channels/" + id + "/messages", headers={"authorization": auth}, params={"limit": b_length}).content)
    else:
        messages = json.loads(requests.get("http://canary.discordapp.com/api/v6/channels/" + id + "/messages", headers={"authorization": auth}, params={"before" : last, "limit" : b_length}).content)

    if (len(messages) != 0):
        oldest = sorted(messages, key=lambda x: x["timestamp"], reverse=True)[-1]
        return messages, oldest["id"]
    else:
        return messages, ""

def delete_message_block(auth, id, user, messages):
    global success_code
    for message in messages:
        if delete_from_all_users:
            while True:
                r = requests.delete("http://canary.discordapp.com/api/v6/channels/" + id + "/messages/" + message["id"], headers={"authorization": auth})
                if (r.status_code == success_code):
                    break
                sleep(delete_sleep)
            
        else:
            if (message["author"]["id"] == user):
                while True:
                    r = requests.delete("http://canary.discordapp.com/api/v6/channels/" + id + "/messages/" + message["id"],
                                headers={"authorization": auth})
                    if (r.status_code == success_code):
                        break
                    sleep(delete_sleep)

start = datetime.now()
while True:
    block, last_message = get_message_block(auth_token, channel_id, block_length, last_message)
    length = len(block)
    total_length += length
    
    delete_message_block(auth_token, channel_id, username_id, block)
    
    if (length < block_length): #end
        break
    
end = datetime.now()
print('all messages deleted, elapsed time = (hh:mm:ss.ms) {}'.format(end - start))
print("press any key to exit...")
sys.stdin.read(1)