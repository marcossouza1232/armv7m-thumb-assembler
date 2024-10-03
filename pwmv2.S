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

// rcc

movw r0, 0x1000
movt r0, 0x4002

movw r1, 0x0a04
str r1, [r0, 0x18]

// gpioa

movw r0, 0x0800
movt r0, 0x4001

movw r1, 0x4449
movt r1, 0x4444
str r1, [r0, 0x4]

movw r1, 0x4400
movt r1, 0x4444
str r1, [r0, 0x0]

// adc1

movw r0, 0x2400
movt r0, 0x4001

movw r1, 0x0001
str r1, [r0, 0x08]

movw r2, 0xFFFF
movw r3, 0x0000

espera1:
sub r2, 0x1
cmp r2, r3
bne espera1

// tim1

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

movw r1, 0xFFFF
str r1, [r0, 0x34]

movw r1, 0x8000
str r1, [r0, 0x44]

movw r1, 0x0081
str r1, [r0, 0x0]

movw r1, 0x0010
str r1, [r0, 0x30]

leitura: 

movw r0, 0x2400
movt r0, 0x4001

movw r2, 0x0000
str r2, [r0, 0x34]

movw r1, 0x0001
str r1, [r0, 0x08]

movw r1, 0x0001
str r1, [r0, 0x08]


leu:
ldr r1, [r0, 0x00]
movw r2, 0x0002
and r1, r1, r2
cmp r1, r2
bne leu

ldr r1, [r0, 0x4c]
movw r2, 0xffff
and r1, r1, r2

movw r0, 0x2c00
movt r0, 0x4001

str r1, [r0, 0x2c]

movw r0, 0x2400
movt r0, 0x4001

movw r2, 0x0001
str r2, [r0, 0x34]

movw r1, 0x0001
str r1, [r0, 0x08]

movw r1, 0x0001
str r1, [r0, 0x08]


leu2:
ldr r1, [r0, 0x00]
movw r2, 0x0002
and r1, r1, r2
cmp r1, r2
bne leu2

ldr r1, [r0, 0x4c]
movw r2, 0xffff
and r1, r1, r2

movw r0, 0x2c00
movt r0, 0x4001

str r1, [r0, 0x34]

b leitura
