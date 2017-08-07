# Readonly Sheet API v4

A [Supercode](http://gosupercode.com) function that reads spreadsheet via sheet api v4.

## Sample Usage

[Supercode](http://gosupercode.com) SDK will be available after the launch.

```
import json
import pprint
import supercode

response = supercode.call(
    "super-code-function",
    "your-supercode-api-key",
    spreadsheet_id="1RUBkhrfDT9aaYvb_jgLLQ26Mj8jkT9jOKmMF_PyL2SU ID",
    range_notation="A:B",
    google_key="GOOGLE_KEY_HERE"
)

    
pprint(response)
```

**Note:** Supercode has not been launched yet. This is for internal testing only.