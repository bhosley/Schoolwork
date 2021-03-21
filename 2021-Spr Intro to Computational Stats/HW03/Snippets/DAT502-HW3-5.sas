LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

PROC SORT DATA=students;
BY mj;

ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW3\SAS Output HW3-5.pdf";
PROC MEANS DATA = students;
VAR teff;
BY mj;
OUTPUT P95=ConfInt;
PROC PRINT;

ODS PDF CLOSE;
