.text
.globl

main:
addi x10, x0, 12
addi x11, x0, 12
jal x1, sum
add x11, x10, x0
li x10, 1
ecall
j exit
sum:
add x10, x11, x10
jalr x0, 0(x1)

exit: