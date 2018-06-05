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

/*
  This program generates the input data set. The arguments are:
  dimension M #_of_points R probability_of_success

  The points are generated uniformly at random in the range [-M, M]^d.
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "BasicDefinitions.h"
#include "Random.h"

void usage(char *programName){
  printf("Usage: %s dimension max_size #_of_points R probability_of_success\n", programName);
}

int main(int nargs, char **args){
  if (nargs < 5){
    usage(args[0]);
    exit(1);
  }

  IntT dimension = atoi(args[1]);
  RealT M = atof(args[2]);
  IntT nPoints = atoi(args[3]);
  RealT R = atof(args[4]);
  //IntT nExpNNs = atoi(args[4]);
  RealT probability = atof(args[5]);

  // for d even, Vol_d = pi^{d/2} / (d/2)!


  // RealT vol_d_const = 1.0 / SQRT(M_PI * (RealT)dimension);

  // RealT R = 2.0 * M * POW((RealT)nExpNNs / (RealT)nPoints / vol_d_const, 1.0/(RealT)dimension) / SQRT(M_PI) * SQRT((RealT)dimension / 2.0 / M_E);
  
//   RealT vol_d_const = 1;
//   for(IntT i = 1; i <= dimension / 2; i++)
//     vol_d_const = vol_d_const * M_PI / (RealT)i;

//   RealT R = 2.0 * M * POW((RealT)nExpNNs / (RealT)nPoints / vol_d_const, 1.0/(RealT)dimension);
  
  //printf("%Lf %Lf \n", POW(R/2.0/M, dimension), (RealT)nExpNNs / (RealT)nPoints / vol_d_const);
  printf("%d %d ", nPoints, dimension);
  FPRINTF_REAL(stdout, R);
  printf(" ");
  FPRINTF_REAL(stdout, probability);
  printf("\n");

  for(IntT d = 0; d < dimension; d++){
    FPRINTF_REAL(stdout, 0.99 * R / SQRT(dimension));
    printf(" ");
  }
  printf("\n");

  for(IntT i = 0; i < nPoints - 1; i++){
    for(IntT d = 0; d < dimension; d++){
      FPRINTF_REAL(stdout, genUniformRandom(-M, M));
      printf(" ");
    }
    printf("\n");
  }
}
