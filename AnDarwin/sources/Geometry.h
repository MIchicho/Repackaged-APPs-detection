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

#ifndef GEOMETRY_INCLUDED
#define GEOMETRY_INCLUDED

// A simple point in d-dimensional space. A point is defined by a
// vector of coordinates. 
typedef struct _PointT {
  //IntT dimension;
  IntT index; // the index of this point in the dataset list of points
  RealT *coordinates;
  RealT sqrLength; // the square of the length of the vector
} PointT, *PPointT;

// Encapsulates a PPoint and a RealT in a single struct.
typedef struct _PPointAndRealTStructT {
  PPointT ppoint;
  RealT real;
} PPointAndRealTStructT;

int comparePPointAndRealTStructT(const void *a, const void *b);

RealT distance(IntT dimension, PPointT p1, PPointT p2);

#endif
