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

#ifndef SELFTUNING_INCLUDED
#define SELFTUNING_INCLUDED

void tuneTimeFunctions();

void sortQueryPointsByRadii(IntT dimension,
			    Int32T nQueries, 
			    PPointT *queries, 
			    Int32T nPoints, 
			    PPointT *dataSet,
			    IntT nRadii,
			    RealT *radii,
			    Int32T *boundaryIndeces);

void determineRTCoefficients(RealT thresholdR, RealT successProbability, BooleanT useUfunctions, IntT typeHT, IntT dimension, Int32T nPoints, PPointT *realData, RealT &lshPrecomp, RealT &uhashOver, RealT &distComp);

RealT estimateNCollisions(IntT nPoints, IntT dim, PPointT *dataSet, PPointT query, IntT k, IntT L, RealT R);

RealT estimateNDistinctCollisions(IntT nPoints, IntT dim, PPointT *dataSet, PPointT query, BooleanT useUfunctions, IntT hfTuplesLength, IntT nHFTuples, RealT R);

RealT computeFunctionP(RealT w, RealT c);

IntT computeLfromKP(IntT k, RealT successProbability);

IntT computeMForULSH(IntT k, RealT successProbability);

RNNParametersT computeOptimalParameters(RealT R, RealT successProbability, IntT nPoints, IntT dimension, PPointT *dataSet, IntT nSampleQueries, PPointT *sampleQueries, MemVarT memoryUpperBound);


#endif
