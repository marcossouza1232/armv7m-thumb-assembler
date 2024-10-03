.cpu cortex-m3
.syntax unified

.thumb_func
.global _start
_start:
    stacktop: .word 0x20000000
    .word reset

    
.thumb_func
.global reset
reset: 

movw r0, 0x1000
movt r0, 0x4002

movw r1, 0x0804
str r1, [r0, 0x18]

movw r0, 0x0800
movt r0, 0x4001

movw r1, 0x4449
movt r1, 0x4444
str r1, [r0, 0x4]

movw r0, 0x2c00
movt r0, 0x4001

ldr r1, [r0, 0x0]
bic r1, r1, 0x0001
orr r1, r1, 0x0080
str r1, [r0, 0x0]

movw r1, 0x0001
str r1, [r0, 0x28]

movw r1, 0x0068
str r1, [r0, 0x18]

movw r1, 0x0001
str r1, [r0, 0x20]

movw r1, 0x1234
str r1, [r0, 0x34]

movw r1, 0x8000
str r1, [r0, 0x44]

movw r1, 0x0081
str r1, [r0, 0x0]

movw r1, 0x0005
str r1, [r0, 0x30]

repete:
movw r2, 0x0000
movw r3, 0xFFFF
movw r4, 0x0000

subida:
add r2, 0x1
str r2, [r0, 0x34]
cmp r2, r3
bne subida

descida:
sub r2, 0x1
str r2, [r0, 0x34]
cmp r2, r4
bne descida

b repete


