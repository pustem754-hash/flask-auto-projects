let display = document.getElementById('result');
let history = [];

function appendToDisplay(value) {
 if (value === '/') {
 display.value += '/';
 } else if (value === '*') {
 display.value += '*';
 } else {
 display.value += value;
 }
}

function clearDisplay() {
 display.value = '';
}

function deleteLast() {
 display.value = display.value.slice(0, -1);
}

function calculate() {
 const expression = display.value;
 if (!expression) return;
 
 fetch('/calculate', {
 method: 'POST',
 headers: {
 'Content-Type': 'application/json',
 },
 body: JSON.stringify({expression: expression})
 })
 .then(response => response.json())
 .then(data => {
 if (data.error) {
 alert('Ошибка: ' + data.error);
 } else {
 display.value = data.result;
 addToHistory(expression + ' = ' + data.result);
 }
 })
 .catch(error => {
 alert('Ошибка соединения');
 });
}

function addToHistory(calculation) {
 history.unshift(calculation);
 if (history.length > 10) {
 history.pop();
 }
 updateHistoryDisplay();
}

function updateHistoryDisplay() {
 const historyList = document.getElementById('history-list');
 historyList.innerHTML = '';
 
 history.forEach(item => {
 const div = document.createElement('div');
 div.className = 'history-item';
 div.textContent = item;
 historyList.appendChild(div);
 });
}

// Поддержка клавиатуры
document.addEventListener('keydown', function(event) {
 const key = event.key;
 
 if (key >= '0' && key <= '9' || key === '.' || key === '+' || key === '-' || key === '*' || key === '/' || key === '(' || key === ')') {
 appendToDisplay(key);
 } else if (key === 'Enter' || key === '=') {
 calculate();
 } else if (key === 'Escape') {
 clearDisplay();
 } else if (key === 'Backspace') {
 deleteLast();
 }
});