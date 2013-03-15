#include <stdio.h>

#include "Interactive.h"
#include "File.h"

int error(int value)
{
	// Printing out the error message(s)
	switch (value)
	{
		case 1: printf("ERR CODE 1: Couldn't open source file."); break;
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
