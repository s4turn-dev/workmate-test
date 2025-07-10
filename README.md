## О проекте

Проект представляет собой решение тестового задания на Junior Python Developer @ Workmate.

<details>
    <summary>ТЗ</summary>
    https://docs.google.com/document/u/0/d/1nraUeVCkbsyvjNvMAWAwgrn7w3DXHsQf15QS1eZ2F1U/mobilebasic#heading=h.or54d8e34zbk
</details>

## Содержание

1. [Для Workmate](#для-workmate)
2. [Установка и запуск](#установка-и-запуск)
3. [Примеры запуска](#примеры-запуска)

## Для Workmate

Привет! Классное тестовое, было интересно выполнить. Несложное технически, но предлагающее простор для проектирования и архитектурных моментов. Было над чем подумать, короче.

### По поводу AI

Я пользовался нейронками.

В начале выполнения тестового я представлял, как гордо будет красоваться фраза "ни одна строчка кода не была написана ИИ", но впоследствии это немного изменилось. 

Но копипаста в проекте действительно нет. Я консультировался на предмет архитектурных решений, бест практисес и всяких организационных моментов; нет кода, за который я не смогу пояснить.

ИИ наступил, и он останется, поэтому уметь им пользоваться становится существенным навыком. По [ссылке](https://chatgpt.com/share/686d7b70-4790-800b-9ae0-6342ef22bdde) вы можете ознакомиться с содержанием чата с нейронкой, к которому я обращался в процессе выполнения тестового.

## Установка и запуск

Поддерживаемые команды:

- `--aggregation '[COLUMN]=min|max|avg`
- `--filter '[COLUMN]</>/=[VALUE]'`
- `--order-by '[COLUMN]=asc|desc'`

Склонируйте репозиторий:

```sh
git clone git@github.com:s4turn-dev/workmate-test.git
cd workmate-test
```

### uv

Запуск программы:

```sh
uv run src/main.py --file путь/до/файла.csv
```

Тесты:

```sh
uv run pytest
```

### pip

Создайте и активируйте виртуальное окружение, установите зависимости:

```sh
python -m venv venv
source venv/bin/activate
pip install .
```

Запустите:

```sh
python src/main.py --file путь/до/файла.csv
```

Тесты:

```sh
pytest
```

## Примеры запуска

```shell-session
$ uv run src/main.py --file products.csv 
name              brand      price    rating
----------------  -------  -------  --------
iphone 15 pro     apple        999       4.9
galaxy s23 ultra  samsung     1199       4.8
redmi note 12     xiaomi       199       4.6
iphone 14         apple        799       4.7
galaxy a54        samsung      349       4.2
poco x5 pro       xiaomi       299       4.4
iphone se         apple        429       4.1
galaxy z flip 5   samsung      999       4.6
redmi 10c         xiaomi       149       4.1
iphone 13 mini    apple        599       4.5
```

Filter:
```shell-session
$ uv run src/main.py --file products.csv --where 'brand=apple'
name            brand      price    rating
--------------  -------  -------  --------
iphone 15 pro   apple        999       4.9
iphone 14       apple        799       4.7
iphone se       apple        429       4.1
iphone 13 mini  apple        599       4.5
```

Aggregation:
```shell-session
$ uv run src/main.py --file products.csv --aggregation 'rating=min'
name       brand      price    rating
---------  -------  -------  --------
iphone se  apple        429       4.1
redmi 10c  xiaomi       149       4.1
```

Order By:
```shell-session
$ uv run src/main.py --file products.csv --where 'brand=samsung' --order-by 'price=asc'
name              brand      price    rating
----------------  -------  -------  --------
galaxy a54        samsung      349       4.2
galaxy z flip 5   samsung      999       4.6
galaxy s23 ultra  samsung     1199       4.8
```
