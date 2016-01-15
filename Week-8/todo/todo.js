'use strict';

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var todoContainer = document.querySelector('.todo-container');
var todoInput = document.querySelector('.todo-input');
var todoButton = document.querySelector('.todo-button');
var deleteButton = document.querySelector('.delete-button');
var updateButton = document.querySelector('.update-button');
var elementId = 0;
var elementText = '';

var listCallback = function (response) {
  var todoArray = JSON.parse(response);
  todoArray.forEach(function(todoItem) {
    var newTodoItem = document.createElement('p');
    highlighter(newTodoItem);
    if (todoItem.completed) {
      newTodoItem.innerHTML = todoItem.text + '    &#10004';
    } else {
      newTodoItem.innerText = todoItem.text;
    }
    newTodoItem.setAttribute('id', todoItem.id);
    todoContainer.appendChild(newTodoItem);
  });
}

function highlighter(element) {
  element.addEventListener('click', function() {
    if (document.querySelector('.highlighted') != null) {
      document.querySelector('.highlighted').classList.remove('highlighted');
    }
    element.classList.add('highlighted');
  });
}

var refresh = function() {
  todoContainer.innerText = '';
  createRequest('GET', url, {}, listCallback);
}

var createTodoCallback = function(response) {
  refresh();
}

todoButton.addEventListener('click', function() {
  var todoEntered = todoInput.value;
  var newTodo = JSON.stringify({text: todoEntered, completed: false});
  createRequest('POST', url, newTodo, createTodoCallback);
  todoInput.value = '';
});

function deleteTodo (id) {
  createRequest('DELETE', url + '/' + id, undefined, refresh);
}

function setStatus(id) {
  createRequest('PUT', url + '/' + id, JSON.stringify({text: elementText, completed: true}), refresh);
}

todoContainer.addEventListener('click', function(event) {
  console.log(event.target.id);
  elementId = event.target.id;
  elementText = event.target.innerText;
});

deleteButton.addEventListener('click', function() {
  deleteTodo(elementId);
});

updateButton.addEventListener('click', function() {
  setStatus(elementId);
});

refresh();
