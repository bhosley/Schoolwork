LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW5';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW5\SAS Output HW5-8.pdf";

DATA crops;
	set lib.crops;
RUN;

PROC ANOVA DATA=crops;
TITLE "Q8: Nitrogen Dunnett test with a0 control Alpha=0.025";
CLASS Trta Trtb Trtc;
MODEL Yield = Trta Trtb Trtc Trta*Trtb Trta*Trtc Trtb*Trtc Trta*Trtb*Trtc;
MEANS Trta / DUNNETT('a0') ALPHA=0.025;
RUN;

ODS PDF CLOSE;
