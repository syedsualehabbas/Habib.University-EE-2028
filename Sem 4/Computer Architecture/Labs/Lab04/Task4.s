.text
.globl main

main:
    li x1, 7       # nth term
    li x4, 1       # series starts with 1
    li x3, 3       # common ratio

loop:
    beq x1, x0, end      # if n == 0, exit loop

    addi sp, sp, -4      
    sw x4, 0(sp)         
    mul x4, x4, x3       # x4 = x4 * x3
    addi x1, x1, -1
    j loop

end:
    j end
# prints (n-1) terms of the geometric series
