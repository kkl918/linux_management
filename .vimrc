set nu
set ai
set tabstop=4
set shiftwidth=4

inoremap ( ()<Esc>i
inoremap " ""<Esc>i
inoremap ' ''<Esc>i
inoremap [ []<Esc>i
inoremap { {}<Esc>i
filetype indent on

map <f5> :w<cr>:!python3 %<cr>
map <f12> :q

autocmd BufReadPost *.c nmap <F6> :call Gcc()
fu Gcc()
exec ":w"
exec "silent !gcc -o " . expand("%:t:r") . " %"
exec "!./" . expand("%:t:r")
endf
