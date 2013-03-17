CC=gcc
EXECUTABLE=crocode
CFLAGS=-std=c99 -Wall -Werror -ggdb
SOURCES=src/Main.c src/Interactive.c src/File.c src/ProgramState.c src/ParseUtils.c src/Interpreter.c
OBJECTS=$(SOURCES:.c=.o)
HEADERS=src/*.h

default: $(SRC) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(CFLAGS) $(OBJECTS) -o $@

clean:
	rm -f src/*.o crocode core
