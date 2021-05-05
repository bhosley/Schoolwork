LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW6';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW6\SAS Output HW6-5.pdf";
DATA regp3;
	set lib.regp3;
	Xsq = X*X;
RUN;

PROC REG DATA=regp3 ALPHA=0.03;
MODEL Y = X Xsq / CLI CLB CLM;
TEST X=200;
TITLE 'Q5: Best Fit Regression';
RUN;

ODS PDF CLOSE;
