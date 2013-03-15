#include "File.h"

#include <string.h>

// Reading a line of a file
char* read_line(FILE* fp)
{
	int len = 16;
	int index = 0;
	char* line = (char*)malloc(len * sizeof(char));
	char* tline;

	for (char c = fgetc(fp); c != EOF && c != '\n'; c = fgetc(fp))
	{
		if (index >= len)
		{
			char* tline = (char*)malloc((len * 2) * sizeof(char));
			memcpy(tline, line, len * sizeof(char));

			free(line);
			line = tline;
			len *= 2;
		}

		line[index] = c;
		line++;
	}

	tline = (char*)malloc((index + 1) * sizeof(char));
	memcpy(tline, line, index * sizeof(char));
	tline[index] = '\0';

	free(line);
	return tline;
}

// Interpretation from a file
int file(char* path)
{
	FILE* fp = fopen(path, "r");
	if (fp == NULL) return 1;

	char* line;
	do
	{
		if (line != NULL) free(line);
		line = read_line(fp);

		int n = eval(line);
		if (n != 0)
		{
			free(line);
			return n;
		}
	} while (line != NULL);

	return 0;
}