var mime_samples = [
  { 'mime': 'application/javascript', 'samples': [
    { 'url': 'http://localhost:3000/main.js', 'dir': '_m0/0', 'linked': 2, 'len': 397636 },
    { 'url': 'http://localhost:3000/polyfills.js', 'dir': '_m0/1', 'linked': 2, 'len': 54568 },
    { 'url': 'http://localhost:3000/runtime.js', 'dir': '_m0/2', 'linked': 2, 'len': 3228 },
    { 'url': 'http://localhost:3000/vendor.js', 'dir': '_m0/3', 'linked': 2, 'len': 400000 } ]
  },
  { 'mime': 'application/xhtml+xml', 'samples': [
    { 'url': 'http://localhost:3000/', 'dir': '_m1/0', 'linked': 2, 'len': 1987 } ]
  },
  { 'mime': 'image/x-ms-bmp', 'samples': [
    { 'url': 'http://localhost:3000/assets/public/favicon_js.ico', 'dir': '_m2/0', 'linked': 2, 'len': 38 } ]
  },
  { 'mime': 'text/css', 'samples': [
    { 'url': 'http://localhost:3000/styles.css', 'dir': '_m3/0', 'linked': 2, 'len': 400000 } ]
  },
  { 'mime': 'text/html', 'samples': [
    { 'url': 'http://localhost:3000/dataerasure/', 'dir': '_m4/0', 'linked': 1, 'len': 4016 },
    { 'url': 'http://localhost:3000/profile/', 'dir': '_m4/1', 'linked': 1, 'len': 1325 },
    { 'url': 'http://localhost:3000/rest/', 'dir': '_m4/2', 'linked': 1, 'len': 3944 },
    { 'url': 'http://localhost:3000/rest/2fa/status/', 'dir': '_m4/3', 'linked': 1, 'len': 972 } ]
  },
  { 'mime': 'text/plain', 'samples': [
    { 'url': 'http://localhost:3000/redirect?to=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm', 'dir': '_m5/0', 'linked': 1, 'len': 88 } ]
  }
];

