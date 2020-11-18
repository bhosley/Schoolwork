         br      main 
;
;*****   uppercase(char ch)
upcase:  LDBYTEA ch,d        ;if (
         CPA     'a',i       ;ch >= 'a'
         BRLT    endUpper
         LDBYTEA ch,d   
         CPA     'z',i       ;ch <= 'z'
         BRGT    endUpper    ; )
         LDBYTEA ch,d
         SUBA    32,i        ; ch = ch - 'a' + 'A'
         STBYTEA ch,d 
endUpper:RET0
;
;*****   increment(char ch)
incr:    LDBYTEA ch,d        ;if(
         CPA     'Z',i       ; ch == 'Z' 
         BREQ    else
         LDBYTEA ch,d
         CPA     'z',i       ; ch == 'z'
         BREQ    else
         ADDA    1,i         ;++ch
         STBYTEA     ch,d
         br      endIncr
else:    LDBYTEA 'A',i       ; ch = 'A'
         STBYTEA ch,d
endIncr: RET0
;
;*****   main()
ch:     .EQUATE 0           ;local variable #1c
main:    SUBSP   1,i         ;allocate #ch
         STRO    msg,d       ;cout << "Please input your character:"
         CHARO   '\n',i      ;cout << endl 
         CHARI   ch,d        ;cin >> ch 
         CALL    upcase,i    ;upcase(ch)
         CALL    incr,i      ;increment(ch)
         CHARO   ch,d        ;cout << ch
;
         ADDSP   1,i         ;deallocate #ch 
         STOP
;*****   Constants
msg:     .ASCII  "Please input your character: \x00"
         .END