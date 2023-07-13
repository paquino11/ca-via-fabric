import subprocess
import os

os.chdir("fabric-samples/test-network/")

subprocess.call("./network.sh down -c dtnetwork", shell=True)

subprocess.call("./network.sh up -ca", shell=True)

#subprocess.call("./network.sh deployCC -c dtnetwork -ccn chaincode1 -ccp ../../chaincode1 -ccl go", shell=True)





