# spreadsheet-golf-tour-be

Back end repo for the Spreadsheet Golf Tour app, written in Flask. The Spreadsheet Golf Tour app is designed to manage a golf-picks pool amongst four friends. The golf-picks pool was originally maintained and stored in a spreadsheet, but has now upgraded to a full web app!

## Setup & Shutdown Instructions (Mac)

1. Clone the repository: `git clone git@github.com:vktr-r2/spreadsheet-golf-tour-be.git`
2. Go to local repo directory and use `make setup` command to setup a local environment (FIRST TIME ONLY)
3. Use `poetry shell` to activate local environment
4. Ensure your `.env` file is set up with the correct database URI
5. Install all dependencies to local env using `make install`
6. Create the database with `make build-db` command
7. Start server with `make server` command

Your local server should now be running on PORT 5000 and you're all set to start working!

To shut down server use `ctrl+c`
To shut down local enviroment use `deactivate`

#### DEV NOTES:

- Update dependencies:
  `poetry update`

- Run pre-commit manually on all files:
  `make lint` OR `pre-commit run --all-files`

## API NOTES

- Use Live Golf Data API available at https://rapidapi.com/slashgolf/api/live-golf-data/
- Free source up to 20 calls per day, 250 calls per month.
- Examples of data structure can be seen in JSON files found in `seed_data` directory

