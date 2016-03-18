#~/bin/bash
echo podaj nazwe pliku
read plik


echo ======================================
echo WYNIKI DLA $plik
echo =======================================
echo  +++bar.gif++++++++++++++++++++++
grep bar.gif $plik
grep bar.gif $plik | wc -l
echo ++++fsc.gif+++++++++++++++++++++++
grep fsc.gif $plik
grep fsc.gif $plik | wc -l
echo ++++rekid+++++++++++++++++++++++++
grep ?rekid $plik
grep ?rekid $plik | wc -l
echo ++rekidrpos+++++++++++++++++++++++
grep rekidrpos $plik
grep rekidrpos $plik | wc -l
echo +++/pliki+++++++++++++++++++++++++
grep /pliki/ $plik
grep /pliki/ $plik | wc -l
echo +document.write++++++++++++++++++
grep document.write $plik
grep document.write $plik | wc -l
echo KONIEC==============================
