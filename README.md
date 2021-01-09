# SocialBuddy

SocialBuddy is a <b>Twitter Bot</b>. By using this you can post <b>random jokes or memes</b> with a single click.

### Demo
https://socialbuddy.herokuapp.com/

<br>

### Setup
##### Step 1 
Download the project files.
<br>
```git clone https://github.com/Shahnwazh170/socialbuddy.git```

##### Step 2
Create a env_variables.py in the root directory of the project.
Add the following variables 
```
#Collect your Api and Token key from your developer twitter account. 

API_KEY = "XXXXXXXXXXXXXXXX"
API_KEY_SECRET = "XXXXXXXXXXXXXXXX"
ACCESS_TOKEN = "XXXXXXXXXXXXXXXX"
ACCESS_TOKEN_SECRET = "XXXXXXXXXXXXXXXX"
```

##### Step 3
Create a user from command line and voila you're done.
```
python manage.py createsuperuser
```

