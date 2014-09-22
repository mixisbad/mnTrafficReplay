#!/bin/bash

if [ -z "$1" ];
then
    echo "Usage: $0 log_file"
else
    head -100 $1 | sed -E 's/([^ \-]*) .* (\[.*\]) (\"[^"]*\") .*/\1;\2;\3/g' > "$1.replay"
fi;
