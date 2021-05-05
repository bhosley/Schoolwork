LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW6\SAS Output HW6-1.pdf";
DATA students;
	set lib.students;
RUN;

PROC REG DATA=students;
MODEL FEXAM = IQ MSAT PEXAM;
TITLE 'Q1: Predict Final Exam Score';
RUN;

ODS PDF CLOSE;
