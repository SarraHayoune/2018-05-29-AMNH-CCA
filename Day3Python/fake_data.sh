#let's create a header
echo 'xaxis yaxis'> data/linear_data.dat
# let'a perform a for loop

for xdat in {1..10};
do
echo $xdat $((xdat*2)) >> data/linear_data.dat
done