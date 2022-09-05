LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

PROC G3D DATA=students;
TITLE 'Math-SAT, IQ, and Teaching Efficiency';
SCATTER MSAT*IQ=TEFF;
RUN;
