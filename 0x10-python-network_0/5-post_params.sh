#!/bin/bash
# Sends a POST request to the passed URL.
curl -sd "$1" -X POST "email=hr@holbertonschool.com&subject=I will always be here for PLD"
