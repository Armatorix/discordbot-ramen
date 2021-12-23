.PHONY: setup
setup:
	python3 -m venv venv
	chmod +x venv/bin/activate

.PHONY: install
install:
	# bash -c "venv/bin/activate"
	pip install -r requirements.txt

.PHONY: clean
clean:
	rm -r lib venv

.PHONY: run
run:
	python3 main.py