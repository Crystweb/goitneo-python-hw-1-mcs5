"""
Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати 
відповідно до введеної команди.
У цій домашній роботі зосередимося на інтерфейсі самого бота.  Найпростіший і найзручніший на початковому етапі розробки 
інтерфейс - це консольний застосунок CLI (Command Line Interface). CLI достатньо просто реалізувати. Будь-який CLI 
складається з трьох основних елементів:
    -> Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та 
    модифікаторів команд.
    -> Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
    -> Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві 
    відповіді від функції - handler-а.
На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, 
змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, 
скористаємося словником. У словнику будемо зберігати ім'я користувача як ключ і номер телефону як значення.
"""