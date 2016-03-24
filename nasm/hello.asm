;Copyright (c) 1999 Konstantin Boldyshev <konst@linuxassembly.org>
;
;"hello, world" in assembly language for Linux
;
;to compile:
;
;nasm -f elf hello.asm
;ld -s -o hello hello.o

section	.text
    global _start       ;must be declared for linker (ld)

_start:         ;tell linker entry point

	mov	eax,4   ;system call number (sys_write)
	mov	ebx,1   ;file descriptor (stdout)
	mov	ecx,msg ;message to write
	mov	edx,len ;message length
	int	0x80    ;call kernel

	mov	eax,1   ;system call number (sys_exit)
	mov	ebx,0   ; Have an exit code of 0
	int	0x80    ;call kernel

section	.data
    msg	db	'Hello, world!',0xa ;our dear string
    len	equ	$-msg               ;length of our dear string
