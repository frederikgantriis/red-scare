graphs=$(cat "$1")

echo "Instance name, n, A, F, M, N, S"
for graph in $graphs; do
    n=$(cat "data/$graph" | head -n 1 | cut -d' ' -f1)

    alternate=$(cat "data/$graph" | python3 "solutions/alternate.py")
    few=$(cat "data/$graph" | python3 "solutions/few.py")
    many=$(cat "data/$graph" | python3 "solutions/many.py")
    none=$(cat "data/$graph" | python3 "solutions/none.py")
    some=$(cat "data/$graph" | python3 "solutions/some.py")

    echo "$graph, $n, $alternate, $few, $many, $none, $some"

done