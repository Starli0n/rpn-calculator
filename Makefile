SHELL=bash
.ONESHELL:

.PHONY: clean
clean:
	cd app && . ./scripts/clean.sh

.PHONY: install-requirements
install-requirements:
	cd app && . ./scripts/install.sh

.PHONY: install-requirements-dev
install-requirements-dev:
	cd app && . ./scripts/install_dev.sh

.PHONY: upgrade
upgrade:
	cd app && . ./scripts/upgrade.sh

.PHONY: upgrade-dev
upgrade-dev: upgrade
	cd app && . ./scripts/upgrade_dev.sh

.PHONY: tests
tests:
	cd app && . ./scripts/tests.sh
