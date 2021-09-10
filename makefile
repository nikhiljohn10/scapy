.DEFAULT_GOAL := help
.PHONY: install invenv clean reset coverage deps test

PIP=$(shell which pip3 || which pip)
VERSION_FILE := $(shell pwd)/scapy/__version__.py
CURRENT_VERSION := $(subst \#v,,$(shell cat $(VERSION_FILE)))

version:  ## Display current version
	@echo "scapy v$(CURRENT_VERSION)"

install:  ## Install poetry
ifeq ($(PIP),)
	@echo "Python3 pip module missing" >&2 && exit 1
endif
	@$(PIP) install --user poetry

deps:  ## Install dependencies
	@poetry update

check:  ## Check package using pre-commit
	@-poetry run pre-commit run --all-files

clean:  ## Clean development files and directories
	@rm -rf build/ .tox/ .pytest_cache/ .mypy_cache/ *.egg-info/
	@find . -type d -name *pycache* -exec rm -rf {} +

reset: clean  ## Reset poetry cache
	@yes | poetry cache clear . --all > /dev/null 2>&1

test:  ## Run tests
	@poetry run pytest -ra

build: test clean  ## Build package
	@poetry run python setup.py sdist bdist_wheel

check-build:  ## Check the package built
	@poetry run twine check dist/*

publish: check-build  ## Publish package in pypi.org
	@poetry run twine upload dist/*

bump:  ## Bump to new version
ifeq ($(VERSION),)
	@echo "Error: Require VERSION variable to be set."
else ifeq ($(VERSION),$(CURRENT_VERSION))
	@echo "Error: You have given current version as input. Please try again."
else
	@echo "#v$(VERSION)" > $(VERSION_FILE)
	@poetry version $(VERSION)
	@git add .
	@git commit -m "bump version to v$(VERSION)"
	@git tag -a "v$(VERSION)" HEAD -m "cloudflare-api v$(VERSION)"
	@git push --follow-tags
endif

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [COMMAND]"; \
	printf "%-16s %s\n" "COMMAND" "DESCRIPTION" ; \
	printf "%-16s %s\n" "-------" "-----------" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-16s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done
