#!/bin/bash

set -e  # Прекратить выполнение при любой ошибке

echo "=== Запуск тестов ==="
pytest tests/ -v --alluredir=./allure-results || { echo "Тесты упали!"; exit 1; }

echo "=== Генерация отчёта ==="
allure generate ./allure-results -o ./allure-report --clean

echo "=== Готово! Отчёт сохранён в allure-report/ ==="
allure open ./allure-report