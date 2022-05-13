======================
Cookiecutter for Data Science
======================

Cookiecutter_ template for a Data Science project in Python. 

Features
--------

Includes:

* Makefile
* linting (black, flake8, mypy and pydocstyle)
* dependency management with ``poetry``
* Docker: Dockerfile and bash scripts to create and manage containers
* pre-commit hooks etc.
* CLI interface with Click and Fire (optional)
* CI/CD pipeline in CircleCI


Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/nastjamakh/cookiecutter-data-science.git

Then:

* Create a repo and put it there.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Run ``make setup_local`` to work locally. This will create a pyenv virtual environment with a chosen python version and install dependencies specified in requiremets.txt accordingly.
* Alternatively, run ``make setup_docker`` to develop in a Docker container. This will build a container using Dockerfile and install poetry with dependencies inside the container.

Note that the provided scripts in ``bin`` folder to help you work with the container.
  
  * Run ``make build`` to build a container, and ``make start`` to start it.
  * Prefix your command with ``./bin/docker-exec.sh`` to run the command inside container. For example, ``./bin/docker-exec.sh poetry install`` would install dependencies in the container.

There are several formatting tools included to ensure consistent Python code.

* ``black`` 
* ``flake8`` for line length
* ``mypy`` for typing hints and imports
* ``pydocstyle`` for docstrings


For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `drivendata/cookiecutter-data-science`_: A more minimalistic boilerplate for stricly local development with no Docker or CI/CD pipeline. More focus on generating dcsumenttaion.


.. _`drivendata/cookiecutter-data-science`: https://github.com/drivendata/cookiecutter-data-science
