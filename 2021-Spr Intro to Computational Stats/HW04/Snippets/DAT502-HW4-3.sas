LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW4\SAS Output HW4-3.pdf";

DATA students;
	SET lib.students;
	IF cl = 'SO' | cl ='SR' THEN DELETE;

PROC SORT DATA = students;
	BY cl;

PROC TTEST DATA = students;
	VAR msat;
	CLASS cl;
RUN;

ODS PDF CLOSE;
