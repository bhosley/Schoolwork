LIBNAME lib '\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW5';
ODS PDF FILE="\\uisnutvdiprof1\redirected$\bhosl2\Documents\DAT502-HW5\SAS Output HW5-4.pdf";

DATA crops;
	set lib.crops;
RUN;

PROC ANOVA DATA=crops;
TITLE "Q4: Nitrogen Sheffe Test Alpha=0.01";
CLASS Trta Trtb Trtc;
MODEL Yield = Trta Trtb Trtc Trta*Trtb Trta*Trtc Trtb*Trtc Trta*Trtb*Trtc;
MEANS Trta / SCHEFFE ALPHA=0.01;
RUN;

ODS PDF CLOSE;
