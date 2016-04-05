

slen: ; finds length of string in eax
    push rbx
    mov rbx, rax

.nextchar:
    cmp byte [rax], 0
    jz .finished
    inc rax
    jmp .nextchar

.finished:
    sub rax, rbx
    pop rbx
    ret


sprint: ; prints string in eax
    push rdx
    push rcx
    push rbx
    push rax
    
    call slen
    
    mov rdx, rax
    pop rax
    
    mov rsi, rax
    mov rdi, STDOUT
    mov rax, SYS_WRITE
    syscall
    
    pop rbx
    pop rcx
    pop rdx
    ret


quit:
    mov	rax, SYS_EXIT
	mov	rdi, 0
	syscall
	ret


