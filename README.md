# Discord SMS Bot
A simple discord bot written in python for registering numbers and sending sms messages using [Twilio](https://www.twilio.com/) or [Messagebird](https://www.messagebird.com/en/) APIs.
## Main Workflow 🎢
![alt text](/assets/workflow.png "Title")
## How to run the code 🏃‍♂️

### Installation 🔧

You will need to install [Poetry](https://python-poetry.org/) to install project's dependencies

```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
```

Locate where Poetry is installed

```bash
$ whereis poetry
```

Copy and replace poetry's path to this line and added it at the end of the `.bashrc` file

```bash
$ export PATH="$HOME/.poetry/bin:$PATH"
```

## Installing project's dependencies 📚


Clone the repository

  ```bash
  $ git clone https://github.com/Arkemix30/school-payment-management-backend
  ```

Enter into project's root folder and run:

```bash
$ poetry install
```

It should create a `.venv` folder, generating a virtual enviroment with all project's dependencies

## How to run locally ⚙️
* First of all, you have to set all the environment variables, you can use the file: `sample.env` in the root folder as reference.

* To run the project, you need to activate the virtual environment.
  For that, you can run this command:

  ```bash
  $ poetry shell
  ```

* And finally, to run the server:

  ```bash
  $ python main.py
  ```

## Built with 🛠️

* [Discord.py](https://discordpy.readthedocs.io/en/stable/) - Python API wrapper for Discord.
* [Pydantic](https://pydantic-docs.helpmanual.io/) - Schema Data Validation
* [SQLModel](https://sqlmodel.tiangolo.com/) - Database ORM based in SQLAlchemy and Pydantic
* [Alembic](https://alembic.sqlalchemy.org/en/latest/front.html) - Database migration tool
* [Twilio SDK](https://www.twilio.com/docs/libraries/python) - The Twilio SMS Python Helper Library
* [Messagebird SDK](https://github.com/messagebird/python-rest-api) - The Messagebird Python SDK

## TODO ✅
- [x] Discord Command - Register Numbers
- [x] Discord Command - Unregister Numbers
- [x] Discord Command - Send SMS
- [x] DB - Register Numbers into DB
- [x] DB - Unregister Numbers from DB
- [x] DB - Insert Notification into DB when SMS is sent
- [x] Send SMS Using Twilio API
- [ ] Send SMS Using Messagebird API
---

README ⌨️ with ❤️ by [Arkemix30](https://github.com/Arkemix30) 😊
