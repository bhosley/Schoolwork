FILENAME AAA '\\uisnutvdiprof1\redirected$\bhosl2\Documents\PILOT.DAT';
LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW1';

DATA students;
INFILE AAA;
INPUT
	CL $
	MJ $
	SEX $
	IQ
	MSAT
	PEXAM
	FEXAM
	@@;
LABEL
	CL = 'Class'
	MJ = 'Major'
	SEX = 'Gender'
	IQ = 'IQ'
	MSAT = 'SAT Math Score'
	PEXAM = 'Pilot Exam'
	FEXAM = 'Final Exam'
	TEFF = 'Teaching Efficiency'
	FG = 'Final Grade';

TEFF = FEXAM - PEXAM;
SELECT;
	WHEN (90 <= FEXAM & FEXAM <= 100) FG = 'A';
	WHEN (80 <= FEXAM & FEXAM < 90) FG = 'B';
	WHEN (70 <= FEXAM & FEXAM < 80) FG = 'C';
	WHEN (60 <= FEXAM & FEXAM < 70) FG = 'D';
	OTHERWISE FG = 'U';
END;

PROC PRINT;
TITLE 'Pilot Class Data';

PROC COPY inlib=work outlib=lib;
	SELECT students;
RUN;
