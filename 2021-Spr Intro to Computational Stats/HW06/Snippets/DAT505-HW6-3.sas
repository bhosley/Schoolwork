LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW6\SAS Output HW6-3.pdf";
DATA students;
	set lib.students;
RUN;

PROC REG DATA=students ALPHA=0.02;
MODEL FEXAM = IQ;
TITLE 'Q3: 98% Confidence Interval based on IQ';
RUN;

ODS PDF CLOSE;
