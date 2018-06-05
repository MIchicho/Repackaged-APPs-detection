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

#ifndef GLOBALVARS_INCLUDED
#define GLOBALVARS_INCLUDED

#ifndef GLOBALVARS_CPP
#define DECLARE_EXTERN extern
#define EXTERN_INIT(x)
#else
#define DECLARE_EXTERN
#define EXTERN_INIT(x) x
#endif

DECLARE_EXTERN MemVarT availableTotalMemory EXTERN_INIT(= DEFAULT_MEMORY_MAX_AVAILABLE);

DECLARE_EXTERN TimeVarT timeComputeULSH;
DECLARE_EXTERN TimeVarT timeGetBucket;
DECLARE_EXTERN TimeVarT timeCycleBucket;
DECLARE_EXTERN TimeVarT timeDistanceComputation;
DECLARE_EXTERN TimeVarT timeResultStoring;
DECLARE_EXTERN TimeVarT timePrecomputeHash;
DECLARE_EXTERN TimeVarT timeGBHash;
DECLARE_EXTERN TimeVarT timeChainTraversal;
DECLARE_EXTERN TimeVarT timeBucketCreation;
DECLARE_EXTERN TimeVarT timeBucketIntoUH;
DECLARE_EXTERN TimeVarT timeCycleProc;
DECLARE_EXTERN TimeVarT timeRNNQuery;
DECLARE_EXTERN TimeVarT timeCopyingULSHs;
DECLARE_EXTERN TimeVarT timeTotalBuckets;
DECLARE_EXTERN TimeVarT timeUnmarking;

DECLARE_EXTERN BooleanT timingOn EXTERN_INIT(= TRUE);
DECLARE_EXTERN TimeVarT currentTime EXTERN_INIT(= 0);
DECLARE_EXTERN TimeVarT timevSpeed EXTERN_INIT(= 0);

DECLARE_EXTERN IntT nOfDistComps EXTERN_INIT(= 0);
DECLARE_EXTERN MemVarT totalAllocatedMemory EXTERN_INIT(= 0);
DECLARE_EXTERN IntT nGBuckets EXTERN_INIT(= 0);
DECLARE_EXTERN IntT nBucketsInChains EXTERN_INIT(= 0);
//DECLARE_EXTERN IntT nPointsInBuckets EXTERN_INIT(= 0); // total # of points found in collinding buckets (including repetitions)
DECLARE_EXTERN IntT nAllocatedGBuckets EXTERN_INIT(= 0);
DECLARE_EXTERN IntT nAllocatedBEntries EXTERN_INIT(= 0);

DECLARE_EXTERN BooleanT noExpensiveTiming  EXTERN_INIT(= FALSE);


#endif
