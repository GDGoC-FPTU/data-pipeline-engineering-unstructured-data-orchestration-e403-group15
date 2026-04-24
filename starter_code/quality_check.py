def run_semantic_checks(doc_dict: dict) -> bool:
    content = doc_dict.get("content", "")
    if not isinstance(content, str) or len(content.strip()) < 10:
        return False

    toxic_keywords = ["Null pointer exception", "OCR Error", "Traceback"]
    normalized_content = content.lower()
    for keyword in toxic_keywords:
        if keyword.lower() in normalized_content:
            return False

    return True
