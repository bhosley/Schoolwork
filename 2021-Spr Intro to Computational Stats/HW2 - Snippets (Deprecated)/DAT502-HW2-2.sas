LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

OPTIONS LINESIZE=125;

PROC CHART DATA=students;
TITLE 'Descriptive Graphs of Student Data';
VBAR MJ / GROUP=SEX;
PIE FG / TYPE=PCT;
HBAR FEXAM / MIDPOINTS=45 TO 95 BY 5;
BLOCK MJ / GROUP=SEX TYPE=MEAN SUMVAR=IQ;
STAR FG;
RUN;
