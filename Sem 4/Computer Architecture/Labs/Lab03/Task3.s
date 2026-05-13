.text
.globl main

main:
    li t0, 0x200      # base address
    li x25, 5         # number of elements = 5
    li x22, 0         # i = 0
    j loop1

loop1:
    bge x22, x25, swap
    slli x10, x22, 2  # offset = i * 4
    add t1, t0, x10
    addi x11, x22, 1 # value = i + 1 (1 to 5)
    sw x11, 0(t1)
    addi x22, x22, 1
    j loop1
swap:
    li x14, 0          # k = 0 
    slli x16, x14, 2   
    add x17, t0, x16  
    addi x18, x17, 4   
    lw x19, 0(x17)     
    lw x20, 0(x18)    

    sw x20, 0(x17)     # A[k] = A[k+1]
    sw x19, 0(x18)     
end:
    j end
