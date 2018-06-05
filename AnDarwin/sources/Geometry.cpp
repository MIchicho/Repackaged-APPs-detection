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

// SqrDistanceT computeSqrDistance(PointT p1, PointT p2){
//   SqrDistanceT result = 0;
//   IntT n = MIN(p1.dimension, p2.dimension);

//   for (IntT i = 0; i < n; i++)
//     result += SQR(p1.coordinates[i] - p2.coordinates[i]);

//   return result;
// }


// Compares according to the field "real" of the struct.
int comparePPointAndRealTStructT(const void *a, const void *b){
  PPointAndRealTStructT *x = (PPointAndRealTStructT*)a;
  PPointAndRealTStructT *y = (PPointAndRealTStructT*)b;
  return (x->real > y->real) - (x->real < y->real);
}


#ifdef USE_L1_DISTANCE
// Returns the L1 distance from point <p1> to <p2>.
RealT distance(IntT dimension, PPointT p1, PPointT p2){
  RealT result = 0;

  for (IntT i = 0; i < dimension; i++){
    result += ABS(p1->coordinates[i] - p2->coordinates[i]);
  }

  return result;
}
#else
// Returns the Euclidean distance from point <p1> to <p2>.
RealT distance(IntT dimension, PPointT p1, PPointT p2){
  RealT result = 0;

  for (IntT i = 0; i < dimension; i++){
    result += SQR(p1->coordinates[i] - p2->coordinates[i]);
  }

  return SQRT(result);
}
#endif
