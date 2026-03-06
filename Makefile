INT=python3
MAIN=src/main.py
BISON_FILE=k0gram.y
OUTPUT_FILE=nterm.h

run:
	$(INT) $(MAIN) $(BISON_FILE) $(OUTPUT_FILE)
