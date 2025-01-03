<h1 align="center"> Smart IDS </h1>

<p align="center">
<a href="https://github.com/light-hat/smart_ids/actions"><img alt="Unit test status" src="https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white"></a>
<a href="https://github.com/light-hat/smart_ids/actions"><img alt="Unit test status" src="https://github.com/light-hat/smart_ids/workflows/Unit%20testing/badge.svg"></a>
<a href="https://github.com/light-hat/smart_ids/actions"><img alt="Pylint status" src="https://github.com/light-hat/smart_ids/workflows/Pylint/badge.svg"></a>
<a href="https://github.com/light-hat/smart_ids/actions"><img alt="Bandit SAST status" src="https://github.com/light-hat/smart_ids/workflows/SAST/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

<p align="center">
Асинхронный API для обнаружения атак в дампах сетевого трафика методами машинного обучения.
</p>

<h2 align="center"> Стек </h2>

<p align="center">

<img src="https://img.shields.io/badge/nVIDIA-%2376B900.svg?style=for-the-badge&logo=nVIDIA&logoColor=white">
<img src="https://img.shields.io/badge/cuda-000000.svg?style=for-the-badge&logo=nVIDIA&logoColor=green">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray">
<img src="https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4">
<img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white">
<img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white">
<img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white">
<img src="https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white">
<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">

</p>

## Содержание

<!-- TOC -->
  * [Стек](#стек)
  * [Содержание](#содержание)
  * [Пару слов о модели](#пару-слов-о-модели)
  * [Требования](#требования)
    * [Аппаратное окружение](#аппаратное-окружение)
    * [Программное окружение](#программное-окружение)
  * [Развёртывание](#развёртывание)
    * [Preflight](#preflight)
    * [Конфигурирование](#конфигурирование)
    * [Запуск проекта](#запуск-проекта)
  * [Эксплуатация](#эксплуатация)
    * [Документация API](#документация-api)
    * [Административная панель](#административная-панель)
    * [Мониторинг](#мониторинг)
<!-- TOC -->

## Пару слов о модели

Для инференса взята модель [rdpahalavan/bert-network-packet-flow-header-payload](https://huggingface.co/rdpahalavan/bert-network-packet-flow-header-payload) на Hugging Face.

## Требования

### Аппаратное окружение

| Требование | Минимум         | Рекомендуется  |
|------------|-----------------|----------------|
| CPU        | `6 ядер`        | `12 ядер`      |
| RAM        | `16 Гб`         | `32 Гб`        |
| Диск       | `80 Гб`         | `150 Гб`       |
| GPU        | `8-16 Гб VRAM`  | `32 Гб VRAM`   |

### Программное окружение

> [!TIP]
> Операционная система в принципе не имеет значения, если соблюдены требования к программному и аппаратному окружению.

| Требование               | Минимальная версия | Рекомендуемая версия           |
|--------------------------|--------------------|--------------------------------|
| Docker                   | `19.03`            | `20.10 или выше`               |
| Docker Compose           | `1.27`             | `1.29 или выше`                |
| NVIDIA драйверы          | `418.87`           | `последняя стабильная версия`  |
| CUDA                     | `11.0`             | `последняя стабильная версия`  |
| NVIDIA Container Toolkit | `1.0`              | `последняя стабильная версия`  |

## Развёртывание

> [!NOTE]
> Тестирование проводилось на сервере с Ubuntu 22.04 с GPU Tesla T4.

### Подготовка сервера

...

```shell
dpkg -l | grep nvidia-container-toolkit
```

<details>
  <summary>👀 Что примерно должно быть в ответе</summary>

<hr />

```
ii  nvidia-container-toolkit          1.17.3-1          amd64     NVIDIA Container toolkit
ii  nvidia-container-toolkit-base     1.17.3-1          amd64     NVIDIA Container Toolkit Base

```

<hr />

</details>

> [!TIP]
> Если в этом ответе пусто, вот [мануал](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) как установить NVIDIA Container Toolkit.

### Конфигурирование

Для начала клонируйте репозиторий:

```shell
git clone https://github.com/light-hat/smart_ids
cd smart_ids
```

В корне репозитория создайте `.env` файл со следующим содержимым:

```
API_URL=127.0.0.1
API_PORT=80
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=shop_database
GF_SECURITY_ADMIN_PASSWORD=admin
GF_SECURITY_ADMIN_USER=admin
```

Переменные окружения в конфигурации:

- `API_URL`: адрес, на котором будет развёрнут сервис;

- `API_PORT`: порт, на котором будет принимать запросы сервис;

- `POSTGRES_HOST`: хост базы данных (имя сервиса в стеке приложений);

- `POSTGRES_PORT`: порт базы данных;

- `POSTGRES_USER`: пользователь базы данных;

- `POSTGRES_PASSWORD`: пароль от базы данных;

- `POSTGRES_DB`: имя базы данных, используемой сервисом;

- `GF_SECURITY_ADMIN_PASSWORD`: имя пользователя для авторизации в Grafana;

- `GF_SECURITY_ADMIN_USER`: пароль для авторизации в Grafana.

### Запуск проекта

Запустите стек приложений на Docker следующей командой:

```shell
docker-compose up -d --build
```

<details>
  <summary>👀 Как выглядит здоровый лог при запуске</summary>

<hr />

Лог инференса:

```shell
docker-compose logs triton
```

```text
Лог
```

Лог API:

```shell
docker-compose logs api
```

```text
ЛОг
```

Лог воркера:

```shell
docker-compose logs worker
```

```text
Logg
```

<hr />

</details>

## Эксплуатация

### Документация API

`TODO`: вставить фотку сваггера по готовности.

API задокументирован при помощи Swagger (`drf-spectacular`).

Тестирование API: `http://127.0.0.1/swagger/`

YAML: `http://127.0.0.1/schema/`

### Административная панель

`TODO`: вставить фотки админки по готовности.

Админка сервиса доступна по адресу `http://127.0.0.1/admin`.

Учётные данные для первого входа: `admin:admin`.

> [!IMPORTANT]
> Учётные данные рекомендуется сменить сразу после развёртывания на более устойчивые.

### Мониторинг

`TODO`: описать работу с системой мониторинга по готовности
