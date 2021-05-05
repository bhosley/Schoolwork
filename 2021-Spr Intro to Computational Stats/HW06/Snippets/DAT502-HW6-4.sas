LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW6';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW6\SAS Output HW6-4.pdf";
DATA regp3;
	set lib.regp3;
RUN;

PROC REG DATA=regp3 ALPHA=0.1;
MODEL Y = X / CLB;
TITLE 'Q4: Simple Linear Regression';
RUN;

ODS PDF CLOSE;
