from urllib.parse import urlparse


def normalize_url(url: str) -> str:
    parsed_url = urlparse(url)
    normalized_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    return normalized_url
