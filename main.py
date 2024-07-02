import os

#def hideSpotlight():
#    os.system("sudo chmod 600 /System/Library/CoreServices/Search.bundle/Contents/MacOS/Search; killall SystemUIServer")

def hiddenAppTransparency():
    os.system("defaults write com.apple.dock showhidden -bool TRUE; killall Dock")

def addSmallSpacer():
    os.system('defaults write com.apple.dock persistent-apps -array-add "{"tile-type"="small-spacer-tile";}"; killall Dock')

def addLargeSpacer():
    os.system('defaults write com.apple.dock persistent-apps -array-add "{"tile-type"="spacer-tile";}"; killall Dock')

def fullPathTitleBar():
    os.system(" defaults write com.apple.finder _FXShowPosixPathInTitle -bool TRUE")

prompt = input("Mac Tweaker!\n1. Transparency for hidden apps in dock\n2. Add small spacer to dock\n3. Add large spacer to dock\n4. Full path in finder title bar\n5. Exit\n: ")

#if prompt == "1":
    #hideSpotlight()
if prompt == "1":
    hiddenAppTransparency()
elif prompt == "2":
    addSmallSpacer()
elif prompt == "3":
    addLargeSpacer()
elif prompt == "4":
    fullPathTitleBar()
