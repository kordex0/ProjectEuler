

isqrt:
    push ebx
    push ecx
    push edx
    
    mov ebx, 1
    mov ecx, 0
    
.loop:
    sub eax, ebx
    cmp eax, 0
    jl .exit        ; if not a perfect square, take floor of the sqrt
    inc ecx
    je .exit        ; if is a perfect square
    add ebx, 2
    jmp .loop

.exit:
    mov eax, ecx
    
    pop edx
    pop ecx
    pop ebx
    ret


