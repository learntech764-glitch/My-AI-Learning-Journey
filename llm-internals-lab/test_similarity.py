from embedder import create_embedding
from search import get_similarity

v1 = create_embedding(
    "I love artificial intelligence"
)

v2 = create_embedding(
    "I love icecream"
)

score = get_similarity(v1, v2)

print(score)
