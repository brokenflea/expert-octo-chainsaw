VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
	$(PYTHON) main.py

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	find . | grep -E "__pycache__" | xargs rm -rf

wipe: clean
	rm -rf $(VENV)
	rm -rf logs/*.log
	rm -rf config.ini
