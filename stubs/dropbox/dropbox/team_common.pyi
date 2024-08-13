from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class GroupManagementType(bb.Union):
    user_managed: Incomplete
    company_managed: Incomplete
    system_managed: Incomplete
    other: Incomplete
    def is_user_managed(self): ...
    def is_company_managed(self): ...
    def is_system_managed(self): ...
    def is_other(self): ...

GroupManagementType_validator: Incomplete

class GroupSummary(bb.Struct):
    group_name: Incomplete
    group_id: Incomplete
    group_external_id: Incomplete
    member_count: Incomplete
    group_management_type: Incomplete
    def __init__(
        self,
        group_name: Incomplete | None = None,
        group_id: Incomplete | None = None,
        group_management_type: Incomplete | None = None,
        group_external_id: Incomplete | None = None,
        member_count: Incomplete | None = None,
    ) -> None: ...

GroupSummary_validator: Incomplete

class GroupType(bb.Union):
    team: Incomplete
    user_managed: Incomplete
    other: Incomplete
    def is_team(self): ...
    def is_user_managed(self): ...
    def is_other(self): ...

GroupType_validator: Incomplete

class MemberSpaceLimitType(bb.Union):
    off: Incomplete
    alert_only: Incomplete
    stop_sync: Incomplete
    other: Incomplete
    def is_off(self): ...
    def is_alert_only(self): ...
    def is_stop_sync(self): ...
    def is_other(self): ...

MemberSpaceLimitType_validator: Incomplete

class TimeRange(bb.Struct):
    start_time: Incomplete
    end_time: Incomplete
    def __init__(self, start_time: Incomplete | None = None, end_time: Incomplete | None = None) -> None: ...

TimeRange_validator: Incomplete
GroupExternalId_validator: Incomplete
GroupId_validator: Incomplete
MemberExternalId_validator: Incomplete
ResellerId_validator: Incomplete
TeamId_validator: Incomplete
TeamMemberId_validator: Incomplete
ROUTES: Incomplete
