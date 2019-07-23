"""
Python - OOP - Observer Pattern
https://github.com/r3ap3rpy/python
"""
class LadiesAbove30:
    def __init__(self, topic):
        topic.register(self)
    
    def notify(self, *args, **kwards):
        print(type(self).__name__, "---> Got", args, "From", topic)

class MenAbove40:
    def __init__(self, topic):
        topic.register(self)
    
    def notify(self, *args, **kwards):
        print(type(self).__name__, "---> Got", args, "From", topic)


class Topic:
    def __init__(self):
        self.__clients = []
    
    def register(self, client):
        print("New subscriber : {}".format(client))
        self.__clients.append(client)

    
    def notifyAll(self, *args, **kwards):
        for client in self.__clients:
            if kwards.get("menOnly") and isinstance(client, MenAbove40):
                client.notify(self, *args, **kwards)
            if kwards.get("women") and isinstance(client, MenAbove40):
                client.notify(self, *args, **kwards)
        
topic = Topic()
Subscribers = []
for i in range(20):
    Subscribers.append(MenAbove40(topic))

for i in range(20):
    Subscribers.append(LadiesAbove30(topic))


topic.notifyAll("Men!", menOnly=True)
topic.notifyAll("Women", women=True, li = "d")