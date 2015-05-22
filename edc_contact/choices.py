FOLLOW_UP = (
    ('sms', 'SMS'),
    ('call', 'Call'),
    ('in_person', 'In Person'),
    ('mail', 'mail'),
)

APPT_LOCATIONS = (
    ('home', 'At home'),
    ('work', 'At work'),
    ('clinic', 'At clinic'),
    ('OTHER', 'Other location'),
)

APPT_GRADING = (
    ('firm', 'Firm appointment'),
    ('weak', 'Possible appointment'),
    ('guess', 'Estimated by RA'),
)

CONTACT_TYPE = (
    ('direct', 'Direct edc_contact with participant'),
    ('indirect', 'Contact with person other than participant'),
    ('no_contact', 'No edc_contact made'),
)
