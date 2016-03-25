
%include        'constants.asm'
%include        'printing.asm'

section .data
    input   equ 4000000
    e1      dd  2
    e2      dd  2

section .text
    global _start

_start:

    mov ebx, 8
    mov ecx, 2
.loop:
    cmp ebx, input
    jge .end
    add ecx, ebx
    mov edx, dword [e2]
    mov dword [e1], edx
    mov dword [e2], ebx
    mov eax, 3
    mul dword [e2]
    add eax, dword [e1]
    add eax, ebx
    mov ebx, eax
    jmp .loop
    
.end:
    mov eax, ecx
    call iprintln
    call quit
