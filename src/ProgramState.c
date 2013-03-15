#include "ProgramState.h"

#include <string.h>

const static int INITIAL_LENGTH = 16;

VARIABLE* variables = NULL;
int varlength = 0x0;
int index = 0x0;

// Function to easily resize variables
int resize_variables()
{
	if (variables == NULL) return 1;

	VARIABLE* tempvariables = (VARIABLE*)malloc((varlength * 2) * sizeof(VARIABLE));
	for (int i = 0; i < varlength; i++)
		tempvariables[i] = variables[i];
	free(variables);
	variables = tempvariables;
	varlength *= 2;

	return 0;
}

// Initializing program state
int init_program_state()
{
	varlength = INITIAL_LENGTH;
	variables = (VARIABLE*)malloc(varlength * sizeof(VARIABLE));
	index = 0;

	return 0;
}

// Destroying the program state
int destroy_program_state()
{
	if (variables == NULL) return 1;

	for (int i = 0; i < index; i++)
	{
		if (variables[i].name == NULL) return 1;
		free(variables[i].name);
	}
	
	free(variables);

	return 0;
}

// Checking if a variable exists
bool var_exists(char* name);
{
	for (int i = 0; i < index; i++)
		if (strcmp(name, variables[i].name) == 0) return true;
	return false;
}

// Getting a variable
int get_var(char* name)
{
	for (int i = 0; i < index; i++)
		if (strcmp(name, variables[i].name) == 0) return variables[i].val;
	return INT_MAX;
}

// Setting a variable to a new value
int set_var(char* name, int val)
{
	for (int i = 0; i < index; i++)
	{
		if (strcmp(name, variables[i].name) == 0) variables[i].val = val;
		return 0;
	}

	return 1;
}

// Inserting a new variable
int insert_var(char* name, int va)
{
	if (var_exists(name)) return 1;
	
	VARIABLE var;

	var.val  = val;
	var.name = name;

	if (index >= varlength) resize_variables();
	
	variables[index] = var;
	index++;

	return 0;
}
