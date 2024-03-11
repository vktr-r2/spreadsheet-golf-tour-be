class TournamentsService:

    def __init__(self, api_wrapper, org_id):
        self.api_wrapper = api_wrapper
        self.org_id = org_id

    def fetch_tournaments(self):
        try:
            tournaments = self.api_wrapper.call_schedule_endpoint(self.org_id)
            return tournaments
        except Exception as e:
            raise e
