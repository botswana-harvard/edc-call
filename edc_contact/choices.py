from django.utils.translation import ugettext as _

from edc_constants.constants import NOT_APPLICABLE, YES, NO, ALIVE, DEAD, UNKNOWN

# choices
BLANK_CHOICE_DASH = [('', '---------')]

""" Try to keep this in alphabetical order """

ACU_EST = (
    ('Acute', 'Acute'),
    ('Established', 'Established'),
)

ACU_EST_NEG = (
    ('Acute', 'Acute'),
    ('Established', 'Established'),
    ('Negative', 'Negative'),
)

ALIVE_DEAD = (
    (ALIVE, 'Alive'),
    (DEAD, 'Dead'),
)

ALIVE_DEAD_UNKNOWN = (
    (ALIVE, 'Alive'),
    (DEAD, 'Dead'),
    (UNKNOWN, 'Unknown'),
)

CONFIRMED_SUSPECTED = (
    ('CONFIRMED', 'Confirmed'),
    ('SUSPECTED', 'Suspected'),
)

COUNTRY = (
    ('botswana', 'Botswana'),
    ('zimbabwe', 'Zimbabwe'),
    ('rsa', 'South Africa'),
    ('zambia', 'Zambia'),
    ('namibia', 'Namibia'),
    ('nigeria', 'Nigeria'),
    ('china', 'China'),
    ('india', 'India'),
    ('OTHER', 'Other'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('AnyDay', 'Any Day'),
)

TIME_OF_DAY = (
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening'),
    ('Anytime', 'Anytime'),
)

DATE_ESTIMATED = (
    ('-', 'No'),
    ('D', 'Yes, estimated the Day'),
    ('MD', 'Yes, estimated Month and Day'),
    ('YMD', 'Yes, estimated Year, Month and Day'),
)

FEEDING = (
    ('BF', 'Breast Feed'),
    ('FF', 'Formula Feed'),
)

GENDER = (
    ('M', _('Male')),
    ('F', _('Female')),
)

GENDER_UNDETERMINED = (
    ('M', _('Male')),
    ('F', _('Female')),
    ('U', _('Undetermined')),
)

"""do not change without inspecting implication to check_omang_field() in utils.py"""
IDENTITY_TYPE = (
    ('OMANG', 'Omang'),
    ('DRIVERS', 'Driver\'s License'),
    ('PASSPORT', 'Passport'),
    ('OMANG_RCPT', 'Omang Receipt'),
    ('OTHER', 'Other'),
)


NORMAL_ABNORMAL = (
    ('NORMAL', 'Normal'),
    ('ABNORMAL', 'Abnormal'),
)

NORMAL_ABNORMAL_NOEXAM = (
    ('NORMAL', 'Normal'),
    ('ABNORMAL', 'Abnormal'),
    ('NO_EXAM', 'No Exam Performed'),
)

NORMAL_ABNORMAL_NOTEVALUATED = (
    ('NORMAL', 'Normal'),
    ('ABNORMAL', 'Abnormal'),
    ('NOT_EVAL', 'Not Evaluated'),
)

REFUSAL_STATUS = (
    ('REFUSED', 'Refused'),
    ('NOT_REFUSED', 'No longer refusing'),
)

SEVERITY_LEVEL = (
    ('mild', 'Mild'),
    ('moderate', 'Moderate'),
    ('severe', 'Severe'),
)

TIME_OF_WEEK = (
    ('weekdays', 'Weekdays'),
    ('weekend', 'Weekends'),
)

TIME_OF_DAY = (
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening'),
)

TIME_UNITS = (
    ('TODAY', 'Today'),
    ('DAYS', 'Days'),
    ('WEEKS', 'Weeks'),
    ('MONTHS', 'Months'),
    ('YEARS', 'Years'),
)

WILL_DECL = (
    ('WILLING', 'Willing'),
    ('DELINED', 'Declined'),
)

YES_NO = (
    (YES, _(YES)),
    (NO, _(NO)),
)

YES_NO_DECLINED = (
    (YES, YES),
    (NO, NO),
    ('Declined', 'Yes, but subject declined copy'),
)

YES_NO_OPTIONAL = (
    (YES, YES),
    (NO, NO),
    ('Optional', 'Optional'),
)

YES_NO_REFUSED = (
    (YES, _(YES)),
    (NO, _(NO)),
    ('REF', _('Refused to answer')),
)

YES_NO_DWTA = (
    (YES, _(YES)),
    (NO, _(NO)),
    ('DWTA', _('Don\'t want to answer')),
)

YES_NO_NA_SPECIFY = (
    (YES, 'Yes, (Specify below)'),
    (NO, NO),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_NA = (
    (YES, YES),
    (NO, NO),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_NOT_EVALUATED = (
    (YES, YES),
    (NO, NO),
    ('Not_evaluated', 'Not evaluated'),
)

YES_NO_NOT_EVALUATED_NA = (
    (YES, YES),
    (NO, NO),
    ('Not_evaluated', 'Not evaluated'),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_NOT_DONE = (
    (YES, YES),
    (NO, NO),
    ('Not_done', 'Not Done'),
)

YES_NO_DOESNT_WORK = (
    (YES, YES),
    (NO, NO),
    ('DontWork', 'Doesn\'t work'),
)

YES_NO_UNKNOWN = (
    (YES, YES),
    (NO, NO),
    ('Unknown', 'Unknown'),
)

YES_NO_UNKNOWN_NA = (
    (YES, YES),
    (NO, NO),
    ('Unknown', 'Unknown'),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_UNSURE = (
    (YES, YES),
    (NO, NO),
    ('Not Sure', 'Not Sure'),
)

YES_NO_UNSURE_NA = (
    (YES, YES),
    (NO, NO),
    ('Not Sure', 'Not Sure'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

YES_NO_DONT_KNOW = (
    (YES, YES),
    (NO, NO),
    ('Dont_know', 'Do not Know'),
)

YES_NO_DONT_KNOW_NA = (
    (YES, YES),
    (NO, NO),
    ('Dont_know', 'Do not Know'),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_DOESNT_WORK = (
    (YES, YES),
    (NO, NO),
    ('Doesnt_work', 'Doesnt Work'),
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

FOLLOW_UP = (
    ('sms', 'SMS'),
    ('call', 'Call'),
    ('in_person', 'In Person'),
    ('mail', 'mail'),
)

REFERRAL_APPT_COMMENTS = (
    ("N/A", "not applicable"),
    ("conflict", "have another commitment"),
    ("prefer_other_facility", "prefer another health facility than the local clinic"),
    ("prefer_other_date", "prefer to come on my own convenient time"),
    ("undecided_thinking", "have to think about it"),
    ("undecided_accepting_status", "need time to accept my HIV status"),
    ("have_other_anc_appt", "have already registered with ANC and have another appointment"),
    ("personal_reasons", "personal reasons"),
)

REFERRAL_CODES = (
    ('pending', '<data collection in progress>'),
    ('TST-CD4', 'POS any, need CD4 testing'),
    ('TST-HIV', 'HIV test'),
    ('MASA-CC', 'Known POS, MASA continued care'),
    ('MASA-DF', 'Known POS, MASA defaulter (was on ART)'),
    ('SMC-NEG', 'SMC (uncircumcised, hiv neg)'),
    ('SMC?NEG', 'SMC (Unknown circumcision status, hiv neg'),
    ('SMC-UNK', 'SMC (uncircumcised, hiv result not known)'),
    ('SMC?UNK', 'SMC (Unknown circumcision status, hiv result not known)'),
    ('NEG!-PR', 'NEG today, Pregnant'),
    ('POS!-PR', 'POS today, Pregnant'),
    ('UNK?-PR', 'HIV UNKNOWN, Pregnant'),
    ('POS#-AN', 'Known POS, Pregnant, on ART (ANC)'),
    ('POS#-PR', 'Known POS, Pregnant, not on ART'),
    ('POS!-HI', 'POS today, not on ART, high CD4)'),
    ('POS!-LO', 'POS today, not on ART, low CD4)'),
    ('POS#-HI', 'Known POS, not on ART, high CD4)'),
    ('POS#-LO', 'Known POS, not on ART, low CD4)'),
)

VISIT_INFO_SOURCE = [
    ('subject', '1. Subject'),
    ('other_member', '2. Other household member'),
    ('OTHER', '9. Other'),
    ]

VISIT_REASON = [
    ('consent', '1. Consent and Survey with subject'),
    ('absent', '2. Absentee'),
    ('undecided', '3. Undecided (with subject)'),
    ('refuse', '4. Refusal (with subject)'),
    ]

RELATION = (
    ('spouse', _('spouse')),
    ('parent', _('parent')),
    ('sibling', _('sibling')),
    ('child', _('child')),
    ('aunt/uncle', _('aunt/uncle')),
    ('cousin', _('cousin')),
    ('partner', _('partner/boyfriend/girlfriend')),
    ('OTHER', _('Other, specify')),
)

YES_NO_RECORD_REFUSAL = (
    ('Yes', _('Yes')),
    ('No', _('No')),
    ('Don\'t want to answer', _('Don\'t want to answer')),
    ('record refusal', _('Participant does not want to provide record')),
    )
