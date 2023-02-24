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
  { 'mime': 'image/x-ms-bmp', 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/assets/public/favicon_js.ico', 'dir': '_m2/0', 'linked': 2, 'len': 15086 } ]
  },
  { 'mime': 'text/css', 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/styles.css', 'dir': '_m3/0', 'linked': 2, 'len': 400000 } ]
  }
];

var issue_samples = [
  { 'severity': 3, 'type': 40401, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/polyfills.js', 'extra': 'server-side JavaScript source', 'sid': '0', 'dir': '_i0/0' } ]
  },
  { 'severity': 3, 'type': 40201, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': '//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.css', 'sid': '0', 'dir': '_i1/0' },
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': '//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.js', 'sid': '0', 'dir': '_i1/1' },
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': '//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js', 'sid': '0', 'dir': '_i1/2' } ]
  },
  { 'severity': 1, 'type': 20301, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/assets/public', 'extra': '', 'sid': '0', 'dir': '_i2/0' } ]
  },
  { 'severity': 1, 'type': 20101, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i3/0' },
    { 'url': 'https://juice-shop.herokuapp.com/polyfills.js', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i3/1' },
    { 'url': 'https://juice-shop.herokuapp.com/vendor.js', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i3/2' },
    { 'url': 'https://juice-shop.herokuapp.com/assets', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i3/3' },
    { 'url': 'https://juice-shop.herokuapp.com/assets/i18n', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i3/4' },
    { 'url': 'https://juice-shop.herokuapp.com/assets/public', 'extra': 'XSS injection', 'sid': '0', 'dir': '_i3/5' } ]
  },
  { 'severity': 0, 'type': 10901, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/assets/i18n', 'extra': '', 'sid': '0', 'dir': '_i4/0' } ]
  },
  { 'severity': 0, 'type': 10205, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i5/0' } ]
  },
  { 'severity': 0, 'type': 10204, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': 'X-Content-Type-Options', 'sid': '0', 'dir': '_i6/0' },
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': 'X-Frame-Options', 'sid': '0', 'dir': '_i6/1' },
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': 'X-Recruiting', 'sid': '0', 'dir': '_i6/2' } ]
  },
  { 'severity': 0, 'type': 10203, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': '1.1 vegur', 'sid': '0', 'dir': '_i7/0' } ]
  },
  { 'severity': 0, 'type': 10202, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': 'Cowboy', 'sid': '0', 'dir': '_i8/0' } ]
  },
  { 'severity': 0, 'type': 10101, 'samples': [
    { 'url': 'https://juice-shop.herokuapp.com/', 'extra': '/C=US/O=Amazon/CN=Amazon RSA 2048 M02', 'sid': '0', 'dir': '_i9/0' } ]
  }
];

