read s1
read s2
l1=${#s1}
l2=${#s2}
t1=$(( $l1 / 2 ))
t2=$(( $l2 / 2 ))
p=0
if [[ "${s1:$t1:1}" !=  "${s2:$t2:1}" ]] 
then  
  echo "-1"  
else  
  while (($(($t1+$p))<$l1 && $(($t2+$p))<$l2))
  do
  if [[ "${s1:$(($t1+$p)):1}" != "${s2:$(($t2+$p)):1}" || "${s1:$(($t1-$p)):1}"  != "${s2:$(($t2-$p)):1}" ]]
  then
  break
  fi
  let "p+=1"
  done
  echo "${s1:$(($t1-$p+1)):$(($p+$p-1))}"
fi