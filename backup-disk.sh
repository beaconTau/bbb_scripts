#!/bin/sh
rsync -aAXv --progress / --exclude={/dev/*,/proc/*,/sys/*,/tmp/*,/run/*,/mnt/*,/media/*,/lost+found} cozzyd@cosmogenic.uchicago.edu:~/Work/nuphase/bbone-backup 
