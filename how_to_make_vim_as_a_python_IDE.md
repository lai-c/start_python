How to make your vim as a Python IDE
================
###1.install

    $ hg clone https://vim.googlecode.com/hg/ vim
    $ cd vim/src
    $ ./configure --enable-pythoninterp --with-features=huge --prefix=$HOME/opt/vim
    $ make && make install
    $ mkdir -p $HOME/bin
    $ cd $HOME/bin
    $ ln -s $HOME/opt/vim/bin/vim
    $ which vim
    $ vim --version

###2.configuration vimrc
add the following to your vimrc
you may save your vimrc in Github

    "Rebind <Leader> key
    let mapleader = ","
    
    "map sort function to a key
    vnoremap <Leader> :sort<CR>
    
    
    "for easier moving code block
    vnoremap < <gv
    vnoremap > >gv

###3.Python IDE set up

