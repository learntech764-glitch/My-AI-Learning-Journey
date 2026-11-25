import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

tokens = enc.encode("Hello, how are you.")

print(tokens)

print(enc.decode(tokens))