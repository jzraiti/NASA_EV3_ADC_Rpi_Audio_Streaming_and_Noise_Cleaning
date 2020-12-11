#include <stdio.h>
#include <stdlib.h>

#define SHELLSCRIPT "\
#/bin/bash \n\
echo \"hello\" \n\
echo \"using python version 3.7.1\" \n\
echo \"running python jasons_continuous_forGstreamer.py\" \n\
python jasons_continuous_forGstreamer.py & \n\
echo \"python script run\" \n\
"

int main()
{
    puts("Will execute sh with the following script :");
    puts(SHELLSCRIPT);
    puts("Starting now:");
    system(SHELLSCRIPT);
    return 0;
}
