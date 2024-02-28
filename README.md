# spreadsheet-golf-tour-be
Back end repo for the Spreadsheet Golf Tour app, written in Flask.  The Spreadsheet Golf Tour app is designed to manage a golf-picks pool amongst four friends.  The golf-picks pool was originally maintained and stored in a spreadsheet, but has now upgraded to a full web app!

## Setup Instructions (Mac)
1. Clone the repository: `git clone git@github.com:vktr-r2/spreadsheet-golf-tour-be.git`
2. Go to local repo directory and create local environment: `python3 -m venv venv`
3. Run local environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Ensure your `.env` file is set up with the correct database URI
6. Create the database tables: `python create_db.py`
7. Run the app: `flask run`


<!-- source venv/bin/activate
flask run -->