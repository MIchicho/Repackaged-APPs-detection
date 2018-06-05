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

#ifndef NEARNEIGHBORS_INCLUDED
#define NEARNEIGHBORS_INCLUDED

void initializeLSHGlobal();

PRNearNeighborStructT initSelfTunedRNearNeighborWithDataSet(RealT thresholdR, RealT successProbability, Int32T nPoints, IntT dimension, PPointT *dataSet, IntT nSampleQueries, PPointT *sampleQueries, MemVarT memoryUpperBound);

Int32T getRNearNeighbors(PRNearNeighborStructT nnStruct, PPointT queryPoint, PPointT *(&result), Int32T &resultSize);

#endif
