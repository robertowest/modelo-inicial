#!/bin/bash

# todos los archivos exceptuando algunas carpetas
# rsync -avzr --progress --exclude 'migrations/' --exclude '__pycache__/' --exclude '*.pyc' --exclude 'sync.sh' /media/roberto/RWEST/modelo/ /home/roberto/Desarrollo/django/modelo

# solo archivos python y html

# desde USB a PC
# rsync -avzr --progress --include '*.py' --include '*.html' /media/roberto/RWEST/Django/modelo/ /home/externo/Desarrollo/django/modelo


# desde PC a USB
# rsync -avzr --progress --include '*.py' --include '*.html' /home/externo/Desarrollo/django/modelo/ /media/roberto/RWEST/Django/modelo
