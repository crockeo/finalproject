#include "Interactive.h"

#include "Interpreter.c"

const int BUFFER_SIZE = 128;

// Interpreting from user-input
int interactive()
{
	char* string;

	while (true)
	{
		string = (char*)malloc(BUFFER_SIZE * sizeof(char));

		printf(": ");
		scanf("%s", string);
		
		int ret = eval(string);
		if (ret != 0) return ret;

		free(string);
	}
}