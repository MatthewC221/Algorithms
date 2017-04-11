#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*  First edition of password cracking
 *  Permute_better.c allows us to input specific characters only
 *  which is in itself somewhat tricky.   
 *  Anyway enjoy!
*/

void brute_forcer(int size);
void print_current(char *A);

int main(int argc, char *argv[]) {

    int size;
    printf("Specify size to brute force: \n");
    scanf("%d", &size);
    brute_forcer(size);
    printf("We can expect 26^N permutations\n");






    return EXIT_SUCCESS;
}

void brute_forcer(int size) {
    
    // Create the initial "aaaaa"
    char *A = malloc(sizeof(char) * size + 1);
    for (int i = 0; i < size; i++) {
        A[i] = 'a';
    }
    
    int current_element = size - 1;
    int count = 0;
    
    // The iterator
    while (1) {
        count++;
        print_current(A);
        A[current_element]++;
        if (A[current_element] == 'z') {        // If current element is 'z', we need to iterate something
            count++;                            // Extra permutation here!
            int temp = current_element;
            while (A[temp] == 'z') {            // Find next iterable, e.g. azzz needs an iteration on a
                A[temp] = 'a';                  // As we look for it azzz->azza->azaa->baaa
                temp--;
                if (temp == -1) {
                    printf("Number of permutations = %d\n", count);
                    return;
                }  
            }
            A[temp]++;
            A[current_element] = 'a';
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








