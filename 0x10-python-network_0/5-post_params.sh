#!/bin/bash
# Sends a POST request to the passed URL.
curl -sd  -X POST "$1" "email=hr@holbertonschool.com&subject=I will always be here for PLD"
