#!/bin/bash

# Get the current date in the format "DD Mon YY"
current_date=$(date +'%d %b %y')
echo "SM_SAST score is: "$SM_SAST
echo "SM_DAST score is: "$SM_DAST
echo "AD_SAST score is: "$AD_SAST
echo "AD_DAST score is: "$AD_DAST
echo "DS_SAST score is: "$DS_SAST
echo "DS_DAST score is: "$DS_DAST
echo "AI_SAST score is: "$AI_SAST

# Define the updated table content
updated_table="<table><thead><tr><th width=\"242\">Product</th><th data-type=\"number\">SAST Score</th><th>DAST Score</th><th>Date</th><th data-hidden></th></tr></thead><tbody>
<tr><td>Subscription Manager</td><td>$SM_SAST</td><td>$SM_DAST</td><td>$current_date</td><td></td></tr>
<tr><td>App Designer</td><td>$AD_SAST</td><td>$AD_DAST</td><td>$current_date</td><td></td></tr>
<tr><td>Data Stream Designer</td><td>$DS_SAST</td><td>$DS_DAST</td><td>$current_date</td><td></td></tr>
<tr><td>XMPro AI</td><td>$AI_SAST</td><td>Not Available</td><td>$current_date</td><td></td></tr></tbody></table>"

#cleanup update_table by removing nextlines
updated_table=$(echo "$updated_table" | tr -d '\n')

# Replace the existing table content in readme.md
sed -i 's|<table>.*<\/table>|'"$updated_table"'|' platform-security.md

# Optional: Display a success message
echo "platform-security.md updated successfully!"
