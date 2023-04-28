from datetime import date, timedelta

import pytest
from flora_api_client.schemas.users import PartnerWorkScheduleSchema
from flora_api_client.presentations.users import WorkSchedule

_work_schedule = {
    "monday": {
        "start": "09:00",
        "end": "18:00",
    },
    "tuesday": {
        "start": "10:00",
        "end": "19:00",
    },
    "wednesday": {
        "start": "11:00",
        "end": "20:00",
    },
    "thursday": {
        "start": "12:00",
        "end": "21:00",
    },
    "friday": {
        "start": "13:00",
        "end": "22:00",
    },
    "exceptions": [
        {
            "start": "2023-05-01",
            "end": "2023-05-01",
            "action": "rest",
            "time_start": "",
            "time_end": "",
        },
        {
            "start": "2023-04-29",
            "end": "2023-04-29",
            "action": "work",
            "time_start": "10:00",
            "time_end": "13:00",
        },
    ],
}


def test_work_schedule_get_working_time():
    ws: WorkSchedule = PartnerWorkScheduleSchema().load(_work_schedule)
    start_date = date(year=2023, month=4, day=1)
    dates = [start_date + timedelta(days=i) for i in range(60)]
    for d in dates:
        if d == date(year=2023, month=5, day=1):
            expected = None
        elif d == date(year=2023, month=4, day=29):
            expected = ("10:00", "13:00")
        else:
            day = d.strftime("%A").lower()
            sh = getattr(ws, day)
            expected = (sh.start, sh.end) if sh else None
        assert ws.get_working_time(d) == expected
