# Sprint_6 — Автотесты для сервиса «Самокат»

Учебный проект по автоматизации тестирования сайта
[«Самокат»](https://qa-scooter.praktikum-services.ru/) на Python + Selenium
с использованием паттерна Page Object и Allure для отчётов.

## Что проверяется

- **FAQ на главной** — 8 вопросов аккордеона, ответы сверяются с эталонными.
- **Оформление заказа** — два позитивных сценария:
  через верхнюю кнопку «Заказать» и через нижнюю.
- **Редиректы по логотипам** — клик по логотипу «Самоката» ведёт на главную,
  клик по логотипу Яндекса открывает Дзен.

## Стек

- Python 3.10+
- Selenium 4.21
- pytest 8.2
- allure-pytest — для формирования отчётов

## Структура проекта

```
Sprint_6/
├── conftest.py                 # Фикстура драйвера
├── data.py                     # Эталонные тексты вопросов и ответов
├── helpers.py                  # Генерация случайных данных для заказа
├── urls.py                     # URL-адреса
├── pytest.ini                  # Настройки pytest
├── requirements.txt            # Зависимости
│
├── locators/                   # Локаторы элементов
│   ├── header_footer_locators.py
│   ├── main_page_locators.py
│   └── order_page_locators.py
│
├── pages/                      # Page Object
│   ├── base_page.py            # Общие методы для всех страниц
│   ├── header_footer_page.py
│   ├── main_page.py
│   └── order_page.py
│
└── tests/                      # Тесты
    ├── test_main_page.py       # FAQ
    ├── test_order_page.py      # Оформление заказа
    └── test_redirect.py        # Редиректы по логотипам
```

## Установка

1. Клонировать репозиторий:

   ```bash
   git clone git@github.com:TheCrazyMakc/Sprint_6.git
   cd Sprint_6
   ```

2. Создать и активировать виртуальное окружение:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Убедиться, что установлен **Google Chrome** — драйвер Selenium 4.x
   подтянет сам.

## Запуск тестов

Все тесты:

```bash
pytest
```

С подробным выводом:

```bash
pytest -v
```

Только конкретный файл:

```bash
pytest tests/test_order_page.py
```

Только конкретный тест:

```bash
pytest tests/test_main_page.py::TestMainPage::test_questions_and_answers
```

## Allure-отчёт

Запустить тесты с сохранением результатов:

```bash
pytest --alluredir=allure-results
```

Сгенерировать и открыть отчёт:

```bash
allure serve allure-results
```

⚠️ Для работы отчёта нужна установленная утилита **Allure CLI**
([инструкция](https://docs.qameta.io/allure/#_installing_a_commandline)).

## Как устроен проект

- **Page Object** — каждая страница описана отдельным классом
  (`MainPage`, `OrderPage`, `HeaderFooterPage`). Тесты работают
  через методы этих классов, не обращаясь к локаторам напрямую.
- **BasePage** — общий родитель для всех страниц, содержит
  переиспользуемые методы: клики с ожиданием, скроллы, форматирование
  параметризованных локаторов, работа с вкладками.
- **Locators** — локаторы вынесены в отдельные модули по страницам.
  Параметризованные локаторы (например, `accordion__heading-{0}`)
  описаны как шаблоны с плейсхолдером.
- **data.py** — эталонные тексты вопросов и ответов для FAQ.
- **helpers.py** — генерация случайных данных для формы заказа,
  чтобы тесты не были привязаны к конкретному человеку.

## Особенности

- Тесты **независимы** — фикстура `driver` создаёт новый браузер
  для каждого теста (scope `function`).
- Тесты **не привязаны к порядку** — можно запускать любой в отдельности.
- Данные для заказа **генерируются случайно** через `helpers.py`.
- Отчёты **читаемые** — каждый шаг обёрнут в `allure.step`.

## Автор

Учебный проект в рамках курса «Автоматизатор тестирования на Python».