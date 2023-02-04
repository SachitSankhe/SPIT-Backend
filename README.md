# SPIT-Backend
Backend repo for SPIT-Hackathon

### Installation

1) First [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) it on your local Machine.

2) Then [create](https://docs.djangoproject.com/en/3.2/intro/contributing/) a virtual environment 

```
py -m venv YOUR_VIRTUAL_ENV_NAME
```
or
```
python -m YOUR_VIRTUAL_ENV_NAME
```
Then Activate the virtual env by running the file at  ```YOUR_VIRTUAL_ENV_NAME/Scripts/activate```

3) Then cd into server.(Check which interpreter has been selected at the right-side bottom of vscode.)

4) Then install all the requirements from requirements.txt
```
pip install -r requirements.txt
```

5) Then create a env file in inner server folder(folder in which settings.py is present) and copy paste entire content of .env.example in that same folder.

6) Fill the respective values in .env file .For getting App Passwords for your email Checkout ->https://support.google.com/accounts/answer/185833?hl=en

7) Finally run the server and see the results.( make your pwd as the folder where manage.py exists and then execute command 

```
py manage.py runserver
``` 
or 
```
python manage.py runserver
```
