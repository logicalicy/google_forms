import requests

def google_forms(form_key, request_body):
    """Execute a HTTP POST request to the Google Form.

    Args:
        form_key (str):         The key that identifies the Google Form.
        request_body (dict):    Contains a `data` key that maps to array of
                                name-value pairs to submit to the Google Form.

    Returns:
        int: HTTP status code returned by HTTP POST request to the Google Form.

    Example:
        from google_forms import google_forms

        response_status = google_forms(
            '2ae5KGBJrE3HmPSLnUyVwKENTpasiwueI9ZlOpsW3kdp',
            { 'entry.92010082': 'example@gmail.com' }
        )
        // response_status = 200

    """
    if not form_key:
        return 400
    form_fields = request_body.get('data', [])
    data = {}
    for form_field in form_fields:
        data[form_field.get('name')] = form_field.get('value')
    r = requests.post('https://docs.google.com/forms/d/%s/formResponse' % form_key, data=data)
    return r.status_code
