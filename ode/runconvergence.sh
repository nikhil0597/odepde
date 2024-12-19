NCELL=$1
FILE=error.txt
rm -rf $FILE && touch $FILE
for ncell in $NCELL
do 
   echo "ncell = $ncell"
   python ode.py -nc $ncell -tmin 0.0 -tmax 1.6 -yinit 2.0 -plot 'no' -compute_error yes \
         -time_scheme rk4 >log.txt
   tail -n 1 log.txt
   tail -n 1 log.txt >> $FILE
done
echo "Wrote file $FILE"