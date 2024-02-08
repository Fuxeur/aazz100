import os
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

       ██╗  ██╗  ████████╗ ██████╗  ██████╗ ██╗     
       ██║ ██╔╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
       █████╔╝█████╗██║   ██║   ██║██║   ██║██║     
       ██╔═██╗╚════╝██║   ██║   ██║██║   ██║██║     
       ██║  ██╗     ██║   ╚██████╔╝╚██████╔╝███████╗
       ╚═╝  ╚═╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                             

''')


os.chdir("/home/userland")

print("""
1:metasploite
2:set
3:sherlock
4:nmap
""")
cmd = input(">")
if cmd == "1":
	os.system("msfconsole")
if cmd == "2":
	os.system("sudo setoolkit")
if cmd == "3":
	os.chdir("Mr.Holmes")
	os.system("python3 MrHolmes.py")
if cmd == "4":
	os.system("nmap -h")
