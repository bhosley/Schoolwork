BR       main
n1:      .BLOCK  2
n2:      .BLOCK  2
n3:      .BLOCK  2
newline: .ASCII "\n\x00"    
;
main:    DECI    n2,d
         DECI    n3,d
         LDA     n2,d
         CPA     n3,d
         BRLT    L1
         DECI    n1,d
         LDA     n1,d
         CPA     n3,d
         BRLT    L7
         BR      L6
         STA     n3,d
L1:      DECI    n1,d
         LDA     n2,d
         CPA     n1,d
         BRLT    L5
         DECO    n1,d
         STRO   newline,d 
         DECO    n2,d
         STRO   newline,d
L2:      DECO    n3,d
         STRO   newline,d
         STOP
L3:      DECO    n2,d
         STRO   newline,d 
         DECO    n3,d
         CHARO   newline,d
         BR      L9
L4:      DECO    n1,d
         CHARO   newline,d
         DECO    n2,d
         CHARO   newline,d
         STOP
         STA     n1,d
L5:      LDA     n3,d
         CPA     n1,d
         BRLT    L3
         DECO    n2,d
         CHARO   newline,d
         DECO    n1,d
         CHARO   newline,d
         BR      L8
L6:      DECO    n3,d
         CHARO   newline,d
         LDA     n1,d
         CPA     n2,d
         BRLT    L4
         BR      L8
L7:      DECO    n1,d
         CHARO   newline,d
         DECO    n3,d
         CHARO   newline,d
         DECO    n2,d
         CHARO   newline,d
         STOP
L8:      DECO    n2,d
         CHARO   newline,d
L9:      DECO    n1,d
         CHARO   newline,d
         STOP
         .END
