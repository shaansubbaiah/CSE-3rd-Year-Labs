#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

main(int argc, char *argv[]) {
    int i, f1, f2;
    char *file1, *file2, buf[2];

    file1 = argv[1];
    file2 = argv[2];

    f1 = open(file1, O_RDONLY, 0777);
    f2 = creat(file2, 0777);

    while (i = read(f1, buf, 1) > 0)
        write(f2, buf, 1);

    remove(file1);
    close(f1);
    close(f2);
}