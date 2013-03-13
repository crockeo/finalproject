#ifndef FILE_H
#define FILE_H

// Reading a line of a file
char* readLine(FILE* fp);

// Reading a whole file
char** readFile(FILE* fp);

// Interpreting from a file
int file(char* path);

#endif
