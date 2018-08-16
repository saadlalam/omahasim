# omahasim
Simulating google omaha server

-----------------------------
I- Installation : 
-Recommanded to use Annaconda

II- How to :

-There are 3 separated .py files that should be run independently.
-On the /server :
    -NewFeatures.py : To be launched first. It simulates a dev environment. Each run, writes on the updates.json file.
    -patcherpy : This to be started next. It simulates the updates server. Basically, it serves hashes.
     Each hash is different, because each time you request from the server, this server hashes (MD5) the previous updates.json file,
     and send it as a response to the client.
-On the /client :
     -niceApp.py : This is supposed to be your software update system. On each run, it requests the server for any new updates.
     The server sends a hash, now the software update system reads a hash on the update.json file, which represents the state after the first installation. If the 2 hashes are equal, there is no update. If they are different, the software update system writes the new hash to its local json file.
     
------
Note : Update systems are more complicated than this, but this is just my version of google omaha server. Hashing is a way to define new content..
-------

EOF
