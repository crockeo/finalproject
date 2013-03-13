#ifndef HASHMAP_H
#define HASHMAP_H

// A hashmap for integers
typedef struct
{
	int* variables;
	int length;
} I_HASHMAP;

// A hashmap for floats
typedef struct
{
	float* variables;
	int length;
} F_HASHMAP;

// Hashing a string
char* hash(char* string);

#endif
