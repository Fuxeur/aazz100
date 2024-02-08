import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
print('''


                ..............
                            ..,;:ccc,.
                          ......\'\'\';lxO.
                .....\'\'\'\'..........,:ld;
                           \';;;:::;,,.x,
                      ..\'\'\'.            0Xxoc:,.  ...
                  ....                ,ONkc;,;cokOdc\',.
                 .                   OMo           \':ddo.
                                    dMc               :OO;
                                    0M.                 .:o.
                                    ;Wd
                                     ;XO,
                                       ,d0Odlc;,..
                                           ..\',;:cdOOd::,.
                                                    .:d;.\':;.
                                                       'd,  .\'
                                                         ;l   ..
                                                          .o
                                                            c
                                                            .\'
                                                             .


██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

''')
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 index.py')
    run('mkdir /usr/share/ktool')
    run('cp index.py /usr/share/ktool/index.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/ktool/index.py "$@"')
    with open('/usr/bin/ktool','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/ktool & chmod +x /usr/share/ktool/index.py')
    print('''+------[installed]------+''')
