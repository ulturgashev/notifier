PYTHONPATH = $(pwd)

check:
	flake8 service/* tests/*

format:
	black service/* tests/*

test:
	pytest
