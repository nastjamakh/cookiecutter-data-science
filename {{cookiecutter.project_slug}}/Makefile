PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}
SHELL = {{ cookiecutter.shell_environment }}
PROJECT_NAME = "home-credit-risk"

setup:
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	brew install zsh

setup_local:
	make setup
	pip install poetry
	make setup_pyenv
	make create_virtualenv
	poetry install
	pip install wheel
	poetry add `cat requirements.txt`
	rm -r requirements.txt

setup_docker:
	make setup
	make build
	make start
	./bin/docker-exec.sh poetry install
	./bin/docker-exec.sh pip install wheel
	./bin/docker-exec.sh poetry add `cat requirements.txt`
	rm -r requirements.txt

## Set up python interpreter environment
setup_pyenv:
	brew install openssl readline sqlite3 xz zlib
	brew install pyenv pyenv-virtualenv
	echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
	echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
	echo 'eval "$(pyenv init -)"' >> ~/.zshrc
	pyenv install {{cookiecutter.python_version}}

create_virtualenv:
	pyenv virtualenv{{cookiecutter.python_version}} $(PROJECT_NAME)
	pyenv local $(PROJECT_NAME)
	@echo ">>> New pyenv virtualenv created. Activate with:pyenv local $(PROJECT_NAME)"
	
# Install Python Dependencies
install:
	./bin/docker-exec.sh poetry install

# images & containers
build:
	./bin/docker-build.sh

image-pull:
	./bin/docker-pull.sh

image-push:
	./bin/docker-push.sh

start:
	./bin/docker-start.sh

stop:
	./bin/docker-remove.sh

notebook:
	./bin/notebook-start.sh

# code
lint:
	{%- if cookiecutter.use_black == 'y' %}./bin/docker-exec.sh poetry run black -- bin src{%- endif %}&& \
	{%- if cookiecutter.use_flake8 == 'y' %}poetry run flake8 --max-line-length=90{%- endif %}&& \
	{%- if cookiecutter.use_mypy == 'y' %}poetry run mypy  --follow-imports=skip --ignore-missing-imports --disallow-untyped-defs -- src{%- endif %}&& \

test:
	./bin/docker-exec.sh poetry run pytest -s

server:
	./bin/docker-exec.sh ./bin/webserver-start.sh

train:
	./bin/docker-exec.sh poetry run train train to_s3=$(to_s3)

