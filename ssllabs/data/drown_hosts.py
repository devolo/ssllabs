from dataclasses import dataclass


@dataclass
class DrownHostsData:
    """Dataclass for Drown Hosts objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#drownhosts
    """

    ip: str
    """IP address of server that shares same RSA-Key/hostname in its certificate"""

    export: bool
    """True if export cipher suites detected"""

    port: int
    """Port number of the server"""

    special: bool
    """True if vulnerable OpenSSL version detected"""

    sslv2: bool
    """True if SSL v2 is supported"""

    status: str
    """Drown host status"""
