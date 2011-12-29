"""
  Author: Justin Cappos
  Module: File system constants for Lind.   This is things like the mode bits
          and macros.

  Start Date: December 17th, 2011

"""
  

# Mostly used with access()
F_OK = 0
X_OK = 1
W_OK = 2
R_OK = 4



O_RDONLY=00
O_WRONLY=01
O_RDWR=02
O_CREAT=0100
O_EXCL=0200
O_NOCTTY=0400
O_TRUNC=01000
O_APPEND=02000
O_NONBLOCK=04000
# O_NDELAY=O_NONBLOCK
O_SYNC=010000
# O_FSYNC=O_SYNC
O_ASYNC=020000

S_IRWXA=00777
S_IRWXU=00700
S_IRUSR=00400
S_IWUSR=00200
S_IXUSR=00100
S_IRWXG=00070
S_IRGRP=00040
S_IWGRP=00020
S_IXGRP=00010
S_IRWXO=00007
S_IROTH=00004
S_IWOTH=00002
S_IXOTH=00001


# file types for open / stat, etc.
S_IFBLK=24576
S_IFCHR=8192
S_IFDIR=16384
S_IFIFO=4096
S_IFLNK=40960
S_IFREG=32768
S_IFSOCK=49152

S_IWRITE=128
S_ISUID=2048
S_IREAD=256
S_ENFMT=1024
S_ISGID=1024

SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2

F_DUPFD = 0
F_GETFD = 1
F_SETFD = 2
F_GETFL = 3
F_SETFL = 4
F_GETLK = 5
F_GETLK64 = 5
F_SETLK = 6
F_SETLK64 = 6
F_SETLKW = 7
F_SETLKW64 = 7
F_SETOWN = 8
F_GETOWN = 9
F_SETSIG = 10
F_GETSIG = 11
F_SETLEASE = 1024
F_GETLEASE = 1025
F_NOTIFY = 1026

# for the lock calls
F_RDLCK = 0
F_WRLCK = 1
F_UNLCK = 2
F_EXLCK = 4
F_SHLCK = 8



# some MACRO helpers...
def IS_DIR(mode):
  if mode & S_IFDIR:
    return True
  else:
    return False
