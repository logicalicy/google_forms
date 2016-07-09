# Summary

A simple API for creating a web proxy for Google forms.

# Install

```
pip install google_forms
```

# Usage

```
from google_forms import google_forms

response_status = google_forms(
    '2ae5KGBJrE3HmPSLnUyVwKENTpasiwueI9ZlOpsW3kdp',
    { 'entry.92010082': 'example@gmail.com' }
)
// response_status = 200
```


# License

See [LICENSE](LICENSE).
