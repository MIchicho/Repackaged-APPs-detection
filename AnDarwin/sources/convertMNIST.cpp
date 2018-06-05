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
#include <math.h>

#define ASSERT(b) { if (!(b)) {printf("Error at line %d.\n", __LINE__); exit(1);}}

double **points;
int nPoints;
double R = 100;
int dim;
double lowerR;
double upperR;

int genRandomInt(int rangeStart, int rangeEnd){
  int r;
  r = rangeStart + (int)((rangeEnd - rangeStart + 1.0) * random() / (RAND_MAX + 1.0));
  return r;
}

double distance(int i, int j){
  double r = 0;
  for(int d = 0; d < dim; d++){
    double x = points[i][d] - points[j][d];
    r += x * x;
  }
  return sqrt(r);
}

static int compareDoubles(const void *a, const void *b){
  if (*((double *)a) < *((double *)b))
    return -1;
  if (*((double *)a) == *((double *)b))
    return 0;
  return 1;
}


void printP(int i){
  for(int d = 0; d < dim; d++){
    if (fabs(points[i][d]) >= 0.000000001){
      printf("%0.6lf ", points[i][d]);
    }else{
      printf("0 ");
    }
  }
  printf("\n");
}

void printPoints(char *file){
  FILE *f = fopen(file, "wt");
  //fprintf(f, "%d %d %lf 0.9\n", nPoints, dim, upperR * 1.0001);
  for(int i = 0; i < nPoints; i++){
    for(int d = 0; d < dim; d++){
      if (fabs(points[i][d]) >= 0.000000001){ 
	fprintf(f, "%0.6lf ", points[i][d]);
      }else{
	fprintf(f, "0 ");
      }
    }
    fprintf(f, "\n");
  }
  fclose(f);
}

int main(){
  FILE *f = fopen("train-images-idx3-ubyte", "r");
  ASSERT(f != NULL);
  int a;
  fread(&a, 4, 1, f);
  a = ((a & 0xFF000000) >> 24) + ((a & 0x00FF0000) >> 8) + ((a & 0x0000FF00) << 8) + ((a & 0x000000FF) << 24);
  ASSERT(a == 2051);
  fread(&a, 4, 1, f);
  nPoints = ((a & 0xFF000000) >> 24) + ((a & 0x00FF0000) >> 8) + ((a & 0x0000FF00) << 8) + ((a & 0x000000FF) << 24);
  //ASSERT(nPoints == 10000);

  int r, c;

  fread(&a, 4, 1, f);
  r = ((a & 0xFF000000) >> 24) + ((a & 0x00FF0000) >> 8) + ((a & 0x0000FF00) << 8) + ((a & 0x000000FF) << 24);
  fread(&a, 4, 1, f);
  c = ((a & 0xFF000000) >> 24) + ((a & 0x00FF0000) >> 8) + ((a & 0x0000FF00) << 8) + ((a & 0x000000FF) << 24);
  
  dim = r * c;

  //printf("dim = %d\n", dim);

  points = (double**)malloc(nPoints * sizeof(double*));

  //printf("%d", sizeof(unsigned));
  for(int p = 0; p < nPoints; p++){
    points[p] = (double*)malloc(dim * sizeof(double));
    for(int i = 0; i < dim; i++){
      unsigned b = 0;
      fread(&b, 1, 1, f);
      //printf("%0x\t", b);
      points[p][i] = b;
    }
  }

  fclose(f);

  for(int p = 0; p < nPoints; p++){
    double norm = 0;
    for(int d = 0; d < dim; d++){
      norm += points[p][d] * points[p][d];
    }
    norm = sqrt(norm);
    if (norm > 0) {
      for(int d = 0; d < dim; d++){
	points[p][d] /= norm;
      }
    }
  }


  //printPoints();
  //exit(0);

  double freqs[100];
  for(int i = 0; i < 100; i++){
    freqs[i] = 0;
  }
  srandom(1);


  int nReps = 200;
  lowerR = 0.5;
  upperR = 0.53;


  double F;
  double increment = 1.1;
  int count;
  int j;
  double *dist = (double*)malloc(nPoints * sizeof(double));
  //printf("nPoints = %d\n", nPoints);
  int qpts[nReps];
  int nqpts = 0;
  for(int rep = 0; rep < nReps; rep++){
    int q = genRandomInt(0, nPoints - 1);
    double minDist = 10E+10;
    for(int i = 0; i < nPoints; i++){
      dist[i] = distance(q, i);
      if (q != i && minDist > dist[i]){
	minDist = dist[i];
      }
    }
    qsort(dist, nPoints, sizeof(double), compareDoubles);
    if (dist[1] >= lowerR && dist[1] < upperR){
      //printf("q=%d\t(rep = %d)\n", q, rep);
      //printf("minDist = %lf\tdist[500]/R=%lf \n", dist[1], dist[500] / dist[1]);
      printP(q);
      for(int d = 0; d < dim; d++){
	points[q][d] = points[nPoints - 1][d];
      }
      nPoints--;
    }



//     R = dist[1] * 1.00001;
//     printf("R=%lf\n", R);
//     F = R;
//     count = 1;
//     j = 0;

//     for(int i = 2; i < nPoints; i++){
//       if (dist[i] > F){
// 	freqs[j++] += count;
// 	count = 0;
// 	//printf("Dist: %0.3lf\tN: %d\n", F / R, count);
// 	F = F * increment;
// 	i--;
//       } else {
// 	count++;
//       }
//     }
//     //printf("Dist: %0.3lf\tN: %d\n", F / R, count);
//     freqs[j++] += count;
  }

//   F = 1;
//   double total = 0;
//   for(int i = 0; i < 100; i++){
//     total += freqs[i] / (double)nReps;
//     printf("Dist: %0.3lf\tN: %0.1lf\n", F, total);
//     F = F * increment;
//   }
  

//   for(int i = 0; i < nPoints; i++){
//     printf("%0.3lf\n", dist[i]);
//   }

//   printf("%d %d %0.3lf 0.9\n", nPoints, dim, R);

//   for(int p = 0; p < nPoints; p++){
//     for(int i = 0; i < dim; i++){
//       printf("%0.5lf ", points[p][i]);
//     }
//     printf("\n");
//   }

  printPoints("mnist60k.dts05");

}
