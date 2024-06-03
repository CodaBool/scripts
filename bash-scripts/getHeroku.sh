#!/bin/bash
wholePercent=$(/snap/bin/heroku ps -a codabool-nextjs-home | grep 'this month' | grep -o -P "(?<=\().*(?=\))")
justInt=${wholePercent::-1}
echo $justInt