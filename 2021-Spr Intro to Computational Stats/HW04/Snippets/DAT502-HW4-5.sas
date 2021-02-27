LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW4\SAS Output HW4-5.pdf";

DATA students;
	SET lib.students;

PROC SORT DATA = students;
	BY mj;

PROC MEANS DATA=students NOPRINT;
	VAR pexam fexam;
	CLASS mj;
	OUTPUT OUT=results QRANGE(pexam)=Pilot_IQR QRANGE(fexam)=Final_IQR;

PROC PRINT DATA=results;
RUN;
ODS PDF CLOSE;
