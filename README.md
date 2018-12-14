How to use the ResDroid

1. we need to download thress tools
1. apktool
2. dex2jar
3. A3E


install the apktool and dex2jar 

install jdk, unzip

We also improve the tools Gator to get the Event handler information and each UIs,

You can get the Gator form thw website 
http://web.cse.ohio-state.edu/presto/software/gator/


1. we can run the feedQAPKforGator1.py to get the UIs and event handler information

================================================
You can use the default apk files's path or input the path you like!
usage: python feedQAPKforGator.py <apk_path> <Output_path>
Example : python feedQAPKforGator.py /home/chicho/test/APK /home/chicho/test/Output_path
Input : 0 -> default path
Input : 1 -> you personal path
================================================


when you change the apk files into the IR, you should run the runSootAndroid.py  file to get the event handler info and GUI

handlerExtract.sh can extract the event handler

2. When you download the a3e tools you should put the file createSatg.py into the a3e-master/satg
runing the file python createSatg.py you can create the ATG


3. python calculate_resref.py you can get the statistical resources information

this file needs the other file conf.py you can put these two files in the same directory

when you are running the file calculate_resref.py you can get the statistical results of resources

and these results can be store in the mysql database.

python insertStatis_feature.py you can insert the statistical results into the database.

You should install a mysql databases in your computer. If you do not have any knowledge about database

you can run other files to get the results.

the file ./ResDroid/new/calculate_resref.py   

by running this file, all the results will be stores in the files

4. if you want to use any clustering algorithm. you can find the directory named clustering

You can modify the path of in each algorithm and get the cluster result.

you can run the spectral clustering algorithm in this way:

python SpectralClusering.py


5. the kd-tree algorithm you can find in the directory.


6. When you get the statistical resources vector you can run the file 
python calstatisVecDist.py to calculate the similarity 


7. When you get the AS, you can run the python LCS.py to get the similar score  

the more experiment code you can find in the directory name experiment.



