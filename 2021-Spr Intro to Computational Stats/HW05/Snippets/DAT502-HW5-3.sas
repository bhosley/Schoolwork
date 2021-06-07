LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW5';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW5\SAS Output HW5-3.pdf";

DATA crops;
	set lib.crops;
END;

PROC ANOVA DATA=crops;
TITLE "Q3: ANOVA Alpha=0.05";
CLASS Trta Trtb Trtc;
MODEL Yield = Trta Trtb Trtc Trta*Trtb Trta*Trtc Trtb*Trtc Trta*Trtb*Trtc;
MEANS ALPHA=0.05;
RUN;

ODS PDF CLOSE;
