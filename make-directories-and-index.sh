#!/bin/bash

names=("Mint-Yz-AquaShine" "Mint-Yz-BlueBelize" "Mint-Yz-BlueElectron" "Mint-Yz-Grey" "Mint-Yz-MintLeaf" "Mint-Yz-MintSoda" "Mint-Yz-OrangeShine" "Mint-Yz-Pink" "Mint-Yz-Purple" "Mint-Yz-RedShine" "Mint-Yz-Yellow")
maindir=$PWD

# Make directories and index.theme for all colors-light (except Mint-Yz-Classic)
for name in "${names[@]}"; do
    mkdir -p "usr/share/icons/$name"
    cp -rf usr/share/icons/Mint-Yz-Classic/places "usr/share/icons/$name/"
    cp -f index.theme "usr/share/icons/$name/"
    cd "usr/share/icons/$name"
    sed -i "s/Name=/Name=$name/" index.theme
    cd "$maindir"
done

# Make directories and index.theme for all colors-dark (except Mint-Yz-Classic-Dark)
# Add symbolic link to Mint-Yz-COLOR/places/ (light variant)
for name in "${names[@]}"; do
    mkdir -p "usr/share/icons/$name-Dark"
    cp -f index.theme "usr/share/icons/$name-Dark/"
    cd "usr/share/icons/$name-Dark"
    sed -i "s/Name=/Name=$name-Dark/" index.theme
    sed -i "s/Inherits=Mint-Yz-Classic,Adwaita,gnome,hicolor/Inherits=Mint-Yz-Classic-Dark,Adwaita,gnome,hicolor/" index.theme
    ln -sf "../$name/places"
    cd "$maindir"
done
