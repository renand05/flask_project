### TEST
# ¯¯¯¯¯¯¯¯


.PHONY: test
test: ## Launch tests in their own docker container
	./manage.py test "tests"
