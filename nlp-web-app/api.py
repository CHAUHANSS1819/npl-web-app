import paralleldots
paralleldots.set_api_key("Gn93OshmKy6eVqdBvt8uuDZBzzZrmqhq1JNiTfxe974")


def ner(text):
    ner = paralleldots.ner(text)
    return ner

