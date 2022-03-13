BR main
numA: .WORD 0
numB: .WORD 0
numC: .WORD 0
numD: .WORD 0
sum: .WORD 0
avg: .WORD 0
labA: .ASCII "input a = \x00"
labB: .ASCII "input b = \x00"
labC: .ASCII "input c = \x00"
labD: .ASCII "input d = \x00"
labSum: .ASCII "sum = \x00"
labAvg: .ASCII "average = \x00"
;set the variables
main: LDA 2,i
STA numA,d ;set a = 2
LDA 4,i
STA numB,d ;set b = 4
LDA 5,i
STA numC,d ;set c = 5
LDA 1,i
STA numD,d ;set d = 1
;calculate results
LDA numA,d ;load a
ADDA numB,d ;add b
ADDA numC,d ;add c
ADDA numD,d ;add d
STA sum,d ;store sum
;calculate simple average
LDA sum,d ;load sum
ASRA ;Arithmetic left(proxy division by 2)
ASRA ;As above
STA avg,d ;store average
;tell the variables
STRO labA,d ;print a label 
DECO numA,d ;Print a
CHARO '\n',i ;newline
STRO labB,d ;print b label 
DECO numB,d ;Print b
CHARO '\n',i ;newline
STRO labC,d ;print c label 
DECO numC,d ;Print c
CHARO '\n',i ;newline
STRO labD,d ;print d label 
DECO numD,d ;Print d
CHARO '\n',i ;newline
STRO labSum,d ;print sum label 
DECO sum,d ;Print sum
CHARO '\n',i ;newline
STRO labAvg,d ;print average label 
DECO avg,d ;Print average
STOP
.END