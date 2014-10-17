#!/bin/bash

log_pattern='s/([^ \-]*) .* (\[.*\]) (\"[^"]*\") .*/\1;\2;\3/g' 

if [ -z "$1" ];
then
    echo "Usage: $0 log_file"
else
    sed -E "$log_pattern" > "$1.replay"
fi;
