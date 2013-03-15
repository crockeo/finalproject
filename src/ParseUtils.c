#include "ParseUtils.h"

// Splitting a string by a delimiter
char** split_by(const char* string, char delimiter)
{
	int len = 8;
	char** strs = (char**)malloc(len * sizeof(char*));
	char** tstrs;
	int index = 0;

	for (char* str = strtok(string, sprintf("%c", delimiter)); str != NULL; str = strtok(string, sprintf("%c", delimiter)))
	{
		if (index >= len)
		{
			tstrs = (char**)malloc((len * 2) * sizeof(char*));
			memcpy(tstrs, strs, len);
			free(strs);
			strs = tstrs;
		}

		strs[index] = str;
		index++;
	}

	tstrs = (char**)malloc((index + 1) * sizeof(char*));
	memcpy(tstrs, strs, index);

	tstrs[index] = NULL;

	free(strs);

	return tstrs;
}

// Getting the length of a split string
int split_len(char** split)
{
	int i;
	for (i = 0; split[i] != NULL; i++) { }
	return i;
}