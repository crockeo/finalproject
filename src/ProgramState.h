#ifndef PROGRAM_STATE_H
#define PROGRAM_STATE_H

#include <stdbool.h>

typedef struct
{
	int val;
	char* name;
} VARIABLE;

// Initializing program state
int init_program_state();

// Destroying the program state
int destroy_program_state();

// Checking if a variable exists
bool var_exists(char* name);

// Getting a variable
int get_var(char* name);

// Setting a variable to a new value
int set_var(char* name, int value);

// Inserting a new variable
int insert_var(char* name, int value);

#endif
