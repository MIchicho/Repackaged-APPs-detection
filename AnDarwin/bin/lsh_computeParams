#!/bin/bash

successProbability=0.9


if [ $# -le 1 ]; then
  echo Usage: $0 radius data_set_file "{query_set_file | .} [successProbability]"
  exit
fi

if [ $# -ge 4 ]; then
 # success probability supplied
 successProbability=$4
fi

arch=`uname`
nDataSet=` wc -l "$2"`
for x in $nDataSet; do nDataSet=$x; break; done
if [ "$3" != "." ]; then
  nQuerySet=` wc -l "$3"`
  for x in $nQuerySet; do nQuerySet=$x; break; done
else
  nQuerySet=0
fi
dimension=`head -1 "$2" | wc -w`

#echo $nDataSet $nQuerySet $dimension



if [ -e bin/mem ]; then
  m=`cat bin/mem`;
elif [ "$arch" = "Darwin" ]
then
  #http://discussions.apple.com/thread.jspa?threadID=1608380&tstart=0
  m=`top -l 1 | grep PhysMem | awk -F "[M,]" ' {print$10 }'`
  let m=m*1024*1024
  echo $m > bin/mem
else
  s=`free -m | grep "Mem:"`
  for i in $s; do m=$i; if [ "$i" != "Mem:" ]; then break; fi; done
  m=${m}000000
  echo $m > bin/mem
fi


bin/LSHMain $nDataSet $nQuerySet $dimension $successProbability "$1" "$2" "$3" $m -c
