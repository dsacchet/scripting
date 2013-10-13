#!/bin/bash

echo "<== ($$) Debut du traitement : $(date) ===" | tee -a ~/softs/var/log/get_photo_s5is.log

echo "<== ($$) Verification du modele d'appareil photo ===" | tee -a ~/softs/var/log/get_photo_s5is.log

if [ "x`gphoto2 --auto-detect | head -n 3 | sed -n '3p'`" != "xCanon PowerShot S5 IS (PTP mode) usb:            " ]
then
	echo "<!> ($$) Ce script est prevu pour le S5IS" | tee -a ~/softs/var/log/get_photo_s5is.log
	echo "=== ($$) Fin du traitement : $(date) ===" | tee -a ~/softs/var/log/get_photo_s5is.log
	exit 1
fi

echo "=== ($$) Verification de l'appareil photo reussi ==>" | tee -a ~/softs/var/log/get_photo_s5is.log

echo "<== ($$) Creation du repertoire temporaire ===" | tee -a ~/softs/var/log/get_photo_s5is.log

OLDTMPDIR=$TMPDIR
#export TMPDIR=/home/maison/softs/var
export TMPDIR=/home/maison/datas/photos/atrier
TMPDEST=`mktemp -td`
FINALDESTPHOTOS=/home/maison/datas/photos/S5IS
FINALDESTVIDEOS=/home/maison/datas/videos/S5IS
cd $TMPDEST

echo "=== ($$) Repertoire temporaire cree ==>" | tee -a ~/softs/var/log/get_photo_s5is.log

echo "<== ($$) Debut du telechargement des fichiers ===" | tee -a ~/softs/var/log/get_photo_s5is.log
gphoto2 --camera="Canon PowerShot S5 IS (PTP mode)" --get-all-files 2>&1 | tee -a ~/softs/var/log/get_photo_s5is.log
echo "=== ($$) Telechargement des fichiers termines ==>" | tee -a ~/softs/var/log/get_photo_s5is.log

echo "<== ($$) Debut du classement des photos ===" | tee -a ~/softs/var/log/get_photo_s5is.log
find . -type f -name "*.JPG" | while read file;
do
	echo "<i> ($$) Traitement du fichier : ${file}" | tee -a ~/softs/var/log/get_photo_s5is.log
	date=`strings "$file" | head -n 4 | sed -n "4p" | sed "s@\(....\):\(..\):\(..\) .*@\1\2\3@"`
	echo "<i> ($$) Date trouvee : ${date}" | tee -a ~/softs/var/log/get_photo_s5is.log
	output_path="${FINALDESTPHOTOS}/${date:0:4}/${date:4:2}/${date}"
	mkdir -p "${output_path}" 2>&1 | tee -a ~/softs/var/log/get_photo_s5is.log
	echo "<i> ($$) Deplacement vers le repertoire : ${output_path}" | tee -a ~/softs/var/log/get_photo_s5is.log
	mv "$file" "${output_path}" 2>&1 | tee -a ~/softs/var/log/get_photo_s5is.log
done
echo "=== ($$) Classement des photos termines ==>" | tee -a ~/softs/var/log/get_photo_s5is.log

echo "<== ($$) Debut du classement des videos ===" | tee -a ~/softs/var/log/get_photo_s5is.log
find . -type f -name "*.AVI" | while read file;
do
	echo "<i> ($$) Traitement du fichier : ${file}" | tee -a ~/softs/var/log/get_photo_s5is.log
	date=`strings "$file" | head -n 40 | egrep '[[:alpha:]]* *[[:alpha:]]* *[[:digit:]]* *[[:digit:]]*:[[:digit:]]*:[[:digit:]]* *[[:digit:]]*' | sed "s@... \(...\) \(..\) ..:..:.. \(....\)@\3\1\2@" | sed "s@ @0@g" | sed "s@Jan@01@" | sed "s@Feb@02@" | sed "s@Mar@03@" | sed "s@Apr@04@" | sed "s@May@05@" | sed "s@Jun@06@" | sed "s@Jul@07@" | sed "s@Aug@08@" | sed "s@Sep@09@" | sed "s@Oct@10@" | sed "s@Nov@11@" | sed "s@Dec@12@"`
	echo "<i> ($$) Date trouvee : ${date}" | tee -a ~/softs/var/log/get_photo_s5is.log
	output_path="${FINALDESTVIDEOS}/${date:0:4}/${date:4:2}/${date}"
	mkdir -p "${output_path}" 2>&1 | tee -a ~/softs/var/log/get_photo_s5is.log
	echo "<i> ($$) Deplacement vers le repertoire : ${output_path}" | tee -a ~/softs/var/log/get_photo_s5is.log
	mv "$file" "${output_path}" 2>&1 | tee -a ~/softs/var/log/get_photo_s5is.log
done;
echo "=== ($$) Classement des videos termine ==>" | tee -a ~/softs/var/log/get_photo_s5is.log

echo "<== ($$) Nettoyage des repertoires temporaires ===" | tee -a ~/softs/var/log/get_photo_s5is.log
rm -rf "$TMPDEST" 2>&1 | tee -a ~/softs/var/log/get_photo_s5is.log
export TMPDIR="$OLDTMPDIR"
unset OLDTMPDIR
echo "=== ($$) Repertoires temporaires nettoyes ==>" | tee -a ~/softs/var/log/get_photo_s5is.log

echo "=== ($$) Fin du traitement : $(date) ===" | tee -a ~/softs/var/log/get_photo_s5is.log
