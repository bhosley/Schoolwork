         BR      main        
;
;******* main ()
finish:   .EQUATE 0           ;local variable #2d
main:    SUBSP   2,i         ;allocate #finish
         STRO    msgIn,d     ;cout << "Enter your score: 1, 2, 3, 4, or 5"
         CHARO   '\n',i      ;cout << endl
         DECI    finish,s     ;cin >> Guess
         LDX     finish,s     ;switch (Guess)
         SUBX    1,i         ;subtract 1
         ASLX                ;addresses occupy two bytes
         BR      finishJT,x   
finishJT:.ADDRSS case0       
         .ADDRSS case1       
         .ADDRSS case2       
         .ADDRSS case3
         .ADDRSS case4       
case0:   STRO    msg0,d      ;cout << "You're the first!"
         BR      endCase     ;break
case1:   STRO    msg1,d      ;cout << "You're the first loser!"
         BR      endCase     ;break
case2:   STRO    msg2,d      ;cout << "Try Harder!"
         BR      endCase     ;break
case3:   STRO    msg2,d      ;cout << "Try Harder!"
         BR      endCase     ;break
case4:   STRO    msg3,d      ;cout << "You weren't even Competing!"
endCase: CHARO   '\n',i      ;count << endl
         ADDSP   2,i         ;deallocate #finish
         STOP                
msgIn:   .ASCII  "Enter your score: 1, 2, 3, 4, or 5 \x00"
msg0:    .ASCII  "You're the first! \x00"
msg1:    .ASCII  "You're the first loser! \x00" 
msg2:    .ASCII  "Try Harder! \x00"
msg3:    .ASCII  "You weren't even Competing! \x00"
         .END                  
