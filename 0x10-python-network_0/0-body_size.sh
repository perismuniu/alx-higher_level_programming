#!/bin/bash
#Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

#!/bin/bash

URL=$1

RESPONSE=$(curl -s $URL)
SIZE=$(echo -n "$RESPONSE" | wc -c)

echo $SIZE
