class CharacterTokenizer:

    def __init__(self, text):
        chars = sorted(set(text))
        self.char_to_id = {ch: i for i, ch in enumerate(chars)}
        self.id_to_char = {i: ch for ch, i in self.char_to_id.items()}

    def encode(self, text):
        return [self.char_to_id[ch] for ch in text]

    def decode(self, ids):
        return "".join(self.id_to_char[i] for i in ids)


text = "I am a Software engineer. I love coding and solving problems."

tokenizer = CharacterTokenizer(text)

encoded = tokenizer.encode("coding and solving problems")
print("Encoded:", encoded)

decoded = tokenizer.decode(encoded)
print("Decoded:", decoded)

# Output:
# Encoded: [9, 14, 3, 8, 13, 0, 1, 3, 8, 13, 0, 18, 14, 21, 11, 8, 13, 6]      
# Decoded: coding and solving problems