#ifndef PROGRAM_STATE_H
#define PROGRAM_STATE_H

#include <stdbool.h>

// Checking if a variable has been declared
bool isdeclared(char* name);

// Getting all int or float variables
int* get_int_vars();
float* get_float_vars();

// Getting a single int or float variable
int get_int_var(char* name);
float get_float_var(char* name);

#endif
