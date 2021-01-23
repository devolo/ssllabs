from dataclasses import dataclass
from typing import List


@dataclass
class HttpTransactionData:
    """Dataclass for HTTP Transaction objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#httptransaction
    """

    requestUrl: str
    """Request URL"""

    statusCode: int
    """Response status code"""

    requestLine: str
    """The entire request line as a single field"""

    # ToDo: Check datatype of list emelements
    requestHeaders: List
    """An array of request HTTP headers, each with name and value"""

    responseLine: str
    """The entire response line as a single field"""

    responseHeadersRaw: List[str]
    """All response headers as a single field (useful if the headers are malformed)"""

    # ToDo: Check datatype of list emelements
    responseHeaders: List
    """An array of response HTTP headers, each with name and value"""

    fragileServer: bool
    """True if the server crashes when inspected by SSL Labs (in which case the full test is refused)"""
