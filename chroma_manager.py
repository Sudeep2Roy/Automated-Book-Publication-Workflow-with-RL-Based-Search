import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("book_versions")

def save_version(version_text, tag):
    collection.add(
        documents=[version_text],
        metadatas=[{"tag": tag}],
        ids=[tag]
    )

def search_version(query):
    result = collection.query(
        query_texts=[query],
        n_results=1
    )
    return result

def rl_search(query):
    result = collection.query(
        query_texts=[query],
        n_results=3
    )
    return result["documents"][0]
