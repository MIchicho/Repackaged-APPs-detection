SOURCES_DIR:=sources
OBJ_DIR:=bin
OUT_DIR:=bin
TEST_DIR:=$(SOURCES_DIR)

#H_SOURCES:=`find $(SOURCES_DIR) -name "*.h"`
#CPP_SOURCES:=`find $(SOURCES_DIR) -name "*.cpp"`
#TEST_SOURCES:=`find $(TEST_DIR) -name "*.cpp"`
OBJ_SOURCES:=$(SOURCES_DIR)/BucketHashing.cpp \
	     $(SOURCES_DIR)/Geometry.cpp \
	     $(SOURCES_DIR)/LocalitySensitiveHashing.cpp \
	     $(SOURCES_DIR)/Random.cpp \
	     $(SOURCES_DIR)/Util.cpp \
	     $(SOURCES_DIR)/GlobalVars.cpp \
	     $(SOURCES_DIR)/SelfTuning.cpp \
	     $(SOURCES_DIR)/NearNeighbors.cpp

LSH_BUILD:=LSHMain

TEST_BUILDS:=exactNNs \
            genDS \
	    compareOutputs \
	    genPlantedDS

GCC:=g++
OPTIONS:=-O3 -DREAL_FLOAT -DDEBUG
# -march=athlon -msse -mfpmath=sse
LIBRARIES:=-lm 
#-ldmalloc

all: 
	bin/compile

c: compile

compile:
	@mkdir -p $(OUT_DIR)
	$(GCC) -o $(OUT_DIR)/$(LSH_BUILD) $(OPTIONS) $(OBJ_SOURCES) $(SOURCES_DIR)/$(LSH_BUILD).cpp $(LIBRARIES)
	chmod g+rwx $(OUT_DIR)/$(LSH_BUILD)

ct:
	@mkdir -p $(OUT_DIR)
	(for i in $(TEST_BUILDS); do \
	 $(GCC) -o $(OUT_DIR)/$$i $(OPTIONS) $(OBJ_SOURCES) $(TEST_DIR)/$${i}.cpp $(LIBRARIES); chmod g+rwx $(OUT_DIR)/$$i; done)

zip:
	zip -r LSHarchive.zip Makefile sources bin Documentation
	chmod g+rw LSHarchive.zip


ship:
	\rm -rf E2LSH-0.1
	mkdir E2LSH-0.1
	cp -r manual.ps sources Makefile gpl.txt E2LSH-0.1
	\rm -rf E2LSH-0.1/sources/CVS
	cp mnist1k.dts05 E2LSH-0.1/mnist1k.dts
	cp mnist10k_q05 E2LSH-0.1/mnist1k.q
	mkdir E2LSH-0.1/bin
	cp bin/compile bin/exact bin/lsh* E2LSH-0.1/bin 
	\rm -f E2LSH-0.1.tar E2LSH-0.1.tar.gz
	tar -cvf E2LSH-0.1.tar E2LSH-0.1/
	gzip -c E2LSH-0.1.tar > E2LSH-0.1.tar.gz
	\rm -f E2LSH-0.1.tar
	chmod -R g+rw E2LSH-0.1
	chmod g+rw E2LSH-0.1.tar.gz
