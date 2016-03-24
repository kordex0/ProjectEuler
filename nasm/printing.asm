
iprint: ; prints int in eax
    push eax
    push ecx
    push edx
    push esi
    mov ecx, 0

.divideLoop:
    inc ecx
    mov edx, 0
    mov esi, 10
    idiv esi
    add edx, 48
    push edx
    cmp eax, 0
    jnz .divideLoop

.printLoop:
    dec ecx
    mov eax, esp
    call sprint
    pop eax
    cmp ecx, 0
    jnz .printLoop
    
    pop esi
    pop edx
    pop ecx
    pop eax
    ret


iprintln: ; prints int in eax
    call iprint
    
    push eax
    mov eax, 0xa
    push eax
    mov eax, esp
    call sprint
    pop eax
    pop eax
    ret
    

slen: ; finds length of string in eax
    push ebx
    mov ebx, eax

.nextchar:
    cmp byte [eax], 0
    jz .finished
    inc eax
    jmp .nextchar

.finished:
    sub eax, ebx
    pop ebx
    ret


sprint: ; prints string in eax
    push edx
    push ecx
    push ebx
    push eax
    call slen
    
    mov edx, eax
    pop eax
    
    mov ecx, eax
    mov ebx, STDOUT
    mov eax, SYS_WRITE
    int 0x80
    
    pop ebx
    pop ecx
    pop edx
    ret
    

sprintln: ; prints string in eax
    call sprint
    
    push eax
    mov eax, 0xa
    push eax
    mov eax, esp
    call sprint
    pop eax
    pop eax
    ret


quit:
    mov	eax, SYS_EXIT
	mov	ebx, 0
	int	0x80
	ret

    
