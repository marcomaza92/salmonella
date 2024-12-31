## Falcon API

### Setup

#### Create virtual environment

```sh
python -m venv .venv
```

or

```sh
python3 -m venv .venv
```

#### Activate virtual environment

On Unix:

```sh
source .venv/bin/activate
```

On Windows:

```sh
source .venv/Scripts/activate
```

#### Install dependencies

```sh
pip install -r requirements.txt
```

#### Run the server

```sh
gunicorn --reload api:app
```

#### Open the API

Go to [localhost:8000](http://localhost:8000)

#### Endpoints

- `/`: welcome message
- `/todo`: connection to Supabase instance and a `todos` table
