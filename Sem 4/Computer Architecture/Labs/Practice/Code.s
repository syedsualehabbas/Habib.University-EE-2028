.globl
.text
main:

    li x4, 0
    li x2, 0

    bge x1, x12, end
    slli x3, x4, 3
    add x14, x3, x1
    ld x7, 0(x14)

    andi x6, x7, 1
    bne x6, x0, odd

even:
    add x20, x13, x7
    add x2, x2, x20
    j next
odd:
    sub x2, x2, x7

next:
    addi x4, x4, 1
    j main

end:
    addi x10, x19, 0
    ret