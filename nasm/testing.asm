
%include        'constants.asm'
%include        'printing.asm'
%include        'math.asm'

section .text
    global _start

_start:

    mov eax, 2500
    call iprintln
    call isqrt
    call iprintln
    
    call quit

