.text
.globl triangle


li a0, 5
triangle:
    addi sp, sp, -8     
    sw ra, 4(sp)         # save return address
    sw a0, 0(sp)         
    beq a0, x0, base     # base case: if n == 0

    addi a0, a0, -1      # n = n - 1
    jal triangle         # recursive call

    lw t0, 0(sp)         # restore n
    add a0, a0, t0     
    j done

base:
    li a0, 0             # base case result

done:
    lw ra, 4(sp)       
    addi sp, sp, 8      
    jr ra
    j end
end:
    j end
