         BR      main
;******* twoVect
v:       .EQUATE 6
n:       .EQUATE 2
k:       .EQUATE 0
twoVect: SUBSP   2,i         ;allocate k ;WARNING: Number of bytes allocated (2) not equal to number of bytes listed in trace tag (0).
         LDX     0,i         ;for(k = 0, 
         STX     k,s         ;|
for0:    CPX     n,i         ; k < n,
         BRGE    endFor0     ;|
         ASLX                ; an integer is two bytes
         LDA     v,sxf       ; k[v]
         ASLA                ; * 2
         STA     v,sxf       ; => k[v] 
         LDX     k,s         ; k++)
         ADDX    1,i         ;|
         STX     k,s         ;|
         BR      for0        ; End For0
endFor0: RET2 ;WARNING: Number of bytes deallocated (2) not equal to number of bytes listed in trace tag (0).
;******* main()
vector:  .EQUATE 2           ;local variable #2d4a
j:       .EQUATE 0           ;local variable #2d
main:    SUBSP   10,i        ;allocate #vector #3 ;WARNING: Number of bytes allocated (10) not equal to number of bytes listed in trace tag (8).
         LDX     0,i         ;for(j = 0, 
         STX     j,s         
for1:    CPX     4,i         ; j < 4,
         BRGE    endFor1
         ASLX                ; an integer is two bytes
         DECI    vector,sx   ;cin >> vector[j]
         LDX     j,s         ; j++)
         ADDX    1,i
         STX     j,s
         BR      for1
endFor1: LDX     0,i         ;for(j = 0
         STX     j,s
;******* Call: twoVect
         ADDSP   4,i         ;push v ;WARNING: Number of bytes deallocated (4) not equal to number of bytes listed in trace tag (0).
         MOVSPA              ;|
         ADDA    vector,i    ;|
         STA     -2,s        ;|
         LDA     n,s         ;push n
         STA     -4,s        ;|
         SUBSP   4,i         ;| ;WARNING: Number of bytes allocated (4) not equal to number of bytes listed in trace tag (0).
         ;CALL    twoVect,i   ;Call twoVect
;;; Print Loop
         LDX     0,i         ;for(j = 0, 
         STX     j,s
for2:    CPX     4,i         ; j < 4
         BRGE    endFor2
         DECO    j,s         ;cout << j
         CHARO   ' ',i       ; << ' '
         ASLX                ; an integer has two bytes
         DECO    vector,sx   ;    << vector[j] 
         CHARO   '\n',i      ;    << endl
         LDX     j,s         ; j++)
         ADDX    1,i
         STX     j,s
         BR      for2
endFor2: ADDSP   10,i        ;deallocate #j #vector
         STOP
         .END