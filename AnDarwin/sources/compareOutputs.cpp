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

#include <stdio.h>
#include <stdlib.h>

#include "headers.h"

void usage(char *programName){
  printf("Usage: %s correct_output lsh_output\n", programName);
}

IntT main(IntT nargs, char **args){
  if (nargs < 2){
    usage(args[0]);
    exit(1);
  }

  FILE *fCorrect = fopen(args[1], "rt");
  FAILIF(fCorrect == NULL);
  FILE *fLSH = fopen(args[2], "rt");
  FAILIF(fLSH == NULL);

  IntT nTotalCorrect = 0;
  IntT nTotalLSH = 0;
  IntT overallOK = 1;

  IntT nPoints;
  fscanf(fCorrect, "nPoints = %d\n", &nPoints);
  IntT *pointsNN = (int*)calloc(nPoints, sizeof(int));
  IntT nCorrect = 0;
  char s[1000];
  char c;
  IntT x;
  IntT nQuery = 0;
  c = ' ';
  while(!feof(fCorrect)){
    // find the start of the query (letter Q).
    while (!feof(fCorrect) && (c != 'Q')) {
      fscanf(fCorrect, "%c", &c);
      if (c != '0') {
	fscanf(fCorrect, "%[^\n]", s);
	fscanf(fCorrect, "\n");
      }
    };

    //printf("%c\n", c);
    
    if (!feof(fCorrect)){
      do {
	fscanf(fCorrect, "%c", &c);
	if (c != '0') {
	  fscanf(fCorrect, "%[^\n]", s);
	  fscanf(fCorrect, "\n");
	}else{
	  fscanf(fCorrect, "%d\n", &x);
	  pointsNN[x] = 3 * nQuery + 1;
	  nCorrect++;
	  nTotalCorrect++;
	}
      } while (!feof(fCorrect) && (c == '0'));
    }
    
    IntT ok = 1;
    IntT nLSH = 0;
    char g = ' ';
    while(!feof(fLSH) && (g != 'Q')){
      fscanf(fLSH, "%c", &g);
      if (g != '0') {
	fscanf(fLSH, "%[^\n]", s);
	fscanf(fLSH, "\n");
      }
    }

    if (!feof(fLSH)){
      do {
	fscanf(fLSH, "%c", &g);
	if (g != '0') {
	  fscanf(fLSH, "%[^\n]", s);
	  fscanf(fLSH, "\n");
	}else{
	  fscanf(fLSH, "%d\n", &x);
	  fscanf(fLSH, "%[^\n]", s);
	  fscanf(fLSH, "\n");
	  if (pointsNN[x] >= 3 * nQuery + 2 ){
	    // LSH reported a poIntT more than once.
	    ok = 0;
	    printf("Error: LSH reported a poIntT (%d) more than once.\n", x);
	  }
	  if (pointsNN[x] <= 3 * nQuery){
	    // LSH reported a poIntT that is not reported by exact NN.
	    ok = 0;
	    printf("Error: LSH reported a poIntT (%d) that was not reported by NN.\n", x);
	  }
	  pointsNN[x] = 3 * nQuery + 2;
	  nLSH++;
	  nTotalLSH++;
	}
      } while (!feof(fLSH) && (g == '0'));
    }

    printf("OK = %d. NN_LSH/NN_Correct = %d/%d=%0.3lf\n", ok, nLSH, nCorrect, (nCorrect > 0)?((double)nLSH/(double)nCorrect):1);
    if (ok == 0){
      overallOK = 0;
    }
    nCorrect = 0;
    nQuery++;
  }

  printf("\nOverall: OK = %d. NN_LSH/NN_Correct = %d/%d=%0.3lf\n", overallOK, nTotalLSH, nTotalCorrect, (nTotalCorrect > 0)?((double)nTotalLSH/(double)nTotalCorrect):1);

  fclose(fCorrect);
  fclose(fLSH);
}
