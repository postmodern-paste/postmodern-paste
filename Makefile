export PYTHONPATH := app:$(PYTHONPATH)


all:
	$(MAKE) dependencies
	$(MAKE) check-style
	$(MAKE) test-coverage
	$(MAKE) default

skip-tests:
	$(MAKE) dependencies
	$(MAKE) default

default:
	mkdir -p app/static/build/js
	mkdir -p app/static/build/css
	python3 build/build_database.py --create
	python3 build/build_js.py --config-environment
	python3 build/build_css.py --config-environment

dev:
	mkdir -p app/static/build/js
	mkdir -p app/static/build/css
	python3 build/build_database.py --create
	python3 build/build_js.py --dev
	python3 build/build_css.py --dev

prod:
	mkdir -p app/static/build/js
	mkdir -p app/static/build/css
	python3 build/build_database.py --create
	python3 build/build_js.py --prod
	python3 build/build_css.py --prod

dependencies:
	java -version
	bundler install --deployment
	npm install uglify-js
	pip install -r requirements.txt
	pre-commit install
	git submodule init
	git submodule update

clean:
	rm -rf app/static/build
	python3 build/build_database.py --drop

test:
	python3 -m unittest discover -s tests -v

test-coverage:
	coverage run --source=app -m unittest discover -s tests -v
	coverage report -m

check-style:
	pre-commit run --all-files
