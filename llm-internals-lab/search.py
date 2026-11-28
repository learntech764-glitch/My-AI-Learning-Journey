from sklearn.metrics.pairwise import cosine_similarity


def get_similarity(
        vector1,
        vector2):

    score = cosine_similarity(
        [vector1],
        [vector2]
    )

    return score[0][0]