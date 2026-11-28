from src.embedder import model
from sklearn.metrics.pairwise import cosine_similarity
from src.config import TOP_K
from data.data import documents

doc_embeddings = model.encode(documents)


def search(query):

    query_embedding = model.encode(query)

    similarities = cosine_similarity(
        [query_embedding],
        doc_embeddings
    )[0]

    results = list(
        zip(
            documents,
            similarities
        )
    )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results[:TOP_K]