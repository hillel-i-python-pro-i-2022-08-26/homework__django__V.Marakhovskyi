# Homework # 11. (Contacts and commands)

---
![Main workflow](https://github.com/hillel-i-python-pro-i-2022-08-26/homework__django__V.Marakhovskyi/actions/workflows/main-workflow.yml/badge.svg?branch=models_commands)
![IDE](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
![REPO](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![DJANGO](https://www.djangoproject.com/m/img/badges/djangomade124x25.gif)
## 👨‍💻 Homework

General features o Django framework. Adding models and commands.

### ▶️ Run

Make all actions needed for run homework from zero.

```shell
make homework-i-run
```

### 🛣️ Install pre-commit and dependencies:
```shell
make init-dev
```


### 🧽🪣 Purge

Delete all created artifacts from run.

```shell
make homework-i-purge
```
### ♻️ Make migrations

Create a migrations

```shell
make migrations
```
### 💾 Migrate

Apply a migration

```shell
make migrate
```
### 📗 Command: generate contacts

Default value - 50 contacts

```shell
make generate-contacts
```
For custom generation with desired amount use a terminal command:
```shell
python manage.py generate_contacts --amount <desired qtty>
```
### 📕 Command: delete contacts

Deleting all auto-generated contacts

```shell
make delete-contacts
```