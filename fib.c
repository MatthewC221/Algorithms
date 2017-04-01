#include <stdio.h>
#include <stdlib.h>

/* 
    FIB IN C... for numbers greater than long
    This is the most basic implementation, better things to do:
        - less malloc, malloc to (size * 2) instead of (size + 1)
        - VECTOR OF INTS, much more memory efficient
        
    A python program is 6 * faster than this

*/

int *array_last;
int *array_next;
int *array_current;

int array_next_size = 1;	//sizes of the current 

void find(int number);
void copyArray();
void shift_left();
void printCurrent();

int main(int argc, char *argv[]) {

	if (argc != 2) return 1;

	unsigned int fib_number = atoi(argv[1]) - 2;

	int *array_current;

	// printf("Fib number is %d size %lu\n", fib_number, sizeof(array_last));
	find(fib_number);

	return 0;
}

void find (int number) {

	array_last = malloc(sizeof(int));
	array_next = malloc(sizeof(int));
	array_current = malloc(sizeof(int));

	int i;
	
	array_next[0] = 1;
	array_last[0] = 1;
	int overflow = 0;
	int last_value;

	//if still overflow at end, shift everything and put 1 
	for (i = 0; i < number; i++) {	
	    overflow = 0;
		for (last_value = array_next_size - 1; last_value >= 0; last_value--) {
			array_current[last_value] =  array_last[last_value] + array_next[last_value] + overflow;
			if (overflow > 0) {
			    overflow = 0;
		    }
			if (array_current[last_value] > 9) {
				overflow++;
				array_current[last_value] = array_current[last_value] - 10;
			}
		}
		if (overflow == 1) {
		 //   printf("here\n");
			shift_left();
			overflow = 0;
		}
		copyArray();
		overflow = 0;
	} 
	
	printCurrent();

}

//array is copying weird

void copyArray () {

    int i;

	for (i = array_next_size; i >= 0; i--) {
		array_last[i] = array_next[i];
	}

	for (i = array_next_size; i >= 0; i--) {
		array_next[i] = array_current[i];
	}

}

void shift_left() {

	int previous_last = array_next_size - 1;
	array_next_size++;

	array_current = realloc(array_current, array_next_size * sizeof(int) + 8);
	array_last = realloc(array_last, array_next_size * sizeof(int) + 8);
	array_next = realloc(array_next, array_next_size * sizeof(int) + 8);

	for (previous_last = previous_last; previous_last >= 0; previous_last--) {
		array_current[previous_last + 1] = array_current[previous_last];
		array_next[previous_last + 1] = array_next[previous_last];
		array_last[previous_last + 1] = array_last[previous_last];
	}
	
	array_current[0] = 1;
	array_next[0] = 0;

}

void printCurrent() {

	int i;
	for (i = 0; i <= array_next_size - 1; i++) {
		printf("%d", array_current[i]);
	}

	printf("\n");



}







