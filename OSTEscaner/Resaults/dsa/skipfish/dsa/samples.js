var mime_samples = [
  { 'mime': 'application/xhtml+xml', 'samples': [
    { 'url': 'http://localhost/Vulnerable-Web-Application/', 'dir': '_m0/0', 'linked': 5, 'len': 1269 },
    { 'url': 'http://localhost/Vulnerable-Web-Application/XSS/', 'dir': '_m0/1', 'linked': 5, 'len': 2057 },
    { 'url': 'http://localhost/Vulnerable-Web-Application/XSS/XSS_level1.php', 'dir': '_m0/2', 'linked': 5, 'len': 622 } ]
  }
];

var issue_samples = [
  { 'severity': 3, 'type': 40101, 'samples': [
    { 'url': 'http://localhost/Vulnerable-Web-Application/XSS/XSS_level1.php?username=.htaccess.aspx--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000021v227743\x3e&submit=Submit', 'extra': 'injected \x27\x3csfi...\x3e\x27 tag seen in HTML', 'sid': '0', 'dir': '_i0/0' } ]
  },
  { 'severity': 2, 'type': 30601, 'samples': [
    { 'url': 'http://localhost/Vulnerable-Web-Application/XSS/XSS_level1.php?username=Smith&submit=Submit', 'extra': '', 'sid': '0', 'dir': '_i1/0' } ]
  },
  { 'severity': 0, 'type': 10901, 'samples': [
    { 'url': 'http://localhost/Vulnerable-Web-Application/XSS/XSS_level1.php', 'extra': '', 'sid': '0', 'dir': '_i2/0' } ]
  },
  { 'severity': 0, 'type': 10404, 'samples': [
    { 'url': 'http://localhost/Vulnerable-Web-Application/XSS/', 'extra': 'Directory listing', 'sid': '0', 'dir': '_i3/0' } ]
  },
  { 'severity': 0, 'type': 10205, 'samples': [
    { 'url': 'http://localhost/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i4/0' } ]
  },
  { 'severity': 0, 'type': 10204, 'samples': [
    { 'url': 'http://localhost/', 'extra': 'X-Powered-By', 'sid': '0', 'dir': '_i5/0' },
    { 'url': 'http://localhost/Vulnerable-Web-Application/XSS/', 'extra': 'X-Powered-By', 'sid': '0', 'dir': '_i5/1' },
    { 'url': 'http://localhost/Vulnerable-Web-Application/XSS/XSS_level1.php', 'extra': 'X-Powered-By', 'sid': '0', 'dir': '_i5/2' } ]
  },
  { 'severity': 0, 'type': 10202, 'samples': [
    { 'url': 'http://localhost/', 'extra': 'Apache/2.4.54 (Unix) OpenSSL/1.1.1s PHP/8.2.0 mod_perl/2.0.12 Perl/v5.34.1', 'sid': '0', 'dir': '_i6/0' } ]
  }
];

