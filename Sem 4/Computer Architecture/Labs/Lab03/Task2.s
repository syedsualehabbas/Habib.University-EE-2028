.text
.globl
main:
li x10, 10 #g
li x11, 6 #h
li x12, 4 #i
li x13, 9 #j
jal x1, stack
jal x2, load
j end

stack: 
    addi sp, sp, -8
    sw x5, 4(sp)
    sw x4, 0(sp)
    add x5, x10, x11
    add x4, x12, x13
    sub x20, x5, x4 #f
    lw x4, 0(sp)
    lw x5, 4(sp)
    addi sp, sp, 8
    jalr x0, 0(x1)

load:
    li x10,1
    add x11, x20, x0
    ecall
    jalr x0, 0(x2)
end:
    j end





