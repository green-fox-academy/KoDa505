'use strict';

function createRequest (method, url, data, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open(method, url);
  probaRequest.setRequestHeader('Content-Type', 'application/json');
  probaRequest.send(data);
  probaRequest.onreadystatechange = function() {
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  }
}
