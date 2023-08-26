class Phone:
    def __init__(self) -> None:
        pass

class NotyficationSystem(Phone):
    def __init__(self):
        self.observers = []

    def update(self, messages , str):
        print(f"{str} display: {messages}") 

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify_mess(self, data , parametr , str):
        for observer in self.observers:
            if parametr == observer:
                observer.update(data , str)

# Usage
messages = NotyficationSystem()
calls = NotyficationSystem()
notification = NotyficationSystem()

notification.attach(messages)

notification.attach(calls)

notification.notify_mess(3 , calls , "calls")
notification.notify_mess(17 , messages, "messages")


notification.detach(calls)

notification.notify_mess(4 , calls , "calls")
notification.notify_mess(19 , messages, "messages")

