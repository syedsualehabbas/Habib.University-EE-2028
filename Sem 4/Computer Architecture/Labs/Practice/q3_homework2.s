.globl
.text
main:
    li x19, 0(x10)
    li x20, 0
    addi x11, x11, -1
loop:
    bge x20, x11, end
    slli x3, x20, 3
    add x6, x10, x5
    ld x7, 0(x6)
    ld x8, 8(x6)
    bge x7, x8, else
    mv x19, x8
else:
    addi x20, x20, 1
    j loop
end:
    mv x10, x19
    jalr x0, 0(x1)