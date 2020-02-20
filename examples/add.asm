.code
lda #30h

main_loop:
add #0ffh
sta end1
lda end2
add #01h
sta end2
lda end1
jz fim
jmp main_loop

fim: hlt

.endcode


.data
end1: db #00h
end2: db #00h
.enddata