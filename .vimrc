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
