import lancedb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

db = lancedb.connect("database")
table = db.open_table("templates")


def select_template(profile_text):

    vector = model.encode(profile_text)

    result = table.search(vector).limit(1).to_list()

    return result[0]["template_name"]