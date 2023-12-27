
default:
	python setup.py build

install:
	python setup.py install

test:
	python example/manage.py test app encrypted_files

lint:
	find ./ -name "*.py" -type f -exec sed -i 's/ \+$$//g' {} \;
	find ./ -name "*.html" -type f -exec sed -i 's/ \+$$//g' {} \;
	isort --profile black .
	black .
	flake8 --ignore=E501,W503 ./encrypted_files ./example
