from datetime import datetime
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
import os
from typing import Optional, Dict, Any


class RapidApiWrapperService:

    def __init__(self) -> None:
        self.rapid_api_key = os.environ.get("RAPID_API_KEY")
        self.base_url = "https://live-golf-data.p.rapidapi.com/"
        self.headers = {
            "X-RapidAPI-Key": self.rapid_api_key,
            "X-RapidAPI-Host": "live-golf-data.p.rapidapi.com",
        }

    def call_schedule_endpoint(self, org_id: str) -> Optional[Dict[str, Any]]:
        current_year = str(datetime.now().year)
        query_string = {"orgID": org_id, "year": current_year}
        return self.make_request("schedule", params=query_string)

    def make_request(
        self, url_path: str, params: Optional[Dict[str, str]] = None
    ) -> Optional[Dict[str, Any]]:
        full_url = f"{self.base_url}{url_path}"

        try:
            response = requests.get(full_url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()

        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except Timeout:
            print("The request timed out")
        except RequestException as err:
            print(f"An error occurred: {err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return None
