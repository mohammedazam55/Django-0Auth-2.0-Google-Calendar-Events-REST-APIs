from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from google.oauth2 import credentials
from google_auth_oauthlib.flow import Flow
from django.conf import settings
from googleapiclient.discovery import build
import json


class GoogleCalendarInitView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        # Configure the OAuth flow
        flow = Flow.from_client_secrets_file(
            settings.GOOGLE_CLIENT_SECRETS_FILE,
            scopes=settings.GOOGLE_CALENDAR_SCOPES,
            redirect_uri=settings.GOOGLE_REDIRECT_URI,
        )

        # Generate the authorization URL and redirect the user
        authorization_url, _ = flow.authorization_url(prompt="consent")
        return redirect(authorization_url)


class GoogleCalendarRedirectView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve the authorization code from the query parameters
        code = request.GET.get("code")

        # Configure the OAuth flow
        flow = Flow.from_client_secrets_file(
            settings.GOOGLE_CLIENT_SECRETS_FILE,
            scopes=settings.GOOGLE_CALENDAR_SCOPES,
            redirect_uri=settings.GOOGLE_REDIRECT_URI,
        )

        # Exchange the authorization code for the access token
        flow.fetch_token(code=code)

        # Obtain the credentials from the flow
        credentials = flow.credentials

        # Use the credentials to fetch events from the user's calendar
        events = self.fetch_events(credentials)

        formatted_events = self.format_events(events)

        # Return the events JSON as the response
        return Response({"events": formatted_events})

    def fetch_events(self, credentials):
        # Create a service instance using the credentials
        service = build("calendar", "v3", credentials=credentials)

        # Fetch the list of events from the user's calendar
        events_result = service.events().list(calendarId="primary").execute()
        events = events_result.get("items", [])

        return events

    def format_events(self, events):
        formatted_events = []
        for event in events:
            formatted_event = {
                "summary": event.get("summary", ""),
                "start": event.get("start", {}).get("dateTime", ""),
                "end": event.get("end", {}).get("dateTime", ""),
                "location": event.get("location", ""),
            }
            formatted_events.append(formatted_event)
        return formatted_events
