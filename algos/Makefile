
package:
	python setup.py sdist

test:
	python -m unittest -v

clean:
	rm -rf dist
	rm -rf *.egg-info
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
