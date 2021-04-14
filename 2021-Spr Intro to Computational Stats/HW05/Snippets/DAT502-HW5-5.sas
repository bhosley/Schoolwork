LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW5';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW5\SAS Output HW5-5.pdf";

DATA crops;
	set lib.crops;
RUN;

PROC ANOVA DATA=crops;
TITLE "Q5: Water Duncan test Alpha=0.1";
CLASS Trta Trtb Trtc;
MODEL Yield = Trta Trtb Trtc Trta*Trtb Trta*Trtc Trtb*Trtc Trta*Trtb*Trtc;
MEANS Trtb / DUNCAN ALPHA=0.1;
RUN;

ODS PDF CLOSE;
