LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW3\SAS Output HW3-4.pdf";
PROC CORR DATA = students;
VAR msat iq pexam;
WITH fexam teff;
PROC PRINT;

ODS PDF CLOSE;
