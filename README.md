# Django-0Auth-2.0-Google-Calendar-Events-REST-APIs

This is a Django REST API that uses Google OAuth 2.0 to fetch the users Google Calendar Events.

## How to run this project on your local machine?

First of all clone the Project to your local machine.

```
git clone [mohammedazam55/Django-0Auth-2.0-Google-Calendar-Events-REST-APIs](https://github.com/mohammedazam55/Django-0Auth-2.0-Google-Calendar-Events-REST-APIs.git)
```

To run this project you need to [install](https://www.python.org/downloads/) Python >= 3.6.0 on your local machine.

Once, you have installed Python you need to follow the following steps:

- Create a virtual environment called 'venv'.

```
py -m venv venv 
```

- Now activate the virtual environment by executing the following command

Windows

```
venv\Scripts\activate
```

OR
for Linux/MacOS

```
source venv\Scripts\activate
```

### Once you have fired up your virtual evnvironment install the necessary libraries :-

```
pip install -r requirements.txt 
```

This will install all the necessary python libraries/packages for the project.

Now we can move on to setting up the Google Calendar API.

## Google 0Auth 2.0 Client Setup

In this step we are going to create a Google API Client that will provide us access to the user's Calendar.

- Visit on to the Google Cloud Console [website](https://console.cloud.google.com/) and Sign up / Sign in.
- Create a **New Project** and the go to API's & Services -> Credentials -> Create Credentials.
- Select Web Application and follow these steps:-
- In the **Authorized JavaScript origins** add the following URI '<https://localhost:8000>'
- In the **Authorized redirect URIs** add the following URI '<https://localhost:8000/rest/v1/calendar/redirect/>'
- Select scope for Google Calendars as readonly '<https://www.googleapis.com/auth/calendar.readonly>'
- After this download the json file at the end and replace it with the '/credentials/client_secrets.json/'

- Visit OAuth Consent Screen under Google APIs & Services:
  - In Test Users add your email address

## Running the Project

Run the following command in your virtual environment terminal to start the Django server :

```
python manage.py runsslserver
```

- Open the browser and enter the following URL :- "<https://localhost:8000/rest/v1/init/>"
