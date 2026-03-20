import lancedb
import pandas as pd
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

templates = [
    {
        "template_name": "modern",
        "description": "student fresher resume modern design"
    },
    {
        "template_name": "developer",
        "description": "software engineer python developer backend resume"
    },
    {
        "template_name": "professional",
        "description": "experienced professional manager resume corporate style"
    }
]

for t in templates:
    t["vector"] = model.encode(t["description"]).tolist()

df = pd.DataFrame(templates)

db = lancedb.connect("database")

db.create_table("templates", df)

print("Database created!")