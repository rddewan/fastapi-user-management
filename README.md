
### VS Code Setup
1. Install Python extension : https://marketplace.windsurf.com/vscode/item?itemName=ms-python.python
2. Install Pylance extension : https://marketplace.windsurf.com/vscode/item?itemName=ms-python.vscode-pylance
3. Install autoDocstring - Python Docstring Generator :https://marketplace.windsurf.com/vscode/item?itemName=njpwerner.autodocstring
4. Install Code Spell Checker :https://marketplace.windsurf.com/vscode/item?itemName=streetsidesoftware.code-spell-checker
5. Install Pyright : https://marketplace.windsurf.com/vscode/item?itemName=Codeium.windsurfPyright
6. Install Black Formatter : https://marketplace.windsurf.com/vscode/item?itemName=ms-python.black-formatter

### To Activate Python Virtual Environment
* DOC: https://fastapi.tiangolo.com/virtual-environments/#__tabbed_2_2

* create a virtual environment
```bash
python -m venv .venv
```

* Mac/ Linux
```bash
source .venv/bin/activate
```

* Windows Bash
```bash
source .venv/Scripts/activate
```

* Windows PowerShell
```bash
.venv\Scripts\Activate.ps1
```

### To Deactivate Python Virtual Environment

```bash
deactivate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```


### Run the Application
```bash
fastapi dev
```

### Run Postgres DB in docker
1. Run Postgres DB container
```bash
docker compose -f docker-compose-dev.yaml --env-file .env up -d
```

### Setup the alembic
```bash
alembic init alembic
```

### alembic commands
```bash
# create a new migration
alembic revision --autogenerate -m "message"

# apply migrations
alembic upgrade head
```
