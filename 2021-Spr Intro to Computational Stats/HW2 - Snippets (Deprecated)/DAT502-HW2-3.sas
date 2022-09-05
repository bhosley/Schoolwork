LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

SYMBOL I=RLCLI90;

PROC GPLOT DATA=students;
TITLE 'Teaching Efficiency Regression';
PLOT MSAT*TEFF;
RUN;
QUIT;
