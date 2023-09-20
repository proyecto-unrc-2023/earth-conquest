# From: https://flask.palletsprojects.com/en/2.3.x/tutorial/tests/
coverage run --branch --source='app/' -m pytest
coverage run --append --branch --source='app/' -m behave
coverage html