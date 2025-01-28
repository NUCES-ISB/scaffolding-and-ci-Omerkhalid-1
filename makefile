lint:
	pylint --disable = C , r *.py 

test:
	pytest test.py 

intsall:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

	