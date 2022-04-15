import pendulum


def job():

    with open('userspace/test_data/selfie.jpg', 'rb') as selfie_file:
        jpg_file = selfie_file.read()

    with open('userspace/test_data/phone.pdf', 'rb') as selfie_file:
        pdf_file = selfie_file.read()

    return {
        'identifier': 'wrapper test',
        'payload': {
            'message': 'Hello, World!',
            'dtg': pendulum.now().to_iso8601_string(),
            'countdown': [3, 2, 1],
            'note': 'See the attachments.',
        },
        'attachments': [
            {
                'filename': 'filename1.txt',
                'binary_contents': b'binary data goes here',
            },
            {
                'filename': 'filename2.txt',
                'binary_contents': b'... and some more binary data.',
            },
            {
                'filename': 'selfie.jpg',
                'binary_contents': jpg_file,
            },
            {
                'filename': 'phone.pdf',
                'binary_contents': pdf_file,
            }
        ]
    }
