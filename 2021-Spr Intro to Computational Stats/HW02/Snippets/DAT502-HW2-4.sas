LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW2\SAS Output HW2-4.pdf";
ODS LATEX path="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW2" file="SAS Output HW2-4.tex";

PROC G3D DATA=students;
TITLE 'Math-SAT, IQ, and Teaching Efficiency';
SCATTER MSAT*IQ=TEFF;
RUN;

ODS PDF CLOSE;
ODS LATEX CLOSE;
