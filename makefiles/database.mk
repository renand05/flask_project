### DATABASE
# ¯¯¯¯¯¯¯¯

database.connect: ## Connect to database
	./manage.py compose exec db psql -Upostgres

database.init: ## Create alembic migration file
	./manage.py flask db init

database.migrate: ## Create alembic migration file
	./manage.py flask db migrate

database.upgrade: ## Upgrade to latest migration
	./manage.py flask db upgrade

database.downgrade: ## Downgrade latest migration
	./manage.py flask db downgrade