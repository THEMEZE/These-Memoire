#!/bin/bash

echo "🔄 Arrêt de VS Code..."
killall "Visual Studio Code" 2>/dev/null

echo "🧹 Nettoyage du cache LTEX..."
rm -rf ~/Library/Application\ Support/Code/User/globalStorage/valentjn.vscode-ltex/*

echo "🚀 Relance de VS Code..."
open -a "Visual Studio Code"

echo "✅ LTEX rafraîchi !"

