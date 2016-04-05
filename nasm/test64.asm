
%include        'constants64.asm'
%include        'printing64.asm'

section .text
    global _start

_start:

    mov rax, msg
    call sprint
    
    call quit

section .data
    msg: db 'Hello World',0xa,0x0
  
