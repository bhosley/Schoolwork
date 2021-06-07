LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW5';

PROC IMPORT DATAFILE = '\\uisnutvdiprof1\redirected$\bhosl2\Documents\HW5.xlsx'
	DBMS = excel
	OUT = crop
	REPLACE;
GETNAMES=YES;
MIXED=NO;
SCANTEXT=YES;
USEDATE=YES;
SCANTIME=YES;
RUN;

PROC TRANSPOSE DATA=crop PREFIX=Yield 
	OUT=crops( RENAME=(Yield1=Yield _NAME_=Field) DROP=_LABEL_ );
BY Trta Trtb Trtc;
LABEL 
	Trta = "Nitrogen"
	Trtb = "Water"
	Trtc = "Location"
	Field = "Field";
RUN;

PROC COPY inlib=work outlib=lib;
SELECT crops;
RUN;
