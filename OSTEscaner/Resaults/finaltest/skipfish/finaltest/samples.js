var mime_samples = [
  { 'mime': 'application/xhtml+xml', 'samples': [
    { 'url': 'http://localhost/DVWA/', 'dir': '_m0/0', 'linked': 5, 'len': 5967 },
    { 'url': 'http://localhost/DVWA/vulnerabilities/', 'dir': '_m0/1', 'linked': 5, 'len': 4731 },
    { 'url': 'http://localhost/DVWA/vulnerabilities/xss_s/', 'dir': '_m0/2', 'linked': 5, 'len': 4960 } ]
  }
];

var issue_samples = [
  { 'severity': 3, 'type': 40101, 'samples': [
    { 'url': 'http://localhost/DVWA/vulnerabilities/xss_s/', 'extra': 'injected \x27\x3csfi...\x3e\x27 tag seen in HTML', 'sid': '0', 'dir': '_i0/0' } ]
  },
  { 'severity': 1, 'type': 20205, 'samples': [
    { 'url': 'http://localhost/DVWA/vulnerabilities/xss_s/', 'extra': 'Responses too slow for time sensitive tests', 'sid': '0', 'dir': '_i1/0' },
    { 'url': 'http://localhost/DVWA/vulnerabilities/xss_s/', 'extra': 'Responses too slow for time sensitive tests', 'sid': '0', 'dir': '_i1/1' } ]
  },
  { 'severity': 1, 'type': 20101, 'samples': [
    { 'url': 'http://localhost/DVWA/vulnerabilities/xss_s/', 'extra': 'param behavior', 'sid': '0', 'dir': '_i2/0' },
    { 'url': 'http://localhost/DVWA/vulnerabilities/xss_s/', 'extra': 'param behavior', 'sid': '0', 'dir': '_i2/1' },
    { 'url': 'http://localhost/DVWA/vulnerabilities/xss_s/', 'extra': 'param OGNL', 'sid': '0', 'dir': '_i2/2' },
    { 'url': 'http://localhost/DVWA/vulnerabilities/xss_s/', 'extra': 'dir traversal', 'sid': '0', 'dir': '_i2/3' },
    { 'url': 'http://localhost/DVWA/vulnerabilities/xss_s/', 'extra': 'param behavior', 'sid': '0', 'dir': '_i2/4' } ]
  },
  { 'severity': 0, 'type': 10601, 'samples': [
    { 'url': 'http://localhost/DVWA/vulnerabilities/xss_s/', 'extra': '', 'sid': '0', 'dir': '_i3/0' } ]
  },
  { 'severity': 0, 'type': 10404, 'samples': [
    { 'url': 'http://localhost/DVWA/vulnerabilities/', 'extra': 'Directory listing', 'sid': '0', 'dir': '_i4/0' } ]
  },
  { 'severity': 0, 'type': 10205, 'samples': [
    { 'url': 'http://localhost/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i5/0' } ]
  },
  { 'severity': 0, 'type': 10204, 'samples': [
    { 'url': 'http://localhost/', 'extra': 'X-Powered-By', 'sid': '0', 'dir': '_i6/0' },
    { 'url': 'http://localhost/DVWA/vulnerabilities/', 'extra': 'X-Powered-By', 'sid': '0', 'dir': '_i6/1' },
    { 'url': 'http://localhost/DVWA/vulnerabilities/xss_s/', 'extra': 'X-Powered-By', 'sid': '0', 'dir': '_i6/2' } ]
  },
  { 'severity': 0, 'type': 10202, 'samples': [
    { 'url': 'http://localhost/', 'extra': 'Apache/2.4.54 (Unix) OpenSSL/1.1.1s PHP/8.2.0 mod_perl/2.0.12 Perl/v5.34.1', 'sid': '0', 'dir': '_i7/0' } ]
  },
  { 'severity': 0, 'type': 10201, 'samples': [
    { 'url': 'http://localhost/DVWA/', 'extra': 'security', 'sid': '0', 'dir': '_i8/0' },
    { 'url': 'http://localhost/DVWA/', 'extra': 'PHPSESSID', 'sid': '0', 'dir': '_i8/1' } ]
  }
];