var issue_samples = [
  { 'severity': 3, 'type': 40401, 'samples': [
    { 'url': 'http://localhost:3000/polyfills.js', 'extra': 'server-side JavaScript source', 'sid': '0', 'dir': '_i0/0' },
    { 'url': 'http://localhost:3000/redirect?to=.../https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm', 'extra': 'CVS RCS data', 'sid': '0', 'dir': '_i0/1' } ]
  },
  { 'severity': 3, 'type': 40302, 'samples': [
    { 'url': 'http://localhost:3000/redirect?to=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000040v746478\x3e', 'extra': 'text/plain', 'sid': '0', 'dir': '_i1/0' } ]
  },
  { 'severity': 3, 'type': 40201, 'samples': [
    { 'url': 'http://localhost:3000/', 'extra': '//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.css', 'sid': '0', 'dir': '_i2/0' },
    { 'url': 'http://localhost:3000/', 'extra': '//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.js', 'sid': '0', 'dir': '_i2/1' },
    { 'url': 'http://localhost:3000/', 'extra': '//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js', 'sid': '0', 'dir': '_i2/2' } ]
  },
  { 'severity': 2, 'type': 30701, 'samples': [
    { 'url': 'http://localhost:3000/', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/0' },
    { 'url': 'http://localhost:3000/dataerasure/./', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/1' },
    { 'url': 'http://localhost:3000/profile/./', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/2' },
    { 'url': 'http://localhost:3000/1', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/3' },
    { 'url': 'http://localhost:3000/1?ht.iconName=function', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/4' },
    { 'url': 'http://localhost:3000/main.js', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/5' },
    { 'url': 'http://localhost:3000/polyfills.js', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/6' },
    { 'url': 'http://localhost:3000/redirect/.htaccess.aspx--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000033v746478\x3e', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/7' },
    { 'url': 'http://localhost:3000/runtime.js', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/8' },
    { 'url': 'http://localhost:3000/styles.css', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/9' },
    { 'url': 'http://localhost:3000/vendor.js', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/10' },
    { 'url': 'http://localhost:3000/assets/--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000004v746478\x3e', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/11' },
    { 'url': 'http://localhost:3000/assets/i18n/.htaccess.aspx--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000021v746478\x3e', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/12' },
    { 'url': 'http://localhost:3000/assets/public/.htaccess.aspx--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000073v746478\x3e', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/13' },
    { 'url': 'http://localhost:3000/assets/public/favicon_js.ico', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i3/14' } ]
  },
  { 'severity': 1, 'type': 20301, 'samples': [
    { 'url': 'http://localhost:3000/assets/public', 'extra': '', 'sid': '0', 'dir': '_i4/0' } ]
  },
  { 'severity': 0, 'type': 10901, 'samples': [
    { 'url': 'http://localhost:3000/rest/2fa/', 'extra': '', 'sid': '0', 'dir': '_i5/0' },
    { 'url': 'http://localhost:3000/assets/i18n', 'extra': '', 'sid': '0', 'dir': '_i5/1' } ]
  },
  { 'severity': 0, 'type': 10802, 'samples': [
    { 'url': 'http://localhost:3000/redirect?to=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm', 'extra': 'text/plain', 'sid': '0', 'dir': '_i6/0' } ]
  },
  { 'severity': 0, 'type': 10403, 'samples': [
    { 'url': 'http://localhost:3000/dataerasure/', 'extra': '', 'sid': '0', 'dir': '_i7/0' },
    { 'url': 'http://localhost:3000/profile/', 'extra': '', 'sid': '0', 'dir': '_i7/1' },
    { 'url': 'http://localhost:3000/rest/', 'extra': '', 'sid': '0', 'dir': '_i7/2' },
    { 'url': 'http://localhost:3000/rest/2fa/', 'extra': '', 'sid': '0', 'dir': '_i7/3' },
    { 'url': 'http://localhost:3000/rest/2fa/disable/', 'extra': '', 'sid': '0', 'dir': '_i7/4' },
    { 'url': 'http://localhost:3000/rest/2fa/status/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i7/5' },
    { 'url': 'http://localhost:3000/redirect', 'extra': '', 'sid': '0', 'dir': '_i7/6' },
    { 'url': 'http://localhost:3000/redirect?[0][\x27to\x27]=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm', 'extra': '', 'sid': '0', 'dir': '_i7/7' } ]
  },
  { 'severity': 0, 'type': 10402, 'samples': [
    { 'url': 'http://localhost:3000/rest/2fa/status/', 'extra': '', 'sid': '0', 'dir': '_i8/0' } ]
  },
  { 'severity': 0, 'type': 10401, 'samples': [
    { 'url': 'http://localhost:3000/rest/', 'extra': '', 'sid': '0', 'dir': '_i9/0' },
    { 'url': 'http://localhost:3000/rest/2fa/', 'extra': '', 'sid': '0', 'dir': '_i9/1' },
    { 'url': 'http://localhost:3000/rest/2fa/disable/', 'extra': '', 'sid': '0', 'dir': '_i9/2' },
    { 'url': 'http://localhost:3000/redirect', 'extra': '', 'sid': '0', 'dir': '_i9/3' } ]
  },
  { 'severity': 0, 'type': 10205, 'samples': [
    { 'url': 'http://localhost:3000/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i10/0' },
    { 'url': 'http://localhost:3000/rest/2fa/status/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i10/1' } ]
  },
  { 'severity': 0, 'type': 10204, 'samples': [
    { 'url': 'http://localhost:3000/', 'extra': 'X-Content-Type-Options', 'sid': '0', 'dir': '_i11/0' },
    { 'url': 'http://localhost:3000/', 'extra': 'X-Frame-Options', 'sid': '0', 'dir': '_i11/1' },
    { 'url': 'http://localhost:3000/', 'extra': 'X-Recruiting', 'sid': '0', 'dir': '_i11/2' } ]
  }
];

