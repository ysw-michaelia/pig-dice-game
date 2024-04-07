# Version of Python
PYTHON ?= python

# To define targets in each directory under the src/
define FOREACH
	for DIR in src/*; do \
		$(MAKE) -C $$DIR $(1); \
	done
endef

all:

# ---------------------------------------------------------
# Create and setup a virtual environment
#

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install: requirements.txt
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list

# ---------------------------------------------------------
# start the game
#

run:
	@printf "This Starts the game\n"
	$(PYTHON) src/game/main.py

# ---------------------------------------------------------
# Test
#

pylint:
	for f in src/game/*.py ; do pylint $${f} ; done

flake8:
	for f in src/game/*.py ; do flake8 $${f} ; done
