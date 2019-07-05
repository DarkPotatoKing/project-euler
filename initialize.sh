# must be run as "source initialize.sh [number]" for the export to work properly
export PROJECT_EULER_PROBLEM="$1"
python create.py $1
clear
echo Problem $1 initialized
echo
