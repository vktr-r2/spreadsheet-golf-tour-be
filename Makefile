# EXAMPLE
# target: dependencies
#    command

.PHONY: setup create-env activate-env
setup: create-env activate-env

create-env:
	@echo "Creating virtual environment..."
	python3 -m venv venv

activate-env:
	@echo "Almost there..."
	@echo "You need to activate the virtual environment manually by running 'source venv/bin/activate'"



install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt



server:
	@echo "Starting server..."
	FLASK_APP=spreadsheet_golf_tour_be/app.py FLASK_ENV=development flask run



test:
	@echo "Starting tester..."
	pytest tests/



build-db:
	@echo "Building the database..."
	@python build_db.py


lint:
	@echo "Checking your work..."
	@pre-commit run --all-files


clean:
	@echo "Cleaning up caches..."
	find . -type d -name '__pycache__' -exec rm -rf {} +
