# make release
# Triggers a git add, commit and push
# Use with care, as this will include all files!
.PHONY: release
release:
	$(eval COMMENT := $(shell bash -c 'read -e -p "Comment: " var; echo $$var'))
	@git add --all; \
	 git commit -m "$(COMMENT)"; \
	 git push
