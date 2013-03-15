#include <stdio.h>

#include "Interactive.h"
#include "File.h"

void err(const char* string) { fprintf(stderr, string); }

int error(int value)
{
	// Printing out the error message(s)
	switch (value)
	{
		case 1: err("ERR CODE 1: Couldn't open source file."); break;
		case 2: err("ERR CODE 2: Provided eval with a NULL string."); break;
		default: break;
	}

	return value;
}

// Return values
//  0 - All's well
int main(int argc, char** argv)
{	
	if (argv > 2) printf("Proper usage: crocode (<source file>)\n");
	else if (argc == 2) return error(file(argv[1]));
	return error(interactive());
}
