#!/bin/bash
function show_time () {
    num=$1
    min=0
    hour=0
    day=0
    if((num>59));then
        ((sec=num%60))
        ((num=num/60))
        if((num>59));then
            ((min=num%60))
            ((num=num/60))
            if((num>23));then
                ((hour=num%24))
                ((day=num/24))
            else
                ((hour=num))
            fi
        else
            ((min=num))
        fi
    else
        ((sec=num))
    fi
    echo "$hour"h "$min"m "$sec"s
}

START=$(date +%s)
echo " ";
echo ".dP\"Y8  dP\"\"b8 88  88 888888 8888b.  .dP\"Y8 888888    db    88     88  dP     88   88 88\"\"Yb 8888b.     db    888888 888888 ";
echo "\`Ybo.\" dP   \`\" 88  88 88__    8I  Yb \`Ybo.\"   88     dPYb   88     88odP      88   88 88__dP  8I  Yb   dPYb     88   88__   ";
echo "o.\`Y8b Yb      888888 88\"\"    8I  dY o.\`Y8b   88    dP__Yb  88  .o 88\"Yb      Y8   8P 88\"\"\"   8I  dY  dP__Yb    88   88\"\"   ";
echo "8bodP'  YboodP 88  88 888888 8888Y\"  8bodP'   88   dP\"\"\"\"Yb 88ood8 88  Yb     \`YbodP' 88     8888Y\"  dP\"\"\"\"Yb   88   888888 ";
echo "                                                                                                                            ";
echo "                                                                                                                            ";
echo "                                                                                                                            ";
echo "                                                                                                                            ";
echo "# Cleaning Data ...."
echo ""
rm -rf ../data/*
## generate deplist.py
python dep_parser.py
## generate allmk.py
python allmk_parser.py
## generate mkList.py
python mkList_parser.py
## generate studentList.py
python student_parser.py
# generate scheduleData.py
python sched_parser.py

echo " _   __   __  _  ___  _ ___    __ ___ __  _ ___ ___  __ _____ __  ___  ";
echo "| | /__\ /__\| |/ / || | _,\  / _] __|  \| | __| _ \/  \_   _/__\| _ \ ";
echo "| || \/ | \/ |   <| \/ | v_/ | [/\ _|| | ' | _|| v / /\ || || \/ | v / ";
echo "|___\__/ \__/|_|\_\\__/|_|    \__/___|_|\__|___|_|_\_||_||_| \__/|_|_\ ";

# generate mkLookup.py
python mkLookupGenerator.py
# generate studentLookup.py
python studentLookupGenerator.py
# generate classLookup.py
python classLookupGenerator.py
# generate matkulClassLookup.py
python matkulClassLookupGenerator.py
# generate matkulPartLookup.py
python matkulPartLookupGenerator.py 
# generate attendClassLookup.py
python attendClassLookupGenerator.py

END=$(date +%s)
DIFF=$(( $END - $START ))
cp *Lookup.py ../data/
cp studentList.py ../data/
cp scheduleData.py ../data/
cp mkList.py ../data/
echo ""
echo "Update SchedStalk Selesai ..."
echo -n "Waktu Eksekusi Total "; show_time $DIFF