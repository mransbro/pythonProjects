newProject:
	@echo "What is the name of project?: ";\
	read PROJECT; \
	mkdir $$PROJECT; \
	touch "./$$PROJECT/README.md"; \
	touch "./$$PROJECT/main.py"