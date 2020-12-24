#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
    int fd;
    char* testpipe = "/temp/testpipe";

    // Creating the named file(FIFO) using mkfifo(<pathname>, <permission>)
    mkfifo(testpipe, 0666);

    char arr1[80], arr2[80];
    while (1) {
        // write to the pipe
        fd = open(testpipe, O_WRONLY);
        fgets(arr2, 80, stdin);

        write(fd, arr2, strlen(arr2) + 1);
        close(fd);

        // then, read the pipe
        fd = open(testpipe, O_RDONLY);
        read(fd, arr1, sizeof(arr1));

        printf("User2: %s\n", arr1);
        close(fd);
    }
    return 0;
}
