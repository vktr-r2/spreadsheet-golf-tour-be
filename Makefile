# EXAMPLE
# target: dependencies
#    command

.PHONY: setup create-env activate-env
setup: create-env activate-env

create-env:
	@echo "Creating virtual environment..."
	python3 -m poetry install

activate-env:
	@echo "Almost there..."
	@echo "You need to activate the virtual environment manually by running 'python -m poetry shell'"


install:
	@echo "Installing dependencies..."
	python -m poetry install


server:
	@echo "Starting server..."
	FLASK_APP=spreadsheet_golf_tour_be/app.py FLASK_ENV=development flask run
	

test:
	@echo "Starting tester..."
	pytest tests/

# DB Related Make Commands
create-db:
	@echo "Creating the database..."
	mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS sgt_db;"

drop-db:
	@echo "Dropping the database..."
	mysql -u root -p -e "DROP DATABASE IF EXISTS sgt_db;"



lint:
	@echo "Checking your work..."
	@pre-commit run --all-files


clean:
	@echo "Cleaning up caches..."
	find . -type d -name '__pycache__' -exec rm -rf {} +
