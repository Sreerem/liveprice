# A simple real-time subscription system using a dictionary

# Dictionary to store users and the channels they are subscribed to
subscriptions = {
    "alice": ["TechWorld", "CookingDaily"],
    "bob": ["TravelVlogs"],
    "charlie": []
}

# Function to subscribe a user to a channel
def subscribe(user, channel):
    if user in subscriptions:
        if channel not in subscriptions[user]:
            subscriptions[user].append(channel)
            print(f"{user} subscribed to {channel}.")
        else:
            print(f"{user} is already subscribed to {channel}.")
    else:
        subscriptions[user] = [channel]
        print(f"{user} subscribed to {channel} (new user).")

# Function to unsubscribe from a channel
def unsubscribe(user, channel):
    if user in subscriptions and channel in subscriptions[user]:
        subscriptions[user].remove(channel)
        print(f"{user} unsubscribed from {channel}.")
    else:
        print(f"{user} is not subscribed to {channel}.")

# Function to list all subscriptions of a user
def list_subscriptions(user):
    if user in subscriptions:
        print(f"{user}'s subscriptions: {subscriptions[user]}")
    else:
        print(f"{user} has no subscriptions.")

# Real-time usage simulation
subscribe("alice", "HealthTalks")
subscribe("david", "TechWorld")
unsubscribe("bob", "TravelVlogs")
list_subscriptions("alice")
list_subscriptions("david")
