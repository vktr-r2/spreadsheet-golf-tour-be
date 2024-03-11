from datetime import datetime
import requests
import os


class RapidApiWrapperService:

    def __init__(self):
        self.rapid_api_key = os.environ.get("RAPID_API_KEY")
        self.base_url = "https://live-golf-data.p.rapidapi.com/"
        self.headers = {
            "X-RapidAPI-Key": self.rapid_api_key,
            "X-RapidAPI-Host": "live-golf-data.p.rapidapi.com",
        }

    def call_schedule_endpoint(self, org_id):
        url = f"{self.base_url}schedule"
        current_year = str(datetime.now().year)
        querystring = {"orgID": org_id, "year": current_year}

        response = requests.get(url, headers=self.headers, params=querystring)

        return response.json()
