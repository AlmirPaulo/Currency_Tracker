" SERVER VERSION
" SETS
set termguicolors
set noshowmode
set hidden
set wildmenu
set number
set relativenumber
filetype plugin on 
set omnifunc=syntaxcomplete#Complete

" PLUGINS
call plug#begin('~/.vim/plugged')

Plug 'davidhalter/jedi-vim'
Plug 'Yggdroot/indentLine'
Plug 'sheerun/vim-polyglot'
"Plug 'mattn/emmet-vim'
Plug 'vim-airline/vim-airline'
Plug 'jiangmiao/auto-pairs'
Plug 'preservim/nerdtree'
Plug 'ghifarit53/daycula-vim' , {'branch' : 'main'}

call plug#end()

" SNIPETS & REMAPS 
let mapleader = "\<SPACE>"
inoremap ii  <ESC>:w <CR>
vnoremap ii  <ESC>:w <CR>
noremap j jzz
nnoremap k kzz
nnoremap <leader> <C-w>
noremap <leader>ss :%s///gc
noremap <leader>q :q!<CR>
noremap <leader>t :! firefox --private-window 
noremap <leader>c :HexokinaseToggle<CR>
noremap <leader>cc :HexokinaseRefresh<CR>
noremap <leader>f :NERDTreeToggle<CR>
nnoremap <leader><TAB> :below terminal<CR>
noremap <Up> <NOP>
noremap <Down>  <NOP>
noremap <Left>  <NOP>
noremap <Right>  <NOP>

let g:jedi#popup_on_dot= 0

let g:daycula_enable_italic = 1
let g:daycula_transparent_background= 1
colorscheme daycula

"let g:user_emmet_leader_key=','

