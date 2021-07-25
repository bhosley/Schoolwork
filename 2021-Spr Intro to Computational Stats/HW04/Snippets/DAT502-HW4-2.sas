LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW4\SAS Output HW4-2.pdf";

DATA students;
	SET lib.students;
	IF mj = 'MAT' THEN matmaj = 'Yes';
	ELSE matmaj = 'No';
	LABEL matmaj = 'Is Math Major';
RUN;

PROC SORT DATA = students;
	BY matmaj;

PROC TTEST DATA = students;
	VAR msat;
	CLASS matmaj;
RUN;

ODS PDF CLOSE;
