# backend_coding_challenge
This project is about creating a RestAPI using the technology of my choice, Django and its powerful app, restframework.

## Setup the environment
So to test this project on your own, you have :
- I couldn't upload the venv here (it has a size that Github can't handle), but fortunately you can create one, you can visit the link below for more information : 
```bash
https://realpython.com/lessons/creating-virtual-environment/
```
The libraries you will need for this project are : django, requests, django-restframework, pymysql using the command : 
```bash 
pip install <lib_name>
``` 
- to activate the virtual environment : open the command line on your computer and go inside this folder (backend_coding_challenge) then type : 
```bash
env\Scripts\activate.bat
```
- next go inside MyAPI_Project folder and fix the database settings there (settings.py)
- then go back to the command line you opened earlier - ensure that the local server, such as XAMPP, is already running -, and type : 
```bash
python manage.py makemigrations
```
Once it's done, type : 
```bash
python manage.py migrate
```
Now that the database is set, run the server:
```bash
python manage.py runserver
```
## Get the data
First you have to go to the browser, and visit the index view, the URL will be like : 
```bash
127.0.0.1:8000/index
```
After you hit enter, you will be redirected to another view - /repo - where repositories with their names, urls and languages are listed.
## Number of repos using this language
Then you can go to 
```bash 
127.0.0.1:8000/repo/get_count_by_lang
```
It will return a JSON response like:
```bash
[
    {
        "language": "Go",
        "dcount": 1
    },
    {
        "language": "C#",
        "dcount": 1
    },

```
## The list of repos using the language
Finally, go to :
```bash
http://127.0.0.1:8000/repo/get_list_repo_by_lang
```
to have for each language, the URL of the repository using it.

Let's take a look at the result:
```bash
{
    "Go": [
        {
            "url": "https://api.github.com/repos/achannarasappa/ticker"
        }
    ],
    "C#": [
        {
            "url": "https://api.github.com/repos/wesdoyle/design-patterns-explained-with-food"
        }
    ],
    "Python": [
        {
            "url": "https://api.github.com/repos/ml-tooling/best-of-python"
        },
        {
            "url": "https://api.github.com/repos/sdushantha/wifi-password"
        },
        {
            "url": "https://api.github.com/repos/yuchenlin/rebiber"
        },
```

Once you finish the test, don't forget to deactivate the virtual environment so it won't consume your laptop resources : 
```bash
env\Scripts\deactivate.bat
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

