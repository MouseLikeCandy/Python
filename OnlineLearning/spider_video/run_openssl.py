import os
cmd = "openssl aes-128-cbc -d -in ./ts002/2.ts -out ./ts002/解密文件2.ts -iv 00000000000000000000000000000000 -K  37613432633731363239396236663036"
os.system(cmd)