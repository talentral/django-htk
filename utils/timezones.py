from zoneinfo import available_timezones

# Pre-computed set of valid IANA timezone names (used for O(1) lookups).
VALID_TIMEZONES = available_timezones()

# Mapping of legacy, informal, or invalid timezone strings → canonical IANA names.
#
# Rules applied (in order):
#  1. Exact match in this dict → use the mapped value
#  2. Value is in zoneinfo.available_timezones() → accept as-is
#  3. Otherwise → fall back to DEFAULT_TIMEZONE
#
# Covers:
#  - Bare continent/region names returned by pygeoip for unresolvable IPs
#  - Informal US region names ('Eastern', 'Pacific', etc.)
#  - POSIX abbreviations ('EST', 'PST', etc.)
#  - Deprecated pytz US/ and Canada/ aliases
#  - Legacy pytz city names renamed in IANA
#  - GMT offset literals

DEFAULT_TIMEZONE = 'America/Los_Angeles'

TIMEZONE_ALIASES = {
    # ── Continent-only strings (returned by pygeoip for low-resolution IPs) ──
    'Africa': DEFAULT_TIMEZONE,
    'America': DEFAULT_TIMEZONE,
    'Antarctica': DEFAULT_TIMEZONE,
    'Arctic': DEFAULT_TIMEZONE,
    'Asia': DEFAULT_TIMEZONE,
    'Atlantic': DEFAULT_TIMEZONE,
    'Australia': 'Australia/Sydney',
    'Europe': 'Europe/London',
    'Indian': DEFAULT_TIMEZONE,
    'Pacific': DEFAULT_TIMEZONE,
    'US': DEFAULT_TIMEZONE,

    # ── Informal US region names ─────────────────────────────────────────────
    'Eastern': 'America/New_York',
    'Central': 'America/Chicago',
    'Mountain': 'America/Denver',
    'Alaska': 'America/Anchorage',
    'Hawaii': 'Pacific/Honolulu',
    'Arizona': 'America/Phoenix',

    # ── POSIX-style abbreviations (not valid IANA) ───────────────────────────
    'EST': 'America/New_York',
    'EDT': 'America/New_York',
    'CST': 'America/Chicago',
    'CDT': 'America/Chicago',
    'MST': 'America/Denver',
    'MDT': 'America/Denver',
    'PST': 'America/Los_Angeles',
    'PDT': 'America/Los_Angeles',
    'AKST': 'America/Anchorage',
    'AKDT': 'America/Anchorage',
    'HST': 'Pacific/Honolulu',
    'GMT': 'Etc/UTC',
    'UTC': 'Etc/UTC',

    # ── Old US/ aliases (deprecated pytz aliases, not in zoneinfo) ──────────
    'US/Eastern': 'America/New_York',
    'US/Central': 'America/Chicago',
    'US/Mountain': 'America/Denver',
    'US/Pacific': 'America/Los_Angeles',
    'US/Alaska': 'America/Anchorage',
    'US/Hawaii': 'Pacific/Honolulu',
    'US/Arizona': 'America/Phoenix',
    'US/East-Indiana': 'America/Indiana/Indianapolis',
    'US/Indiana-Starke': 'America/Indiana/Knox',
    'US/Michigan': 'America/Detroit',
    'US/Samoa': 'Pacific/Pago_Pago',

    # ── Old Canada/ aliases ──────────────────────────────────────────────────
    'Canada/Eastern': 'America/Toronto',
    'Canada/Central': 'America/Winnipeg',
    'Canada/Mountain': 'America/Edmonton',
    'Canada/Pacific': 'America/Vancouver',
    'Canada/Atlantic': 'America/Halifax',
    'Canada/Newfoundland': 'America/St_Johns',
    'Canada/Saskatchewan': 'America/Regina',
    'Canada/Yukon': 'America/Whitehorse',

    # ── Common Europe/ aliases that lack zoneinfo equivalents ───────────────
    'Europe/Kiev': 'Europe/Kyiv',

    # ── Misc legacy pytz names not in zoneinfo ───────────────────────────────
    'Asia/Calcutta': 'Asia/Kolkata',
    'Asia/Katmandu': 'Asia/Kathmandu',
    'Asia/Rangoon': 'Asia/Yangon',
    'Asia/Saigon': 'Asia/Ho_Chi_Minh',
    'Asia/Macao': 'Asia/Macau',
    'Asia/Ulaanbaatar': 'Asia/Ulaanbaatar',  # valid, but alias kept for safety
    'Atlantic/Faeroe': 'Atlantic/Faroe',
    'Pacific/Ponape': 'Pacific/Pohnpei',
    'Pacific/Truk': 'Pacific/Chuuk',
    'Pacific/Yap': 'Pacific/Chuuk',

    # ── GMT offset literals (not IANA zone names) ────────────────────────────
    # No universal mapping exists; we pick a representative city per offset.
    'GMT+0': 'Etc/UTC',
    'GMT-0': 'Etc/UTC',
    'GMT+1': 'Europe/Paris',
    'GMT+2': 'Europe/Helsinki',
    'GMT+3': 'Europe/Moscow',
    'GMT+4': 'Asia/Dubai',
    'GMT+5': 'Asia/Karachi',
    'GMT+5:30': 'Asia/Kolkata',
    'GMT+6': 'Asia/Dhaka',
    'GMT+7': 'Asia/Bangkok',
    'GMT+8': 'Asia/Shanghai',
    'GMT+9': 'Asia/Tokyo',
    'GMT+10': 'Australia/Sydney',
    'GMT+11': 'Pacific/Guadalcanal',
    'GMT+12': 'Pacific/Auckland',
    'GMT-1': 'Atlantic/Azores',
    'GMT-2': 'America/Noronha',
    'GMT-3': 'America/Sao_Paulo',
    'GMT-4': 'America/Halifax',
    'GMT-5': 'America/New_York',
    'GMT-6': 'America/Chicago',
    'GMT-7': 'America/Denver',
    'GMT-8': 'America/Los_Angeles',
    'GMT-9': 'America/Anchorage',
    'GMT-10': 'Pacific/Honolulu',
    'GMT-11': 'Pacific/Pago_Pago',
    'GMT-12': 'Etc/GMT+12',
}
