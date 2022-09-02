LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

PROC SORT DATA=students;
BY MJ;

PROC PRINT D N DATA=students SPLIT=' ';
ID CL; 
VAR SEX MSAT PEXAM FEXAM FG TEFF;
BY MJ;
SUM TEFF;
TITLE 'Teaching Efficiency by Major';
RUN;
