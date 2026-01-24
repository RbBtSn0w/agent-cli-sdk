from typing import Tuple, Optional
from urllib.parse import urlparse

def parse_cli_url(url: str) -> Tuple[str, int]:
    # Handle port-only case
    if url.isdigit() or (url.startswith("-") and url[1:].isdigit()):
        port = int(url)
        if not (1 <= port <= 65535):
            raise ValueError(f"Port out of range: {port}")
        return "localhost", port

    
    # Handle implicit localhost with port (e.g. :8080)
    if url.startswith(":"):
        return "localhost", int(url[1:])

    parsed = urlparse(url)
    
    # If scheme is missing but it looks like host:port (and not just port)
    if not parsed.scheme and ":" in url:
        # urlparse might handle "localhost:8080" as path if no scheme
        # Let's try prepending // to make it a netloc
        parsed = urlparse("//" + url)

    if not parsed.hostname:
        # Fallback if parsing failed or just a port number string that wasn't digit
        try:
            return "localhost", int(url)
        except ValueError:
            raise ValueError(f"Invalid URL or port: {url}")
            
    port = parsed.port
    if not port:
         raise ValueError(f"No port specified in URL: {url}")
    
    if not (1 <= port <= 65535):
        raise ValueError(f"Port out of range: {port}")
         
    return parsed.hostname, port
