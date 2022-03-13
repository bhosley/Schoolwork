         BR      main
; 
;******* main()
vector:  .EQUATE 2           ;local variable #2d4a
j:       .EQUATE 0           ;local vairable #2d
main:    SUBSP   10,i       ;allocate #vector #3 ;WARNING: Number of bytes allocated (10) not equal to number of bytes listed in trace tag (8).
         LDX     0,i         ;for(j - 0) 
         STX     j,s         
for1:    CPX     4,i         ; j < 4
         BRGE    endFor1
         ASLX                ; an integer is two bytes
         DECI    vector,sx   ;cin >> vector[j]
         LDX     j,s         ; j++)
         ADDX    1,i
         STX     j,s
         BR      for1
endFor1: LDX     3,i         ;for(j - 3
         STX     j,s
for2:    CPX     0,i         ; j >= 0
         BRLT    endFor2
         DECO    j,s         ;cout << j
         CHARO   ' ',i       ; << ' '
         ASLX                ; an integer has two bytes
         DECO    vector,sx   ;    << vector[j]
         CHARO   '\n',i      ;    << endl
         LDX     j,s         ; j--)
         SUBX    1,i
         STX     j,s
         BR      for2
endFor2: ADDSP   10,i        ;deallocate #j #vector
         STOP
         .END