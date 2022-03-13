         BR      main        
;
;******* twoVect
v:      .EQUATE  6           ;local variable #2d4a
n:      .EQUATE  2           ;local variable #2d
k:      .EQUATE  0           ;local variable #2d
twoVect: SUBSP   2,i         ;allocate #k 
         LDX     0,i         ;for(k = 0, 
         STX     k,s         ;|
for0:    CPX     4,i         ; k < n,
         BRGE    endFor0     ; |

         ASLX                ; an integer is two bytes 
         LDA     v,sxf       ; k[v]
         ASLA                ; * 2
         STA     v,sxf       ; => k[v] 

         LDX     k,s         ; k++) 
         ADDX    1,i         ; |
         STX     k,s         ; |
         BR      for0        ; End For0
endFor0: RET2                ;deallocate #k 
;
;******* main ()
vector:  .EQUATE 2           ;local variable #2d4a
j:       .EQUATE 0           ;local variable #2d
main:    SUBSP   10,i        ;allocate #vector #j
         LDX     0,i         ;for (j = 0
         STX     j,s         
for1:    CPX     4,i         ;   j < 4
         BRGE    endFor1     
         ASLX                ;   an integer is two bytes
         DECI    vector,sx   ;   cin >> vector[j]
         LDX     j,s         ;   j++)
         ADDX    1,i         
         STX     j,s         
         BR      for1        
endFor1: BR      tvCall       
;******* Call: twoVect 
;
vaddr:   .EQUATE 2           ; local variable #2d
tvCall:  MOVSPA              ;push address of vector 
         ADDA    vector,i
         STA    -2,s 
         MOVSPA              ;push address of n
         ADDA    4,i 
         STA     -4,s 
         SUBSP   4,i         ; allocate #vaddr #n 
         CALL    twoVect,i   ;Call twoVect
         ADDSP   4,i         ; deallocate #n #vaddr 
;
;;; Print Loop
         LDX     0,i         ;for (j = 0
         STX     j,s  
for2:    CPX     4,i         ;   j > 4
         BRGE    endFor2     
         DECO    j,s         ;   cout << j
         CHARO   ' ',i       ;      << ' '
         ASLX                ;   an integer is two bytes
         DECO    vector,sx   ;      << vector[j]
         CHARO   '\n',i      ;      << endl
         LDX     j,s         ;   j--)
         ADDX    1,i         
         STX     j,s         
         BR      for2        
endFor2: ADDSP   10,i        ;deallocate #j #vector
         STOP                
         .END                  
