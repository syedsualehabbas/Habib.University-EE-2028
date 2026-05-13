.data
arr: .word 9, 7, 4, 2, 1

.text
.globl main

main:
    la a0, arr
    li a1, 5
    
    li t0, 0

outerloop:
    bge t0, a1, done
    
    li t1, 0

innerloop:
    addi t2, a1, -1
    sub t2, t2, t0
    bge t1, t2, next_i
    
    slli t3, t1, 2
    add t4, a0, t3
    lw t5, 0(t4)
    
    addi t6, t4, 4
    lw x6, 0(t6)
    
    bge t5, x6, no_swap
    sw x6, 0(t4)
    sw t5, 0(t6)

no_swap:
    addi t1, t1, 1
    j innerloop

next_i:
    addi t0, t0, 1
    j outerloop

done:
    li a7, 10
    ecall