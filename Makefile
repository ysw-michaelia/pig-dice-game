# Version of Python
PYTHON ?= python

# To define targets in each directory under the src/
define FOREACH
	for DIR in pigGame/* tests/*; do \
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
	$(PYTHON) pigGame/main.py

# ---------------------------------------------------------
# Test
#

test:
	$(PYTHON) -m unittest discover -b tests/

coverage:
	$(PYTHON) -m coverage run -m unittest discover -b tests/
	coverage report
	coverage html

pylint:
	for f in pigGame/*.py ; do pylint $${f} ; done

flake8:
	for f in pigGame/*.py ; do flake8 $${f} ; done

# ---------------------------------------------------------
# Generating documentation
#
.PHONY: doc

doc:
	mkdir -p doc
	$(PYTHON) -m pydoc -b -w pigGame
	# mv *.html doc/api

pyreverse:
	install -d doc/uml
	pyreverse pigGame/*.py
	dot -Tpng classes.dot -o doc/uml/classes.png
	dot -Tpng packages.dot -o doc/uml/packages.png
	rm -f classes.dot packages.dot

