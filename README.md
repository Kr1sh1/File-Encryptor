# File Encryptor
 Encrypt (and decrypt) multiple files (and directories) at once

Uses AES 256 bit encryption with a secure random 32 bit salt.

Usage:

python encrypt.py password file1 [file2] [file3] [dir1] [dir2] ...

Performace:
On an i5 6600K @ 4.1GHz - encryption takes place at roughly 5.5GB/minute

Upcoming features:
Multiprocessing
