# Installation (Ubuntu)

1. Download Android Studio + SDK

https://developer.android.com/studio/index.html

2. unzip and move to /opt or /usr/local/
3. open android-studio/bin and run studio.sh to install
4. it should install to ~/Android, otherwise open up preferences in the studio, got to SDK and look it up
5. echo to, or open up .profile or .bashrc (???) and add

export ANDROID_HOME=~/Android/Sdk
export PATH=${PATH} ~/Android/Sdk/tools/bin
export PATH=${PATH} ~/Android/Sdk/platform-tools

6. npm install -g nativescript
7. check that tns and sdkmanager work
8. Install a virtual android machine by opening studio > help > find action and type AVD Manager and then create a new device.
  or... you could possibly run android avd in command line
9. Now open SDK Manager in Studio and check Android Emulator
You need some (???) the following utilities:

  sudo apt-get install lib32z1 lib32ncurses5 lib32stdc++6

  sudo apt-get install lib64stdc++6:i386 
  sudo apt-get install mesa-utils 
  cd YOURPATH/Android/Sdk/emulator/lib64 
  mv libstdc++/ libstdc++.bak 
  ln -s /usr/lib64/libstdc++.so.6  libstdc++  

  sudo apt-get install lib64stdc++6:i386    
  sudo apt-get install mesa-utils

10. navigate to ~/Android/Sdk/emulator/lib64
11. rename and then softlink:

  mv libstdc++/ libstdc++.bak
  ln -s /usr/lib64/libstdc++.so.6 libstdc++

