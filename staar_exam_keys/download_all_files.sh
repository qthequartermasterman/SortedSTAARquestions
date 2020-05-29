wget -i filenames.txt --trust-server-names
for i in *.xlsx; do xlsx2csv $i > "$i.csv"; done
