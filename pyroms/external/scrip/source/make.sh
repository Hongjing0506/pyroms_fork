#!/usr/bin/bash

export PREFIX=/home/chenhj23/anaconda3/envs/roms
make DEVELOP=1 PREFIX=$PREFIX install
mv -vf scrip*.so ../../../pyroms


# if uninstall
#make DEVELOP=1 uninstall
