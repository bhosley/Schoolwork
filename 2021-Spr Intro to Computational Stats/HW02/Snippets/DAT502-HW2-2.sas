LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
DATA students;
	set lib.students;
RUN;

ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW2\SAS Output HW2-2.pdf";
ODS LATEX path="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW2" file="SAS Output HW2-2.tex";

OPTIONS LINESIZE=125;

PROC CHART DATA=students;
TITLE 'Descriptive Graphs of Student Data';
VBAR MJ / GROUP=SEX;
PIE FG / TYPE=PCT;
HBAR FEXAM / MIDPOINTS=45 TO 95 BY 5;
BLOCK MJ / GROUP=SEX TYPE=MEAN SUMVAR=IQ;
STAR FG;
RUN;

ODS PDF CLOSE;
ODS LATEX CLOSE;
