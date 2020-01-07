#!/bin/bash
# Special request.
curl -sdX PUT "user_id=98" -LH "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
