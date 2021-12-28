### FORMAT
# ¯¯¯¯¯¯¯¯

format.black: ## Run black on every file
	black .
format.isort: ## Sort imports
	isort --recursive .