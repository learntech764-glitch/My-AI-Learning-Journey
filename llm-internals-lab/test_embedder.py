from embedder import create_embedding

vector = create_embedding(
    "I love Artificial Intelligence"
)

print(vector)
print(len(vector))

vector = create_embedding(
    "I love AI"
)

print(vector)
print(len(vector))