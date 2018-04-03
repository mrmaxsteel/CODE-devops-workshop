integration_test:
	venv/bin/py.test tests/integration -v

unit_test:
	venv/bin/py.test tests/unit -v

test: unit_test integration_test

run:
	venv/bin/python calculator/app.py
