## Setting up

### Basic setup (required)

#### Prerequisites
1. Homebrew
2. Python 3.6.5
3. PostgreSQL

#### Install Python

Install `pyenv` Python version manager

	$ brew install pyenv

Next, have `pyenv` install 3.6.5:

	$ pyenv install 3.6.5

Double-check 3.6.5 appears under versions:

	$ pyenv versions

Set the global version to 3.6.5:

	$ pyenv global 3.6.5

Load `pyenv` automatically by adding this to your `/.bash_profile` (depends on if using bash or zsh):

	$ eval "$(pyenv init -)"

#### Install Postgres

For MacOS, simplest way is using Homebrew by running `brew install postgres`

To start postgresql now and restart at login:

	$ brew services start postgresql

#### Install application

Create virtual environment:

	$ python3 -m venv venv

Create `env.sh` file:

	$ echo "source venv/bin/activate" > env.sh

Initialize env variables from `env.sh`:

	$ source env.sh

Make sure virtual environment is using *Python >=3.6*:

	(venv) $ python --version
	Python 3.6.5
	...

Install PIP dependencies (be sure you're in your virtual environment!):

	(venv) $ pip3 install -r requirements.txt

## Start it up

In terminal inside project directory,:

	$ source env.sh
	(venv) $ flask run --port 8002

