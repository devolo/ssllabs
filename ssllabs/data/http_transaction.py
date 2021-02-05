from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class HttpTransactionData:
    """Dataclass for HTTP Transaction objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#httptransaction
    """

    requestUrl: str
    """Request URL"""

    statusCode: Optional[int]
    """Response status code"""

    requestLine: Optional[str]
    """The entire request line as a single field"""

    requestHeaders: List[str]
    """An array of request HTTP headers, each with name and value"""

    responseLine: Optional[str]
    """The entire response line as a single field"""

    responseHeadersRaw: List[str]
    """All response headers as a single field (useful if the headers are malformed)"""

    responseHeaders: List[Dict]
    """An array of response HTTP headers, each with name and value"""

    fragileServer: bool
    """True if the server crashes when inspected by SSL Labs (in which case the full test is refused)"""
