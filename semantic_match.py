from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def semantic_score(
    resume_text,
    jd_text
):

    resume_embedding = model.encode(
        resume_text
    )

    jd_embedding = model.encode(
        jd_text
    )

    similarity = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )

    return round(
        similarity[0][0] * 100,
        2
    )