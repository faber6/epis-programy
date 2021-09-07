# epis-programy
#### Programy API for Epis Bot
#### Hosting on [Heroku](epis-programy.herokuapp.com)

## Installations
1. Install requirements from requirements.txt:
  * `pip install -r requirements.txt`
2. Edit files in './config'.
2. Run:
  * `python main.py`

## Usage
Request the API:
```python
api = requests.get(f'http://epis-programy.herokuapp.com/context/<random_string>/question/[<question>]')
```
Get response:
```python
if api.status_code == 200:
 load = api.json()
 response = load['success']
 print(response)
```
Args:
* random_string: a conversation id will keep the answer follow the conversation
* question: a question to ask

