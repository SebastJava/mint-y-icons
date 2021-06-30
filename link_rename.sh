#! /bin/bash
# from: https://superuser.com/questions/157743/batch-update-symbolic-links-recursively
# author: https://superuser.com/users/940119/akhil-mohan
#
# This can be executed as link_rename.sh /home/human/dir link1 link2
# The script has 3 arguments:
#    The directory in which you want to perform the batch rename of symlinks
#    The old pattern. Here link1 is the old pattern which will be replaced
#    The new pattern. Here link2 is the new pattern with which link1 will be replaced

DIR=$1
OLD_PATTERN=$2
NEW_PATTERN=$3

while read -r line
do
    echo $line
    CUR_LINK_PATH="$(readlink "$line")"
    NEW_LINK_PATH="$CUR_LINK_PATH"  
    NEW_LINK_PATH="${NEW_LINK_PATH/"$OLD_PATTERN"/"$NEW_PATTERN"}"
    rm "$line"
    ln -s "$NEW_LINK_PATH" "$line"
done <<< $(find "$DIR" -type l)
