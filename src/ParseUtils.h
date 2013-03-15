#ifndef PARSE_UTILS_H
#define PARSE_UTILS_H

// Splitting a string by a delimiter
char** split_by(const char* string, char delimiter);

// Getting the length of a split string
int split_len(char** split);

#endif