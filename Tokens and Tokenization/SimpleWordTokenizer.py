
# 1. Simple Word Tokenizer

text = "Hello, how are you doing today?"

# Tokenization
tokens = text.lower().split()

print(tokens)

# Output:
# ['hello,', 'how', 'are', 'you', 'doing', 'today?']

# 2.Improved Tokenizer Using Regex
import re

text = "Hello, how are you doing today?"

tokens = re.findall(r"\w+|[^\w\s]", text)

print(tokens)
# Output:  
# ['Hello', ',', 'how', 'are', 'you', 'doing', 'today', '?']

# 3. Building a Vocabulary

import re

text = "Hello, how are you? Hello again!"

tokens = re.findall(r"\w+|[^\w\s]", text)

# Create vocabulary
vocab = {word: idx for idx, word in enumerate(sorted(set(tokens)))}

print(vocab)
# Output:
# {'!': 0, ',': 1, '?': 2, 'Hello': 3, 'again': 4, 'are': 5, 'doing': 6, 'how': 7, 'today': 8, 'you': 9}

# 4. Encode Tokens Into IDs
encoded = [vocab[token] for token in tokens]

print(encoded)
# Output:
# [3, 1, 7, 5, 9, 2, 3, 4, 0]  

# 5. Decode IDs Back Into Tokens
reverse_vocab = {v: k for k, v in vocab.items()}

decoded = [reverse_vocab[id] for id in encoded]

print(decoded)
# Output:
# ['Hello', ',', 'how', 'are', 'you', '?', 'Hello', 'again', '!']