#!/bin/bash
# =============
# Color scheme download
# =============
mkdir -p ~/.vim/colors && cd ~/.vim/colors
wget -O wombat256mod.vim http://www.vim.org/scripts/download_script.php?src_id=13400

# =============
# pathogen install
# Now you can install any plugin into a .vim/bundle/plugin-name/ folder
# =============
mkdir -p ~/.vim/autoload ~/.vim/bundle                                        
curl -so ~/.vim/autoload/pathogen.vim https://raw.github.com/tpope/vim-pathogen/HEAD/autoload/pathogen.vim

# =============
# Settings for vim-powerline                                                       
# =============
cd ~/.vim/bundle                                                                 
git clone git://github.com/Lokaltog/vim-powerline.git 
  
# =============
# Settings for ctrlp                                                               
# =============
cd ~/.vim/bundle                                                                 
git clone https://github.com/kien/ctrlp.vim.git 

# =============
# Settings for jedi-vim                                                         
# Note that the python-mode VIM plugin seems to conflict with jedi-vim,         
# therefore you should disable it before enabling jedi-vim                      
# =============
cd ~/.vim/bundle                                                              
git clone git://github.com/davidhalter/jedi-vim.git 
cd jedi-vim
sudo pip install jedi

# =============
# Python folding                                                                
# =============
mkdir -p ~/.vim/ftplugin                                                      
wget -O ~/.vim/ftplugin/python_editing.vim http://www.vim.org/scripts/download_script.php?src_id=5492


# =============
# pyflakes-vim
# check python syntax error 
# =============
cd ~/.vim/bundle
git clone https://github.com/kevinw/pyflakes-vim.git
cd pyflakes-vim
git submodule init
git submodule update

# =============
# vim-flake8
# check python syntax error 
# =============
cd ~/.vim/bundle
git clone https://github.com/nvie/vim-flake8.git
sudo pip install flake8

# =============
# indent guides
# =============
cd ~/.vim/bundle
git clone git://github.com/nathanaelkane/vim-indent-guides.git

