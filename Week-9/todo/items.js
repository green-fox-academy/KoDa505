"use-strict"

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '',
  database : 'todo'
});

connection.connect();

module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems,
  update: updateItem
};

function addItem(attributes) {
  connection.query('INSERT INTO todo SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  })
}

function removeItem(id, callback) {
  connection.query('DELETE FROM `todo` WHERE `todo_id`= ?', id, function(err, res) {
      if (err) throw err;
      console.log(res);
      callback(res);
    });
}

function getItem(attributes) {
  connection.query('SELECT * FROM todo', function(err, result) {
    if (err) throw err;
    console.log(result);
  });
}

function updateItem(id, cb) {
  connection.query('UPDATE todo SET completed = \'true\' WHERE todo_id = ?', id, function(err, result) {
    if (err) throw err;
    cb(result);
  });
}

function allItems(cb) {
  connection.query('SELECT * FROM todo', function(err, result) {
    if (err) throw err;
    cb(result);
  });
}


var TodoItem = function () {
  this.id = nextId();
  this.text = "";
  this.completed = false;
}

TodoItem.prototype.update = function(attributes) {
  this.text = attributes.text || "";
  this.completed = !!attributes.completed;
};

var currId = 0;
function nextId() {
  return ++currId;
}

var items = {};

// function getItem(id) {
//   return items[id];
// }
