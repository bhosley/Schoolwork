LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW2\SAS Output HW2-3.pdf";
ODS LATEX path="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW2" file="SAS Output HW2-3.tex";

SYMBOL I=RLCLI90;

PROC GPLOT DATA=students;
TITLE 'Teaching Efficiency Regression';
PLOT MSAT*TEFF;
RUN;
QUIT;

ODS PDF CLOSE;
ODS LATEX CLOSE;
