from dataclasses import dataclass
from typing import List, Optional

from .certificate_chain import CertificateChainData
from .drown_hosts import DrownHostsData
from .hpkp_policy import HpkpPolicyData
from .hsts_policy import HstsPolicyData
from .hsts_preload import HstsPreloadData
from .http_transaction import HttpTransactionData
from .named_groups import NamedGroupsData
from .protocol import ProtocolData
from .sim_details import SimDetailsData
from .static_pkp_policy import StaticPkpPolicyData
from .suite import SuiteData


@dataclass
class EndpointDetailsData:
    """Dataclass for endpoint detail objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#endpointdetails
    """

    hostStartTime: int
    """
    Endpoint assessment starting time, in milliseconds since 1970. This field is useful when test results are retrieved in
    several HTTP invocations. Then, you should check that the hostStartTime value matches the startTime value of the host.
    """

    certChains: List[CertificateChainData]
    """Server Certificate chains"""

    protocols: List[ProtocolData]
    """Supported protocols"""

    suites: List[SuiteData]
    """Supported cipher suites per protocol"""

    noSniSuites: SuiteData
    """Cipher suites observed only with client that does not support Server Name Indication (SNI)."""

    namedGroups: NamedGroupsData
    """Instance of NamedGroups object."""

    serverSignature: str
    """
    Contents of the HTTP Server response header when known. This field could be absent for one of two reasons: 1) the HTTP
    request failed (check httpStatusCode) or 2) there was no Server response header returned.
    """

    prefixDelegation: bool
    """True if this endpoint is reachable via a hostname with the www prefix"""

    nonPrefixDelegation: bool
    """True if this endpoint is reachable via a hostname without the www prefix"""

    vulnBeast: bool
    """True if the endpoint is vulnerable to the BEAST attack"""

    renegSupport: int
    """This is an integer value that describes the endpoint support for renegotiation."""

    sessionResumption: int
    """This is an integer value that describes endpoint support for session resumption."""

    compressionMethods: int
    """Integer value that describes supported compression methods"""

    supportsNpn: bool
    """True if the server supports NPN"""

    npnProtocols: str
    """Space separated list of supported NPN protocols"""

    supportsAlpn: bool
    """True if the server supports ALPN"""

    alpnProtocols: str
    """Space separated list of supported ALPN protocols"""

    sessionTickets: int
    """Indicates support for Session Tickets"""

    ocspStapling: bool
    """True if OCSP stapling is deployed on the server"""

    staplingRevocationStatus: int
    """Same as Cert.revocationStatus, but for the stapled OCSP response."""

    staplingRevocationErrorMessage: str
    """Description of the problem with the stapled OCSP response, if any."""

    sniRequired: bool
    """If SNI support is required to access the web site."""

    httpStatusCode: int
    """
    Status code of the final HTTP response seen. When submitting HTTP requests, redirections are followed, but only if they
    lead to the same hostname. If this field is not available, that means the HTTP request failed.
    """

    httpForwarding: str
    """Available on a server that responded with a redirection to some other hostname."""

    supportsRc4: bool
    """True if the server supports at least one RC4 suite."""

    rc4WithModern: bool
    """True if RC4 is used with modern clients."""

    rc4Only: bool
    """True if only RC4 suites are supported."""

    forwardSecrecy: int
    """Indicates support for Forward Secrecy"""

    supportsAead: bool
    """True if the server supports at least one AEAD suite."""

    supportsCBC: bool
    """True if the server supports at least one CBC suite."""

    protocolIntolerance: int
    """Indicates protocol version intolerance issues"""

    miscIntolerance: int
    """Indicates various other types of intolerance"""

    sims: SimDetailsData
    """Instance of SimDetails."""

    heartbleed: bool
    """True if the server is vulnerable to the Heartbleed attack."""

    heartbeat: bool
    """True if the server supports the Heartbeat extension."""

    openSslCcs: int
    """Results of the CVE-2014-0224 test"""

    openSSLLuckyMinus20: int
    """Results of the CVE-2016-2107 test"""

    ticketbleed: int
    """Results of the ticketbleed CVE-2016-9244 test"""

    bleichenbacher: int
    """Results of the Return Of Bleichenbacher's Oracle Threat (ROBOT) test"""

    zombiePoodle: int
    """Results of the Zombie POODLE test"""

    goldenDoodle: int
    """Results of the GOLDENDOODLE test"""

    zeroLengthPaddingOracle: int
    """Results of the 0-Length Padding Oracle (CVE-2019-1559) test"""

    sleepingPoodle: int
    """Results of the Sleeping POODLE test"""

    poodle: bool
    """True if the endpoint is vulnerable to POODLE"""

    poodleTls: int
    """Results of the POODLE TLS test"""

    fallbackScsv: Optional[bool]
    """
    True if the server supports TLS_FALLBACK_SCSV, false if it doesn't. This field will not be available if the server's
    support for TLS_FALLBACK_SCSV can't be tested because it supports only one protocol version (e.g., only TLS 1.2).
    """

    freak: bool
    """True if the server is vulnerable to the FREAK attack, meaning it supports 512-bit key exchange."""

    hasSct: int
    """Information about the availability of certificate transparency information (embedded SCTs)"""

    dhPrimes: Optional[List[str]]
    """List of hex-encoded DH primes used by the server. Not present if the server doesn't support the DH key exchange."""

    dhUsesKnownPrimes: Optional[int]
    """Whether the server uses known DH primes. Not present if the server doesn't support the DH key exchange."""

    dhYsReuse: Optional[bool]
    """True if the DH ephemeral server value is reused. Not present if the server doesn't support the DH key exchange."""

    ecdhParameterReuse: bool
    """True if the server reuses its ECDHE values"""

    logjam: bool
    """True if the server uses DH parameters weaker than 1024 bits."""

    chaCha20Preference: bool
    """
    True if the server takes into account client preferences when deciding if to use ChaCha20 suites. Will be deprecated in
    new version.
    """

    hstsPolicy: HstsPolicyData
    """Server's HSTS policy. Experimental."""

    hstsPreloads: List[HstsPreloadData]
    """Information about preloaded HSTS policies."""

    hpkpPolicy: HpkpPolicyData
    """Server's HPKP policy."""

    hpkpRoPolicy: HpkpPolicyData
    """Server's HPKP-RO policy."""

    staticPkpPolicy: StaticPkpPolicyData
    """Server's SPKP policy."""

    httpTransactions: List[HttpTransactionData]
    """An array of HttpTransaction objects."""

    drownHosts: List[DrownHostsData]
    """List of DROWN hosts."""

    drownErrors: bool
    """True if error occurred in the DROWN test."""

    drownVulnerable: bool
    """True if server vulnerable to the DROWN attack."""

    implementsTLS13MandatoryCS: Optional[bool]
    """True if server supports mandatory TLS 1.3 cipher suite (TLS_AES_128_GCM_SHA256), null if TLS 1.3 not supported."""

    zeroRTTEnabled: Optional[int]
    """Results of the 0-RTT test. This test will only be performed if TLS 1.3 is enabled."""
