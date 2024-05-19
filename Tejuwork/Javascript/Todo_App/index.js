let todos = [];

const todoForm = document.querySelector('.todo-form');
const todoInput = document.querySelector('.todo-input');
const todoItemsList = document.querySelector('.todo-items');

todoForm.addEventListener('submit', function(event) {
    event.preventDefault();
    addTodo(todoInput.value);
    todoInput.value = "";
    setAlertMessage("Todo item added");
});

function addTodo(todoItem) {
    const newTodo = {
        id: todos.length + 1,
        name: todoItem,
        completed: false
    };
    todos.push(newTodo);
    renderTodos();
    addToLocalStorage(todos);
}

function renderTodos() {
    todoItemsList.innerHTML = "";
    todos.forEach(function(todo) {
        const todoItem = document.createElement('li');
        todoItem.textContent = todo.name;
        if (todo.completed) {
            todoItem.classList.add('completed');
        }
        todoItem.addEventListener('dblclick', function() {
            toggle(todo.id);
        });
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', function() {
            deleteTodo(todo.id);
        });
        todoItem.appendChild(deleteButton);
        todoItemsList.appendChild(todoItem);
    });
}

function toggle(id) {
    todos.forEach(function(todo) {
        if (todo.id == id) {
            todo.completed = !todo.completed;
        }
    });
    addToLocalStorage(todos);
    renderTodos();
}

function deleteTodo(id) {
    todos = todos.filter(function(todo) {
        return todo.id != id;
    });
    addToLocalStorage(todos);
    renderTodos();
}

function addToLocalStorage(todos) {
    localStorage.setItem('todos', JSON.stringify(todos));
}

function getFromLocalStorage() {
    const storedTodos = localStorage.getItem('todos');
    if (storedTodos) {
        todos = JSON.parse(storedTodos);
        renderTodos();
    }
}

getFromLocalStorage();
