---
title: ""
posted: 1141 08/07/2024
mood: 50%
---

```sh
ENTRY_DATE=$(date +%H%M%d%m%Y)
cp template.md "Entry $ENTRY_DATE.md"
sed -i "s|posted:.*|posted: \"$(date +%H%M\ %d\/%m\/%Y)\"|g" "Entry $ENTRY_DATE.md"
```

content.
