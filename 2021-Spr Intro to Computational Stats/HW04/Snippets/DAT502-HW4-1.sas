LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW4\SAS Output HW4-1.pdf";
DATA students;
	set lib.students;
RUN;

PROC TTEST DATA = students H0=70 SIDE=U;
VAR fexam;
RUN;

ODS PDF CLOSE;
