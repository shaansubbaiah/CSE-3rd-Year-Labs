#include <dirent.h>
#include <unistd.h>
#include <sys/fcntl.h>
#include <sys/resource.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>
#include <setjmp.h>

int main(int argc, char **argv[])
{
    // code
    return 0;
}

// Note: All these flags (for mode, perm, etc) can be combined using OR
// eg. to check if permissions rwx for user and r for group exist:
// ( S_IRWXU | S_IRGRP )

// Access Mode: O_RDONLY, O_WRONLY, O_RDWR
//              O_APPEND, O_CREAT, O_EXCL, O_TRUNC, O_NONBLOCK, O_NOCTTY

// Permissions: Set only if a new file is being created with O_CREAT
//              S_IRWXU, S_IRUSR, S_IWUSR, S_IXUSR
//              S_IRWXG, S_IRGRP, S_IWGRP, S_IXGRP
//              S_IRWXO, S_IROTH, S_IWOTH, S_IXOTH
//              Can use 0777, 0755, etc instead

// // Regular file APIs
int open(const char *path, int accessmode, mode_t perms);
// returns file descryptor; -1 on error

int creat(const char *path, mode_t mode);
// returns file descryptor; -1 on error

size_t read(int fd, void *buf, size_t nbytes);
// returns the no. of bytes; -1 on error

size_t write(int fd, void *buf, size_t nbytes);
// returns the no. of bytes; -1 on error

int close(int fd);
// returns 0; -1 on error

int fcntl(int fd, int cmd, ...);
// helps user to set, query flags on the fd

off_t lseek(int fd, off_t pos, int whence);
// used to change file offset, allow random access of data
// returns new file offset; -1 on error
// Whence: reference location; current, beg of file, end of file
//              SEEK_CUR, SEEK_SET, SEEK_END

int link(const char *cur_link, const char *new_link);
// returns 0; -1 on error

int unlink(const char *cur_link);
// returns 0; -1 on error

int rename(const char *old_path, const char *new_path);
// defined in ANSI C; similar to unlink

int chown(const char *path, uid_t uid, gid_t gid);
int fchown(int fd, uid_t uid, gid_t gid);
int lchown(const char *path, uid_t uid, gid_t gid);
// changes the user id, group id of files

int chmod(const char *path, mode_t flag);
int fchmod(int fd, mode_t flag);
// changes permissions of a file; should be su/owner
// can also set user id, group id to the user running the program, using:
// S_ISUID, S_ISGID flags

int stat(const char *path, struct stat *statv);
int fstat(int fd, struct stat *statv);
int lstat(const char *path, struct stat *statv);
// returns 0; -1 on error
// lets us determine the file type, using macros:
//          S_ISREG(), S_ISDIR(), S_ISCHR(), S_ISFIFO(),
//          S_ISLNK(), S_ISBLK(), S_ISSOCK()

int access(const char *path, int flag);
// checks existence and access permissions
// returns 0; -1 on error
// flags    file exists, read, write, exec perms
//          F_OK, R_OK, W_OK, X_OK

int utime(const char *path, struct utimbuf *time);
// modifies the access and modification timestamps of a file
// returns 0, -1 on error
// if time variable is not provided, current time is taken
// struct utimbuf {
//      time_t actime; time_t modtime; }

// // Directory file APIs
int mkdir(const char *path, mode_t mode);
int rmdir(const char *path);

DIR *opendir(const char *path);
Dirent *readdir(DIR *dir_fd);
int closedir(DIR *dir_fd);
void rewinddir(DIR *dir_fd); // sets pointer to the dir's 1st file

// // Device file APIs
int mknod(const char *path, mode_t mode, int device_id);
// returns 0; -1 on error
// open, read and write using the above directory file APIs
// for major no. 8, minor no. 3, device id = ((15<<8)|3)

// // FIFO file APIs
int mkfifo(const char *path, mode_t mode);
// returns 0; -1 on error
// open, read and write using the above directory file APIs

int pipe(int fd[2]);
// process can read from fd[0], write to fd[1]
// returns 0; -1 on error

// // Unix process functions
void exit(int status);  // performs cleanup, then returns to kernel
void _Exit(int status); // directly returns to the kernel
void _exit(int status); // same as above^

int atexit(void (*func)(void));
// functions to be executed before exiting are registered using atexit()
// upto 32 functions can be registered, and are called in reverse order
// return 0; non-zero on error

extern char **environ; // pointer to environment variables

void *malloc(size_t size);
void *calloc(size_t nobj, size_t size);
void realloc(void *ptr, size_t new_size);
// returns pointer; NULL on error
// alloca() is just like malloc() but mem is from stack frame, not heap
void free(void *ptr);

char *getenv(const char *name);
char *putenv(const char *str); // str = "name=value", replaces old defn.
char *setenv(const char *name, const char *val, int rewrite);
char *unsetenv(const char *name);

int setjmp(jmp_buf env);
// returns 0 if called directly; non-zero if returning from a call to longjmp
void longjmp(jmp_buf env, int val);

int getrlimit(int rsc, struct rlimit *ptr);
int setrlimit(int rsc, const struct rlimit *ptr);
// return 0; non-zero on error
// struct rlimit{
//      rlmi_t rlim_cur;     // soft limit: current limit
//      rlmi_t rlim_max;   } // hard limit: max val for rlim_cur
// RLIMIT_CORE, RLIMIT_DATA, RLIMIT_CPU, RLIMIT_FSIZE, RLIMIT_FSIZE
// RLMIT_LOCKS, RLIMIT_NOFILE, RLIMIT_NPROC

pid_t getpid(void);  // returns proc id of calling process
pid_t getppid(void); // returns parent proc id of calling process
uid_t getuid(void);  // returns real user id of calling process
uid_t geteuid(void); // returns effective user id of calling process
gid_t getgid(void);  // returns real group id of calling process
gid_t getegid(void); // returns effective group id of calling process

int setuid(uid_t uid);
int setgid(gid_t gid);
// both return 0, -1 on error

pid_t fork(void);
pid_t vfork(void);
// returns 0 in child; pid of child in parent; 1 on error

pid_t wait(int *statloc);
pid_t waitpid(pid_t pid, int *statloc, int options);
// waitpid() waits for a particular process to terminate
// waitpid() supports a pid argument for:
//      pid == 1, waits for any child
//      pid >  0, waits for child whose pid = pid argument
//      pid == 0, waits for any child whose gid = gid of calling process
//      pid <  1, waits for any child whose gid = absolute value of pid

int execvp(const char **file, char *const argv[]);
//  execlp                 execl                 execle
//    ↓ build argv           ↓ build argv           ↓ build argv
//  execvp --------------> execv --------------> execve
//         try each path          use environ      (system call)
