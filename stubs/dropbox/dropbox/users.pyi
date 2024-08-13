from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class Account(bb.Struct):
    account_id: Incomplete
    name: Incomplete
    email: Incomplete
    email_verified: Incomplete
    profile_photo_url: Incomplete
    disabled: Incomplete
    def __init__(
        self,
        account_id: Incomplete | None = None,
        name: Incomplete | None = None,
        email: Incomplete | None = None,
        email_verified: Incomplete | None = None,
        disabled: Incomplete | None = None,
        profile_photo_url: Incomplete | None = None,
    ) -> None: ...

Account_validator: Incomplete

class BasicAccount(Account):
    is_teammate: Incomplete
    team_member_id: Incomplete
    def __init__(
        self,
        account_id: Incomplete | None = None,
        name: Incomplete | None = None,
        email: Incomplete | None = None,
        email_verified: Incomplete | None = None,
        disabled: Incomplete | None = None,
        is_teammate: Incomplete | None = None,
        profile_photo_url: Incomplete | None = None,
        team_member_id: Incomplete | None = None,
    ) -> None: ...

BasicAccount_validator: Incomplete

class FileLockingValue(bb.Union):
    other: Incomplete
    @classmethod
    def enabled(cls, val): ...
    def is_enabled(self): ...
    def is_other(self): ...
    def get_enabled(self): ...

FileLockingValue_validator: Incomplete

class FullAccount(Account):
    country: Incomplete
    locale: Incomplete
    referral_link: Incomplete
    team: Incomplete
    team_member_id: Incomplete
    is_paired: Incomplete
    account_type: Incomplete
    root_info: Incomplete
    def __init__(
        self,
        account_id: Incomplete | None = None,
        name: Incomplete | None = None,
        email: Incomplete | None = None,
        email_verified: Incomplete | None = None,
        disabled: Incomplete | None = None,
        locale: Incomplete | None = None,
        referral_link: Incomplete | None = None,
        is_paired: Incomplete | None = None,
        account_type: Incomplete | None = None,
        root_info: Incomplete | None = None,
        profile_photo_url: Incomplete | None = None,
        country: Incomplete | None = None,
        team: Incomplete | None = None,
        team_member_id: Incomplete | None = None,
    ) -> None: ...

FullAccount_validator: Incomplete

class Team(bb.Struct):
    id: Incomplete
    name: Incomplete
    def __init__(self, id: Incomplete | None = None, name: Incomplete | None = None) -> None: ...

Team_validator: Incomplete

class FullTeam(Team):
    sharing_policies: Incomplete
    office_addin_policy: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        name: Incomplete | None = None,
        sharing_policies: Incomplete | None = None,
        office_addin_policy: Incomplete | None = None,
    ) -> None: ...

FullTeam_validator: Incomplete

class GetAccountArg(bb.Struct):
    account_id: Incomplete
    def __init__(self, account_id: Incomplete | None = None) -> None: ...

GetAccountArg_validator: Incomplete

class GetAccountBatchArg(bb.Struct):
    account_ids: Incomplete
    def __init__(self, account_ids: Incomplete | None = None) -> None: ...

GetAccountBatchArg_validator: Incomplete

class GetAccountBatchError(bb.Union):
    other: Incomplete
    @classmethod
    def no_account(cls, val): ...
    def is_no_account(self): ...
    def is_other(self): ...
    def get_no_account(self): ...

GetAccountBatchError_validator: Incomplete

class GetAccountError(bb.Union):
    no_account: Incomplete
    other: Incomplete
    def is_no_account(self): ...
    def is_other(self): ...

GetAccountError_validator: Incomplete

class IndividualSpaceAllocation(bb.Struct):
    allocated: Incomplete
    def __init__(self, allocated: Incomplete | None = None) -> None: ...

IndividualSpaceAllocation_validator: Incomplete

class Name(bb.Struct):
    given_name: Incomplete
    surname: Incomplete
    familiar_name: Incomplete
    display_name: Incomplete
    abbreviated_name: Incomplete
    def __init__(
        self,
        given_name: Incomplete | None = None,
        surname: Incomplete | None = None,
        familiar_name: Incomplete | None = None,
        display_name: Incomplete | None = None,
        abbreviated_name: Incomplete | None = None,
    ) -> None: ...

Name_validator: Incomplete

class PaperAsFilesValue(bb.Union):
    other: Incomplete
    @classmethod
    def enabled(cls, val): ...
    def is_enabled(self): ...
    def is_other(self): ...
    def get_enabled(self): ...

PaperAsFilesValue_validator: Incomplete

class SpaceAllocation(bb.Union):
    other: Incomplete
    @classmethod
    def individual(cls, val): ...
    @classmethod
    def team(cls, val): ...
    def is_individual(self): ...
    def is_team(self): ...
    def is_other(self): ...
    def get_individual(self): ...
    def get_team(self): ...

SpaceAllocation_validator: Incomplete

class SpaceUsage(bb.Struct):
    used: Incomplete
    allocation: Incomplete
    def __init__(self, used: Incomplete | None = None, allocation: Incomplete | None = None) -> None: ...

SpaceUsage_validator: Incomplete

class TeamSpaceAllocation(bb.Struct):
    used: Incomplete
    allocated: Incomplete
    user_within_team_space_allocated: Incomplete
    user_within_team_space_limit_type: Incomplete
    user_within_team_space_used_cached: Incomplete
    def __init__(
        self,
        used: Incomplete | None = None,
        allocated: Incomplete | None = None,
        user_within_team_space_allocated: Incomplete | None = None,
        user_within_team_space_limit_type: Incomplete | None = None,
        user_within_team_space_used_cached: Incomplete | None = None,
    ) -> None: ...

TeamSpaceAllocation_validator: Incomplete

class UserFeature(bb.Union):
    paper_as_files: Incomplete
    file_locking: Incomplete
    other: Incomplete
    def is_paper_as_files(self): ...
    def is_file_locking(self): ...
    def is_other(self): ...

UserFeature_validator: Incomplete

class UserFeatureValue(bb.Union):
    other: Incomplete
    @classmethod
    def paper_as_files(cls, val): ...
    @classmethod
    def file_locking(cls, val): ...
    def is_paper_as_files(self): ...
    def is_file_locking(self): ...
    def is_other(self): ...
    def get_paper_as_files(self): ...
    def get_file_locking(self): ...

UserFeatureValue_validator: Incomplete

class UserFeaturesGetValuesBatchArg(bb.Struct):
    features: Incomplete
    def __init__(self, features: Incomplete | None = None) -> None: ...

UserFeaturesGetValuesBatchArg_validator: Incomplete

class UserFeaturesGetValuesBatchError(bb.Union):
    empty_features_list: Incomplete
    other: Incomplete
    def is_empty_features_list(self): ...
    def is_other(self): ...

UserFeaturesGetValuesBatchError_validator: Incomplete

class UserFeaturesGetValuesBatchResult(bb.Struct):
    values: Incomplete
    def __init__(self, values: Incomplete | None = None) -> None: ...

UserFeaturesGetValuesBatchResult_validator: Incomplete
GetAccountBatchResult_validator: Incomplete
features_get_values: Incomplete
get_account: Incomplete
get_account_batch: Incomplete
get_current_account: Incomplete
get_space_usage: Incomplete
ROUTES: Incomplete
