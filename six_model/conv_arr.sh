#!/bin/bash

array=(0010 0050 0100 0200)

for file_num in ${array[*]}
do 
    echo $file_num
    convert -quality 300 DPanel-xz-$file_num.png Dxz$file_num.eps
    convert -quality 300 McPanel-xz-$file_num.png Mcxz$file_num.eps
done
