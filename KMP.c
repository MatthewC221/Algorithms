#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Implementation of Knuth-Morris-Pratt in C. To better understand content in COMP3121 (Algorithms UNSW)
// Great explanation here: https://www.youtube.com/watch?v=GTJr8OvyEVQ

void main(int argc, char *argv[]) 
{

    if (argc != 2) {
        fprintf(stderr, "Usage ./KMP <substring>\n");
    } else {
        char *sub_string = argv[1];
        int *backtrack = malloc(sizeof(int) * strlen(sub_string));

        // First organise the backtrack array
        int i = 0;
        int j = 1;
        
        backtrack[0] = 0;
        // O(n)
        while (j < strlen(sub_string)) {
            if (sub_string[i] == sub_string[j]) {
                backtrack[j] = i + 1;
                i++;
                j++;
            } else {
                if (i > 0 && backtrack[i - 1] >= 0) {
                    i = backtrack[i - 1];
                } else {
                    backtrack[j] = 0;
                    j++;
                }
            }
        }
        
        FILE *test_file = fopen("KMP_test.txt", "r");
        
        char line[256];
        // When mismatch, index should become = backtrack[index - 1] + 1 or 0
        
        int flag = 0;
        int index = 0;
        int line_count = 0;
        while (fgets(line, sizeof(line), test_file)) {
            // O(n)
            for (i = 0; i < strlen(line); i++) {
                if (line[i] == sub_string[index]) {
                    index++;
                    if (index == strlen(sub_string)) {
                        printf("Found at line %d:%d\n", line_count, i);
                        flag = 1;
                        index--;
                    }
                } else {
                    if (index > 0) {
                        index = backtrack[index - 1] + 1;
                    } else {
                        index = 0;
                    }
                }
            }
            if (flag) printf("%s\n", line);
            flag = 0;
            line_count++;
        }        
        
        fclose(test_file);

    }
}










