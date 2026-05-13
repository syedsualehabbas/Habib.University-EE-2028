.text
.globl

main:
    li x4, 5 # x2=n
    li t0, 1
    li x1, 1
loop:
    ble x4, x1, end
    mul t0, t0, x4  # res = res * n
    addi x4, x4, -1 # n=n-1
    j loop
end:
    li x10, 1
    add x11, t0, x0
    ecall 
