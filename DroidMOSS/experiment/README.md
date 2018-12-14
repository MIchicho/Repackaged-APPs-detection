How to run the DroidMOSS

1. first you should download the dexdump to get the opcode of apk

2. run the file  python parseDexOpcode.py you can get the opcode sequence


you can find the detailed messages in the  parseDexOpcode.py


# function  : 1. use the tool dexdump to decompile the dex file
#             2. get the opcode and store it in a file name apkName.txt
#             3. All of these files are store under the directory Juxtapp
# running   : Two methods
#             1. python parseDexOpcode.py
#             2. python parseDexOpcode.py  your PATH



'''
============================================================
running  : python parseDexOpcode.py
You can input different number to choose which path you want 
to use 
************************************************************
input : 0 -> original APKs  ~/workspace/repackaged/result/original/ 
input : 1 -> repackaged APKs ~/workspace/repackaged/result/repackaged/
input : 2 -> test PATH 
input : 3 -> your PATH  
============================================================
'''

you have two methods to run this files



3. When we get the opcode sequences we should use the Fuzzyhash to get the fingerprint


we  should install ssdeep on our computer, you can find the files in the FuzzyHashing 


follow the tips you can install the files



4. run the file python dexSimilarityComparsion.py

# function :  1. we compare the dex file between the original apks
#             and repackaged apks 
#             2. set the different threshold and get the best result 
#             3. write the report 
# tip      :  we should install the ssdeep first 



you can find the usage in the file and you can change the path into your personal apk Path


4. use the edit distance to get the similar Value

python editDistance.py

5. python findsimilarAPK.py  get the similar app pairs.
