#!/bin/bash

# http://www.vicente-navarro.com/blog/2008/01/13/backups-con-rsync/
# -a, --archive               archive mode; equals -rlptgoD (no -H,-A,-X)
# -r, --recursive             recurse into directories
# -t, --times                 preserve modification times
# -v, --verbose               increase verbosity
#     --progress              show progress during transfer
# -u, --update                skip files that are newer on the receiver
# -s, --protect-args          no space-splitting; only wildcard special-chars
# -z, --compress              compress file data during the transfer

# NOTA: la ruta de la carpeta EXTERNO siempre debe terminar con /

TEMP=""
LOCAL=${PWD}
EXTERNO=/media/roberto/RWEST/Django/modelo

echo 'Seleccione acción:'
echo '1 - desde directorio local a USB'
echo '2 - desde USB a directorio local'

read doit

case $doit in
  1)
    echo 'desde directorio local a USB'
    # rsync -r -t -v --progress -u -s --exclude '.picasa.ini'   $LOCAL/  $EXTERNO/
    # rsync -ausrtvP --progress --exclude='*' --include='*.'{py,html} $LOCAL/  $EXTERNO/
    # rsync -ausrtvP --progress --exclude 'migrations/' --exclude '__pycache__/' --exclude '*.pyc' --exclude 'sync.sh' $LOCAL/  $EXTERNO/
    # rsync -ausrtvP --progress --include '*.py' --include '*.html' $LOCAL/  $EXTERNO/
    # rsync -ausrtvP --progress --exclude={migrations,__pycache__} $LOCAL/  $EXTERNO/
    echo "desde " $LOCAL " a " $EXTERNO
    ;;
  2)
    echo 'desde USB a directorio local'
    TEMP=$EXTERNO
    EXTERNO=$LOCAL
    LOCAL=$TEMP
    # rsync -ausrtvP --progress --exclude={migrations,__pycache__} $EXTERNO/ $LOCAL/
    echo "desde " $EXTERNO " a " $LOCAL
    ;;
  *) echo "debe seleccionar una opción válida" ;;
esac

