LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW6\SAS Output HW6-2.pdf";
DATA students;
	set lib.students;
RUN;

PROC REG DATA=students;
MODEL FEXAM = IQ MSAT PEXAM / SELECTION=B SLS = 0.05;
TITLE 'Q2: Predict Final Exam Score With Significance of 0.05';
RUN;

ODS PDF CLOSE;
