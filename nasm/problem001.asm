
%include        'constants.asm'
%include        'printing.asm'

section .data
    input   equ 999

section .text
    global _start

_start:

    mov ecx, 0
    
    ; three
    mov eax, input
    mov ebx, 3
    div ebx
    mov ebx, eax
    add ebx, 1
    mul ebx
    mov ebx, 2
    div ebx         ; eax result, edx remainder
    mov ebx, 3
    mul ebx
    add ecx, eax
    
    ; five
    mov eax, input
    mov ebx, 5
    div ebx
    mov ebx, eax
    add ebx, 1
    mul ebx
    mov ebx, 2
    div ebx
    mov ebx, 5
    mul ebx
    add ecx, eax
    
    ; fifteen
    mov eax, input
    mov ebx, 15
    div ebx
    mov ebx, eax
    add ebx, 1
    mul ebx
    mov ebx, 2
    div ebx
    mov ebx, 15
    mul ebx
    sub ecx, eax
    
    mov eax, ecx
    
    call iprintln

	call quit
	

