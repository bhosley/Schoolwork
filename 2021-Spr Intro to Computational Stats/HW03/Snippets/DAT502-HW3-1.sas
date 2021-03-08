ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW3\SAS Output HW3-1.pdf";
LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

PROC UNIVARIATE DATA = students PLOTS;
VAR teff;
RUN;

ODS PDF CLOSE;
