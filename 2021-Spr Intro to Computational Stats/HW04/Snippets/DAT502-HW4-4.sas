LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW4\SAS Output HW4-4.pdf";

DATA students;
	SET lib.students;

PROC TTEST DATA=students H0=15 SIDE=L;
	VAR teff;
RUN;

ODS PDF CLOSE;
