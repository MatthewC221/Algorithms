#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*  Use lower case inputs of characters
 *  This was an experiment, which also would help out one of my Uni wargames
 *  There isn't a clear solution online in which we permute N characters into a X char string 
 *  (apart from using a library)
 *  A common question is unique permutations from N->N letters which is interesting too...
*/

void brute_forcer(int size, char *string);
void print_current(char *A);

int main(int argc, char *argv[]) {

    if (argc == 3) {
        int size = atoi(argv[1]);
        char *string = argv[2];
        
        // Removing duplicates
        int word_size = 0;
        int all[27] = {0};    // A = 1, Z = 26
        for (int i = 0; i < strlen(string); i++) {
            int temp = string[i] - 96;
            if (!all[temp]) {
                word_size++;
                all[temp]++;
            }
        }
        
        char *new_string = malloc(sizeof(char) * word_size + 1);
        int increment = 0;
        for (int i = 1; i < 27; i++) {
            if (all[i]) {
                new_string[increment++] = i + 96;
            }
        }
        new_string[word_size] = '\0';
        brute_forcer(size, new_string);
        
        printf("There are %d unique letters in %s\n", word_size, string);
        printf("We can expect N permutations where N is (unique letters in the word)^size\n");
    } else {
        printf("Usage ./permute_merkle <size> <word>\n");
    }

    return EXIT_SUCCESS;
}

void brute_forcer(int size, char *string) {

    int *element_pos = malloc(sizeof(int) * size);           // Position of each element in string.
    char *A = malloc(sizeof(char) * size + 1);                  // e.g [0,0,0,0,0] = [m,m,m,m,m]
    for (int i = 0; i < size; i++) {
        A[i] = string[0];
        element_pos[i] = 0;
    }
    
    char last_element = string[strlen(string) - 1];
    
    int current_position = 0;
    int current_element = size - 1;
    int count = 0;
    
    while (1) {
        A[current_element] = string[element_pos[current_element]];
        element_pos[current_element]++;
        print_current(A);
        count++;
        if (A[current_element] == last_element) {
            int temp = current_element;
            while (A[temp] == last_element) {
                A[temp] = string[0];
                element_pos[temp] = 0;
                temp--;
                if (temp == -1) {
                    printf("Number of permutations = %d\n", count);
                    return;
                } 
            }
            element_pos[temp]++;
            A[temp] = string[element_pos[temp]];
            element_pos[current_element] = 0;
            A[current_element] = string[element_pos[current_element]];
            print_current(A);
        }
    }
   
}

void print_current(char *A) {

    for (int i = 0; i < strlen(A); i++) {
        printf("%c", A[i]);
    }
    printf("\n");
}








