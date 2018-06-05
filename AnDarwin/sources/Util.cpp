/*
 *   Copyright (c) 2004-2005 Massachusetts Institute of Technology.
 *   All Rights Reserved.
 *
 *   This program is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, either version 3 of the License, or
 *   (at your option) any later version.
 *
 *   This program is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *   Authors: Alexandr Andoni (andoni@mit.edu), Piotr Indyk (indyk@mit.edu)
*/

#include "headers.h"

// Verifies whether vector v1 and v2 are equal (component-wise). The
// size of the vectors is given by the parameter size.
BooleanT vectorsEqual(IntT size, IntT *v1, IntT *v2){
  for(IntT i = 0; i < size; i++){
    if (v1[i] != v2[i]){
      return FALSE;
    }
  }
  return TRUE;
}

// Copies the vector <from> to the vector <to>. The size of the
// vectors is given by <size>.
void copyVector(IntT size, IntT *from, IntT *to){
  for(IntT i = 0; i < size; i++){
    to[i] = from[i];
  }
}

// Creates a new vector of size <size> and copies the vector <from> to
// the new vector.
IntT *copyOfVector(IntT size, IntT *from){
  IntT *newVector;
  FAILIF(NULL == (newVector = (IntT*)MALLOC(size * sizeof(IntT))));
  for(IntT i = 0; i < size; i++){
    newVector[i] = from[i];
  }
  return newVector;
}

// Prints the vector <v> of size <size>. The string <s> appears
// in front.
void printRealVector(char *s, IntT size, RealT *v){
  ASSERT(v != NULL);
  
  printf("%s", s);
  for(IntT i = 0; i < size; i++){
    if (i > 0){
      printf(" ");
    }
    printf("%0.2lf", (double)v[i]);
  }

  printf("\n");
}

// Prints the vector <v> of size <size>. The string <s> appears
// in front.
void printIntVector(char *s, IntT size, IntT *v){
  ASSERT(v != NULL);
  
  printf("%s", s);
  for(IntT i = 0; i < size; i++){
    if (i > 0){
      printf(" ");
    }
    printf("%d", v[i]);
  }

  printf("\n");
}

// Returns the amount of available memory.
MemVarT getAvailableMemory(){
  // TODO
  //printf("mem=%lu\n", MEMORY_MAX_AVAILABLE - totalAllocatedMemory);
  FAILIFWR(availableTotalMemory < totalAllocatedMemory, "Not enough memory.\n");
  return availableTotalMemory - totalAllocatedMemory; 
}
