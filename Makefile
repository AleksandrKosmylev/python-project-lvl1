install:
	poetry install

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-gcd:
	poetry run brain-gcd

lint:
	poetry run flake8 brain_games

full:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl --force-reinstall
	
selfcheck:
	poetry check
