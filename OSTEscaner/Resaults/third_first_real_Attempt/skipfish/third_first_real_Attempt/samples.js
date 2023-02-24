var mime_samples = [
  { 'mime': 'application/javascript', 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/main.js', 'dir': '_m0/0', 'linked': 2, 'len': 399134 },
    { 'url': 'https://juice-shop.herokuapp.com/polyfills.js', 'dir': '_m0/1', 'linked': 2, 'len': 54475 },
    { 'url': 'https://juice-shop.herokuapp.com/runtime.js', 'dir': '_m0/2', 'linked': 2, 'len': 3210 },
    { 'url': 'https://juice-shop.herokuapp.com/vendor.js', 'dir': '_m0/3', 'linked': 2, 'len': 400000 } ]
  },
  { 'mime': 'application/xhtml+xml', 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'dir': '_m1/0', 'linked': 2, 'len': 1987 } ]
  },
  { 'mime': 'text/css', 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/styles.css', 'dir': '_m2/0', 'linked': 2, 'len': 400000 } ]
  },
  { 'mime': 'text/html', 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/dataerasure/', 'dir': '_m3/0', 'linked': 1, 'len': 2940 },
    { 'url': 'https://juice-shop.herokuapp.com/profile/', 'dir': '_m3/1', 'linked': 1, 'len': 1231 },
    { 'url': 'https://juice-shop.herokuapp.com/rest/', 'dir': '_m3/2', 'linked': 1, 'len': 2866 } ]
  },
  { 'mime': 'text/plain', 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/redirect?to=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm', 'dir': '_m4/0', 'linked': 1, 'len': 88 } ]
  }
];

var issue_samples = [
  { 'severity': 3, 'type': 40401, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/polyfills.js', 'extra': 'server-side JavaScript source', 'sid': '0', 'dir': '_i0/0' },
    { 'url': 'https://juice-shop.herokuapp.com/redirect?to=.../https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm', 'extra': 'CVS RCS data', 'sid': '0', 'dir': '_i0/1' } ]
  },
  { 'severity': 3, 'type': 40302, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/redirect?to=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000040v914955\x3e', 'extra': 'text/plain', 'sid': '0', 'dir': '_i1/0' } ]
  },
  { 'severity': 3, 'type': 40201, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': '//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.css', 'sid': '0', 'dir': '_i2/0' },
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': '//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.js', 'sid': '0', 'dir': '_i2/1' },
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': '//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js', 'sid': '0', 'dir': '_i2/2' } ]
  },
  { 'severity': 1, 'type': 20301, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/assets', 'extra': '', 'sid': '0', 'dir': '_i3/0' } ]
  },
  { 'severity': 1, 'type': 20101, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i4/0' },
    { 'url': 'https://juice-shop.herokuapp.com/1', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i4/1' },
    { 'url': 'https://juice-shop.herokuapp.com/1?z.iconName=function', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i4/2' },
    { 'url': 'https://juice-shop.herokuapp.com/main.js', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i4/3' },
    { 'url': 'https://juice-shop.herokuapp.com/styles.css', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i4/4' },
    { 'url': 'https://juice-shop.herokuapp.com/vendor.js', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i4/5' },
    { 'url': 'https://juice-shop.herokuapp.com/assets/i18n', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i4/6' } ]
  },
  { 'severity': 0, 'type': 10901, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/rest/2fa/', 'extra': '', 'sid': '0', 'dir': '_i5/0' },
    { 'url': 'https://juice-shop.herokuapp.com/assets/i18n', 'extra': '', 'sid': '0', 'dir': '_i5/1' } ]
  },
  { 'severity': 0, 'type': 10802, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/redirect?to=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm', 'extra': 'text/plain', 'sid': '0', 'dir': '_i6/0' } ]
  },
  { 'severity': 0, 'type': 10403, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/dataerasure/', 'extra': '', 'sid': '0', 'dir': '_i7/0' },
    { 'url': 'https://juice-shop.herokuapp.com/profile/', 'extra': '', 'sid': '0', 'dir': '_i7/1' },
    { 'url': 'https://juice-shop.herokuapp.com/rest/', 'extra': '', 'sid': '0', 'dir': '_i7/2' },
    { 'url': 'https://juice-shop.herokuapp.com/rest/2fa/', 'extra': '', 'sid': '0', 'dir': '_i7/3' },
    { 'url': 'https://juice-shop.herokuapp.com/redirect', 'extra': '', 'sid': '0', 'dir': '_i7/4' },
    { 'url': 'https://juice-shop.herokuapp.com/redirect?[0][\x27to\x27]=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm', 'extra': '', 'sid': '0', 'dir': '_i7/5' } ]
  },
  { 'severity': 0, 'type': 10401, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/rest/', 'extra': '', 'sid': '0', 'dir': '_i8/0' },
    { 'url': 'https://juice-shop.herokuapp.com/rest/2fa/', 'extra': '', 'sid': '0', 'dir': '_i8/1' },
    { 'url': 'https://juice-shop.herokuapp.com/redirect', 'extra': '', 'sid': '0', 'dir': '_i8/2' } ]
  },
  { 'severity': 0, 'type': 10205, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i9/0' } ]
  },
  { 'severity': 0, 'type': 10204, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': 'X-Content-Type-Options', 'sid': '0', 'dir': '_i10/0' },
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': 'X-Frame-Options', 'sid': '0', 'dir': '_i10/1' },
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': 'X-Recruiting', 'sid': '0', 'dir': '_i10/2' } ]
  },
  { 'severity': 0, 'type': 10203, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': '1.1 vegur', 'sid': '0', 'dir': '_i11/0' },
    { 'url': 'https://juice-shop.herokuapp.com/dataerasure/', 'extra': '1.1 vegur', 'sid': '0', 'dir': '_i11/1' },
    { 'url': 'https://juice-shop.herokuapp.com/profile/', 'extra': '1.1 vegur', 'sid': '0', 'dir': '_i11/2' },
    { 'url': 'https://juice-shop.herokuapp.com/rest/', 'extra': '1.1 vegur', 'sid': '0', 'dir': '_i11/3' } ]
  },
  { 'severity': 0, 'type': 10202, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': 'Cowboy', 'sid': '0', 'dir': '_i12/0' } ]
  },
  { 'severity': 0, 'type': 10101, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': '/C=US/O=Amazon/CN=Amazon RSA 2048 M02', 'sid': '0', 'dir': '_i13/0' } ]
  }
];

