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
echo "XMPRO_VERSION_PLATFORM is: "$XMPRO_VERSION_PLATFORM

# Define the updated table content
updated_table="<table><thead><tr><th width=\"242\">Product</th><th data-type=\"number\">SAST Score</th><th>DAST Score</th><th>Date</th><th data-hidden></th></tr></thead><tbody>
<tr><td>Subscription Manager $XMPRO_VERSION_PLATFORM</td><td>$SM_SAST</td><td>$SM_DAST</td><td>$current_date</td><td></td></tr>
<tr><td>App Designer $XMPRO_VERSION_PLATFORM</td><td>$AD_SAST</td><td>$AD_DAST</td><td>$current_date</td><td></td></tr>
<tr><td>Data Stream Designer $XMPRO_VERSION_PLATFORM</td><td>$DS_SAST</td><td>$DS_DAST</td><td>$current_date</td><td></td></tr>
<tr><td>XMPro AI $XMPRO_VERSION_PLATFORM</td><td>$AI_SAST</td><td>$AI_DAST</td><td>$current_date</td><td></td></tr>
<tr><td>WorkFlow</td><td>$WF_SAST</td><td>$WF_DAST</td><td>$current_date</td><td></td></tr></tbody></table>"

#cleanup update_table by removing nextlines
updated_table=$(echo "$updated_table" | tr -d '\n')

# Replace the existing table content in readme.md
sed -i 's|<table>.*<\/table>|'"$updated_table"'|' docs/resources/platform-security.md

# Optional: Display a success message
echo "platform-security.md updated successfully!"
