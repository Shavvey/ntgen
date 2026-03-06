INT=python3
MAIN=src/main.py
BISON_FILE=k0gram.y

run:
	$(INT) $(MAIN) $(BISON_FILE)
