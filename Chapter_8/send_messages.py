def send_messages(messages):
    sent_messages = []
    while messages:
        message = messages.pop(0)
        print(message)
        sent_messages.append(message)
    return sent_messages

tosend_messages = ["Hi", "how are you", "when are you back"]
sent_messages = send_messages(tosend_messages)
print(tosend_messages)
print(sent_messages)
        