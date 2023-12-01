#!/bin/bash
# send GET request to URL and display the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
