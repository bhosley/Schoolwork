LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW2\SAS Output HW2-1.pdf";
ODS LATEX path="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW2" file="SAS Output HW2-1.tex";

PROC SORT DATA=students;
BY MJ;

PROC PRINT D N DATA=students SPLIT=' ';
ID CL; 
VAR SEX MSAT PEXAM FEXAM FG TEFF;
BY MJ;
SUM TEFF;
TITLE 'Teaching Efficiency by Major';
RUN;

ODS PDF CLOSE;
ODS LATEX CLOSE;
