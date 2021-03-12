LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW3\SAS Output HW3-3.pdf";
PROC UNIVARIATE NORMAL PLOT DATA = students;
VAR iq;
RUN;

ODS PDF CLOSE;
