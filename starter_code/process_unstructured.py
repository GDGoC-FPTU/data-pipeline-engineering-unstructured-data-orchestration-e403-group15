import re


def process_pdf_data(raw_json: dict) -> dict:
    raw_text = raw_json.get("extractedText", "")
    cleaned_content = re.sub(r"\b(?:HEADER|FOOTER)_PAGE_\d+\b", " ", raw_text)
    cleaned_content = re.sub(r"\s+", " ", cleaned_content).strip()

    return {
        "document_id": str(raw_json.get("docId", "")),
        "source_type": "PDF",
        "author": str(raw_json.get("authorName", "")).strip(),
        "category": str(raw_json.get("docCategory", "")),
        "content": cleaned_content,
        "timestamp": str(raw_json.get("createdAt", "")),
    }


def process_video_data(raw_json: dict) -> dict:
    return {
        "document_id": str(raw_json.get("video_id", "")),
        "source_type": "Video",
        "author": str(raw_json.get("creator_name", "")).strip(),
        "category": str(raw_json.get("category", "")),
        "content": str(raw_json.get("transcript", "")).strip(),
        "timestamp": str(raw_json.get("published_timestamp", "")),
    }
