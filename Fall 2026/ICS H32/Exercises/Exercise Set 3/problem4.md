# Problem 4

## Why do clients speak first?

Since the client is the one that will be taking some action, then the client is the one that needs to reach out. The server does not have anything to say until it is asked something. If it were to speak before anybody had asked it anything, it would either be speaking to nobody or trying to guess who it was addressing.

## Why does the client start with a "hello" that names the protocol?

Because the client and the server have to agree on how to talk to each other before the conversation can begin, and the most reliable way to agree is to make the agreement explicit and checkable rather than to hope both sides happen to be configured the same way.

The name of the protocol is a concise, clear identifier for a full list of rules, including the messages that are defined, their possible ordering, and how to read the rest of the bytes following them. "Hello" is a message that allows the server to check whether it is using the correct language before agreeing to do anything, or to simply send back an error message.