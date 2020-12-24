#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
    int fd1;
    char* testpipe = "/temp/testpipe";

    // Creating the named file(FIFO) using mkfifo(<pathname>,<permission>)
    mkfifo(testpipe, 0666);

    char str1[80], str2[80];
    while (1) {
        // read from the pipe
        fd1 = open(testpipe, O_RDONLY);
        read(fd1, str1, 80);

        printf("User1: %s\n", str1);
        close(fd1);

        // then, write to the pipe
        fd1 = open(testpipe, O_WRONLY);
        fgets(str2, 80, stdin);

        write(fd1, str2, strlen(str2) + 1);
        close(fd1);
    }
    return 0;
}
