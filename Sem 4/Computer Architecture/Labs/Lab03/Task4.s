.data
src: .asciiz "Hello World"
dst: .space 10

.text
.globl main

main:
    la t0, src     
    la t1, dst  
    j copy    

copy:
    lb t2, 0(t0)  
    li t3, 32 
    beq t3,t2, end  #stop at the ascii value of empty space
    sb t2, 0(t1)    
    beq t2, zero, end   # stop at '\0'
    addi t0, t0, 1  
    addi t1, t1, 1  
    j copy
end:
    j end
