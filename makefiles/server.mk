### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

server.install: ## Install server with its dependencies
	./manage.py compose run --rm web pip install -r requirements.txt --user --upgrade --no-warn-script-location

server.start: ## Start server in its docker container
	./manage.py compose up

server.daemon: ## Start daemon server in its docker container
	./manage.py compose up -d server

server.stop: ## Start server in its docker container
	./manage.py compose stop

server.upgrade: ## Upgrade pip dependencies
	./manage.py compose run --rm server bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-dev.txt --skip-virtualenv-check"