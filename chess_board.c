#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 4

/*
 * In hindsight, this is actually a DP solution. I never realised.
 * 
 * From an algorithm midterm, "every square of a n*n chess board is an int, you can only 
 * move downwards or right, everytime you move on a square you add it to your sum, maximise that sum"
 * I thought this was a cool question, I made a copy board that maps it out, basically change
 * each tile to it's local max (from a move downwards or right).

    2 | 3 | 4         2 | 3 | 4     2 | 3 | 4       2 | 3 | 4
    1 | 2 | 3 -->   (3) | 2 | 3 --> 3 |(5)| 3 -->   3 | 5 | 8


*/

int main(int argc, char *argv[]) {

    srand(time(NULL));
    int map[SIZE][SIZE];
    int i, j;
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            map[i][j] = 1 + rand() % 7;
        }
    }
    printf("The original board: \n");
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            printf("%3d ", map[i][j]);
        }
        printf("\n");
    }
    
    int copy[SIZE][SIZE];
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            copy[i][j] = map[i][j]; 
        }
    }    
    
    // J = column, I = row
    
    for (i = 0; i < SIZE; i++) {            
        for (j = 0; j < SIZE; j++) {    
            if (!i && !j) {                                 // Ignoring (0, 0)
                continue;
            } else if (!i) {                                // If first row, only right move able
                copy[i][j] = copy[i][j] + copy[i][j-1];
            } else if (i == SIZE - 1) {                     // If last row, only downwards move able
                copy[i][j] = copy[i][j] + copy[i-1][j];
            } else if (!j) {                                // If first column, only downwards move able
                copy[i][j] = copy[i-1][j] + copy[i][j];
            } else {
                if (copy[i][j-1] > copy[i-1][j]) {
                    copy[i][j] = copy[i][j] + copy[i][j-1];
                } else {
                    copy[i][j] = copy[i][j] + copy[i-1][j];
                }
            }
        }
    }    
    
    printf("\n\nThe new board is: \n");
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            printf("%3d ", copy[i][j]);
        }
        printf("\n");
    }
    
    // Almost always the right hand corner that is the largest (some exceptions). You get much more moves
    // by moving right before down at the end. More probable as board increases size
    
    int max = 0;
    int index = 0;
    for (i = SIZE - 1; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            if (copy[i][j] > max) {
                max = copy[i][j];
                index = j;
            }
        }
    }        
    printf("The max value was %d at (%d, %d)\n", max, SIZE-1, index);

    return EXIT_SUCCESS;
}


