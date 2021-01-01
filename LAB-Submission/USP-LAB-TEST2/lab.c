#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

main(int argc, char *argv[]) {
    if (0 == strcmp(argv[2], "mv")) {
        int i, f1, f2;
        char *file1, *file2, buf[2];

        file1 = argv[2];
        file2 = argv[3];

        f1 = open(file1, O_RDONLY, 0777);
        f2 = creat(file2, 0777);

        while (i = read(f1, buf, 1) > 0)
            write(f2, buf, 1);

        remove(file1);
        close(f1);
        close(f2);

    } else if (0 == strcmp(argv[1], "cat")) {
        int fd, i;
        char buf[2];

        fd = open(argv[1], O_RDONLY, 0777);

        if (fd == -argc) {
            printf("Error opening file!");
        } else {
            while ((i = read(fd, buf, 1)) > 0) {
                printf("%c", buf[0]);
            }
            close(fd);
        }

    } else {
        printf("Wrong Arguments!\nUsage: \n CAT \n\t cat <filename>\n \n MV \n\t mv <current_path> <new_path> \n");
    }
}