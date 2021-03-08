ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW3\SAS Output HW3-2.pdf";
LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

PROC SUMMARY DATA = students;
CLASS mj;
VAR teff;
OUTPUT OUT=summary MEAN=TeffMean STD=StDev T=T;
PROC PRINT;

ODS PDF CLOSE;
