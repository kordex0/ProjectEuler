
all: problem001 testing

%: %.asm
	nasm -f elf $@.asm
	ld -melf_i386 -s -o $@ $@.o

