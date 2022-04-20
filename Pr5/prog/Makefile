CC=g++
FLAGS=-c

all: Coco.o APC_VecMat3D.o APC_Time.o APC_Math.o APC_Sun.o APC_Spheric.o APC_PrecNut.o
	$(CC) Coco.o APC_VecMat3D.o APC_Time.o APC_Math.o APC_Sun.o APC_Spheric.o APC_PrecNut.o

Coco.o: Coco.cpp
	$(CC) $(FLAGS) Coco.cpp

APC_VecMat3D.o: APC_VecMat3D.cpp
	$(CC) $(FLAGS) APC_VecMat3D.cpp

APC_Time.o: APC_Time.cpp
	$(CC) $(FLAGS) APC_Time.cpp

APC_Sun.o: APC_VecMat3D.h APC_Sun.cpp
	$(CC) $(FLAGS) APC_Sun.cpp

APC_Spheric.o: APC_Spheric.cpp
	$(CC) $(FLAGS) APC_Spheric.cpp

APC_PrecNut.o: APC_PrecNut.cpp
	$(CC) $(FLAGS) APC_PrecNut.cpp

APC_Math.o: APC_Math.cpp
	$(CC) $(FLAGS) APC_Math.cpp

clean:
	rm *.o
	rm *.gch
