#!/bin/bash

names=("Mint-Yz-Aqua" "Mint-Yz-Blue" "Mint-Yz-BlueDeep" "Mint-Yz-Grey" "Mint-Yz-MintContrast" "Mint-Yz-Orange" "Mint-Yz-Pink" "Mint-Yz-Purple" "Mint-Yz-PurpleDeep" "Mint-Yz-Red" "Mint-Yz-Yellow")
maindir=$PWD

# Make directories and index.theme for all colors-light (except Mint-Yz-Mint)
for name in "${names[@]}"; do
    mkdir -p "usr/share/icons/$name"
    cp -f index.theme "usr/share/icons/$name/"
    cd "usr/share/icons/$name"
    sed -i "s/Name=/Name=$name/" index.theme
    cd "$maindir"
done

# Make directories and index.theme for all colors-dark (except Mint-Yz-Mint-Dark)
# Add symbolic link to Mint-Yz-COLOR/places/ (light variant)
for name in "${names[@]}"; do
    mkdir -p "usr/share/icons/$name-Dark"
    cp -f index.theme "usr/share/icons/$name-Dark/"
    cd "usr/share/icons/$name-Dark"
    sed -i "s/Name=/Name=$name-Dark/" index.theme
    sed -i "s/Inherits=Mint-Yz-Mint/Inherits=Mint-Yz-Mint-Dark/" index.theme
    ln -sf "../$name/places"
    cd "$maindir"
done
