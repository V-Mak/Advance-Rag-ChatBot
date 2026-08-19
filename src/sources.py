def get_sources(documents):

    sources = []

    for document, score in documents:

        page = document.metadata.get("page", "N/A")

        source = document.metadata.get("source", "N/A")

        sources.append({
            "page": page,
            "source": source,
            "score": score
        })
    return sources