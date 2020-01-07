#!/bin/bash
# Special request.
curl -s -d "user_id=98" -X PUT -L -H "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
