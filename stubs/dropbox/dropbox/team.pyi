from _typeshed import Incomplete

from dropbox import async_, team_common
from stone.backends.python_rsrc import stone_base as bb

class DeviceSession(bb.Struct):
    session_id: Incomplete
    ip_address: Incomplete
    country: Incomplete
    created: Incomplete
    updated: Incomplete
    def __init__(
        self,
        session_id: Incomplete | None = None,
        ip_address: Incomplete | None = None,
        country: Incomplete | None = None,
        created: Incomplete | None = None,
        updated: Incomplete | None = None,
    ) -> None: ...

DeviceSession_validator: Incomplete

class ActiveWebSession(DeviceSession):
    user_agent: Incomplete
    os: Incomplete
    browser: Incomplete
    expires: Incomplete
    def __init__(
        self,
        session_id: Incomplete | None = None,
        user_agent: Incomplete | None = None,
        os: Incomplete | None = None,
        browser: Incomplete | None = None,
        ip_address: Incomplete | None = None,
        country: Incomplete | None = None,
        created: Incomplete | None = None,
        updated: Incomplete | None = None,
        expires: Incomplete | None = None,
    ) -> None: ...

ActiveWebSession_validator: Incomplete

class AddSecondaryEmailResult(bb.Union):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    @classmethod
    def unavailable(cls, val): ...
    @classmethod
    def already_pending(cls, val): ...
    @classmethod
    def already_owned_by_user(cls, val): ...
    @classmethod
    def reached_limit(cls, val): ...
    @classmethod
    def transient_error(cls, val): ...
    @classmethod
    def too_many_updates(cls, val): ...
    @classmethod
    def unknown_error(cls, val): ...
    @classmethod
    def rate_limited(cls, val): ...
    def is_success(self): ...
    def is_unavailable(self): ...
    def is_already_pending(self): ...
    def is_already_owned_by_user(self): ...
    def is_reached_limit(self): ...
    def is_transient_error(self): ...
    def is_too_many_updates(self): ...
    def is_unknown_error(self): ...
    def is_rate_limited(self): ...
    def is_other(self): ...
    def get_success(self): ...
    def get_unavailable(self): ...
    def get_already_pending(self): ...
    def get_already_owned_by_user(self): ...
    def get_reached_limit(self): ...
    def get_transient_error(self): ...
    def get_too_many_updates(self): ...
    def get_unknown_error(self): ...
    def get_rate_limited(self): ...

AddSecondaryEmailResult_validator: Incomplete

class AddSecondaryEmailsArg(bb.Struct):
    new_secondary_emails: Incomplete
    def __init__(self, new_secondary_emails: Incomplete | None = None) -> None: ...

AddSecondaryEmailsArg_validator: Incomplete

class AddSecondaryEmailsError(bb.Union):
    secondary_emails_disabled: Incomplete
    too_many_emails: Incomplete
    other: Incomplete
    def is_secondary_emails_disabled(self): ...
    def is_too_many_emails(self): ...
    def is_other(self): ...

AddSecondaryEmailsError_validator: Incomplete

class AddSecondaryEmailsResult(bb.Struct):
    results: Incomplete
    def __init__(self, results: Incomplete | None = None) -> None: ...

AddSecondaryEmailsResult_validator: Incomplete

class AdminTier(bb.Union):
    team_admin: Incomplete
    user_management_admin: Incomplete
    support_admin: Incomplete
    member_only: Incomplete
    def is_team_admin(self): ...
    def is_user_management_admin(self): ...
    def is_support_admin(self): ...
    def is_member_only(self): ...

AdminTier_validator: Incomplete

class ApiApp(bb.Struct):
    app_id: Incomplete
    app_name: Incomplete
    publisher: Incomplete
    publisher_url: Incomplete
    linked: Incomplete
    is_app_folder: Incomplete
    def __init__(
        self,
        app_id: Incomplete | None = None,
        app_name: Incomplete | None = None,
        is_app_folder: Incomplete | None = None,
        publisher: Incomplete | None = None,
        publisher_url: Incomplete | None = None,
        linked: Incomplete | None = None,
    ) -> None: ...

ApiApp_validator: Incomplete

class BaseDfbReport(bb.Struct):
    start_date: Incomplete
    def __init__(self, start_date: Incomplete | None = None) -> None: ...

BaseDfbReport_validator: Incomplete

class BaseTeamFolderError(bb.Union):
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    @classmethod
    def status_error(cls, val): ...
    @classmethod
    def team_shared_dropbox_error(cls, val): ...
    def is_access_error(self): ...
    def is_status_error(self): ...
    def is_team_shared_dropbox_error(self): ...
    def is_other(self): ...
    def get_access_error(self): ...
    def get_status_error(self): ...
    def get_team_shared_dropbox_error(self): ...

BaseTeamFolderError_validator: Incomplete

class CustomQuotaError(bb.Union):
    too_many_users: Incomplete
    other: Incomplete
    def is_too_many_users(self): ...
    def is_other(self): ...

CustomQuotaError_validator: Incomplete

class CustomQuotaResult(bb.Union):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    @classmethod
    def invalid_user(cls, val): ...
    def is_success(self): ...
    def is_invalid_user(self): ...
    def is_other(self): ...
    def get_success(self): ...
    def get_invalid_user(self): ...

CustomQuotaResult_validator: Incomplete

class CustomQuotaUsersArg(bb.Struct):
    users: Incomplete
    def __init__(self, users: Incomplete | None = None) -> None: ...

CustomQuotaUsersArg_validator: Incomplete

class DateRange(bb.Struct):
    start_date: Incomplete
    end_date: Incomplete
    def __init__(self, start_date: Incomplete | None = None, end_date: Incomplete | None = None) -> None: ...

DateRange_validator: Incomplete

class DateRangeError(bb.Union):
    other: Incomplete
    def is_other(self): ...

DateRangeError_validator: Incomplete

class DeleteSecondaryEmailResult(bb.Union):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    @classmethod
    def not_found(cls, val): ...
    @classmethod
    def cannot_remove_primary(cls, val): ...
    def is_success(self): ...
    def is_not_found(self): ...
    def is_cannot_remove_primary(self): ...
    def is_other(self): ...
    def get_success(self): ...
    def get_not_found(self): ...
    def get_cannot_remove_primary(self): ...

DeleteSecondaryEmailResult_validator: Incomplete

class DeleteSecondaryEmailsArg(bb.Struct):
    emails_to_delete: Incomplete
    def __init__(self, emails_to_delete: Incomplete | None = None) -> None: ...

DeleteSecondaryEmailsArg_validator: Incomplete

class DeleteSecondaryEmailsResult(bb.Struct):
    results: Incomplete
    def __init__(self, results: Incomplete | None = None) -> None: ...

DeleteSecondaryEmailsResult_validator: Incomplete

class DesktopClientSession(DeviceSession):
    host_name: Incomplete
    client_type: Incomplete
    client_version: Incomplete
    platform: Incomplete
    is_delete_on_unlink_supported: Incomplete
    def __init__(
        self,
        session_id: Incomplete | None = None,
        host_name: Incomplete | None = None,
        client_type: Incomplete | None = None,
        client_version: Incomplete | None = None,
        platform: Incomplete | None = None,
        is_delete_on_unlink_supported: Incomplete | None = None,
        ip_address: Incomplete | None = None,
        country: Incomplete | None = None,
        created: Incomplete | None = None,
        updated: Incomplete | None = None,
    ) -> None: ...

DesktopClientSession_validator: Incomplete

class DesktopPlatform(bb.Union):
    windows: Incomplete
    mac: Incomplete
    linux: Incomplete
    other: Incomplete
    def is_windows(self): ...
    def is_mac(self): ...
    def is_linux(self): ...
    def is_other(self): ...

DesktopPlatform_validator: Incomplete

class DeviceSessionArg(bb.Struct):
    session_id: Incomplete
    team_member_id: Incomplete
    def __init__(self, session_id: Incomplete | None = None, team_member_id: Incomplete | None = None) -> None: ...

DeviceSessionArg_validator: Incomplete

class DevicesActive(bb.Struct):
    windows: Incomplete
    macos: Incomplete
    linux: Incomplete
    ios: Incomplete
    android: Incomplete
    other: Incomplete
    total: Incomplete
    def __init__(
        self,
        windows: Incomplete | None = None,
        macos: Incomplete | None = None,
        linux: Incomplete | None = None,
        ios: Incomplete | None = None,
        android: Incomplete | None = None,
        other: Incomplete | None = None,
        total: Incomplete | None = None,
    ) -> None: ...

DevicesActive_validator: Incomplete

class ExcludedUsersListArg(bb.Struct):
    limit: Incomplete
    def __init__(self, limit: Incomplete | None = None) -> None: ...

ExcludedUsersListArg_validator: Incomplete

class ExcludedUsersListContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

ExcludedUsersListContinueArg_validator: Incomplete

class ExcludedUsersListContinueError(bb.Union):
    invalid_cursor: Incomplete
    other: Incomplete
    def is_invalid_cursor(self): ...
    def is_other(self): ...

ExcludedUsersListContinueError_validator: Incomplete

class ExcludedUsersListError(bb.Union):
    list_error: Incomplete
    other: Incomplete
    def is_list_error(self): ...
    def is_other(self): ...

ExcludedUsersListError_validator: Incomplete

class ExcludedUsersListResult(bb.Struct):
    users: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self, users: Incomplete | None = None, has_more: Incomplete | None = None, cursor: Incomplete | None = None
    ) -> None: ...

ExcludedUsersListResult_validator: Incomplete

class ExcludedUsersUpdateArg(bb.Struct):
    users: Incomplete
    def __init__(self, users: Incomplete | None = None) -> None: ...

ExcludedUsersUpdateArg_validator: Incomplete

class ExcludedUsersUpdateError(bb.Union):
    users_not_in_team: Incomplete
    too_many_users: Incomplete
    other: Incomplete
    def is_users_not_in_team(self): ...
    def is_too_many_users(self): ...
    def is_other(self): ...

ExcludedUsersUpdateError_validator: Incomplete

class ExcludedUsersUpdateResult(bb.Struct):
    status: Incomplete
    def __init__(self, status: Incomplete | None = None) -> None: ...

ExcludedUsersUpdateResult_validator: Incomplete

class ExcludedUsersUpdateStatus(bb.Union):
    success: Incomplete
    other: Incomplete
    def is_success(self): ...
    def is_other(self): ...

ExcludedUsersUpdateStatus_validator: Incomplete

class Feature(bb.Union):
    upload_api_rate_limit: Incomplete
    has_team_shared_dropbox: Incomplete
    has_team_file_events: Incomplete
    has_team_selective_sync: Incomplete
    other: Incomplete
    def is_upload_api_rate_limit(self): ...
    def is_has_team_shared_dropbox(self): ...
    def is_has_team_file_events(self): ...
    def is_has_team_selective_sync(self): ...
    def is_other(self): ...

Feature_validator: Incomplete

class FeatureValue(bb.Union):
    other: Incomplete
    @classmethod
    def upload_api_rate_limit(cls, val): ...
    @classmethod
    def has_team_shared_dropbox(cls, val): ...
    @classmethod
    def has_team_file_events(cls, val): ...
    @classmethod
    def has_team_selective_sync(cls, val): ...
    def is_upload_api_rate_limit(self): ...
    def is_has_team_shared_dropbox(self): ...
    def is_has_team_file_events(self): ...
    def is_has_team_selective_sync(self): ...
    def is_other(self): ...
    def get_upload_api_rate_limit(self): ...
    def get_has_team_shared_dropbox(self): ...
    def get_has_team_file_events(self): ...
    def get_has_team_selective_sync(self): ...

FeatureValue_validator: Incomplete

class FeaturesGetValuesBatchArg(bb.Struct):
    features: Incomplete
    def __init__(self, features: Incomplete | None = None) -> None: ...

FeaturesGetValuesBatchArg_validator: Incomplete

class FeaturesGetValuesBatchError(bb.Union):
    empty_features_list: Incomplete
    other: Incomplete
    def is_empty_features_list(self): ...
    def is_other(self): ...

FeaturesGetValuesBatchError_validator: Incomplete

class FeaturesGetValuesBatchResult(bb.Struct):
    values: Incomplete
    def __init__(self, values: Incomplete | None = None) -> None: ...

FeaturesGetValuesBatchResult_validator: Incomplete

class GetActivityReport(BaseDfbReport):
    adds: Incomplete
    edits: Incomplete
    deletes: Incomplete
    active_users_28_day: Incomplete
    active_users_7_day: Incomplete
    active_users_1_day: Incomplete
    active_shared_folders_28_day: Incomplete
    active_shared_folders_7_day: Incomplete
    active_shared_folders_1_day: Incomplete
    shared_links_created: Incomplete
    shared_links_viewed_by_team: Incomplete
    shared_links_viewed_by_outside_user: Incomplete
    shared_links_viewed_by_not_logged_in: Incomplete
    shared_links_viewed_total: Incomplete
    def __init__(
        self,
        start_date: Incomplete | None = None,
        adds: Incomplete | None = None,
        edits: Incomplete | None = None,
        deletes: Incomplete | None = None,
        active_users_28_day: Incomplete | None = None,
        active_users_7_day: Incomplete | None = None,
        active_users_1_day: Incomplete | None = None,
        active_shared_folders_28_day: Incomplete | None = None,
        active_shared_folders_7_day: Incomplete | None = None,
        active_shared_folders_1_day: Incomplete | None = None,
        shared_links_created: Incomplete | None = None,
        shared_links_viewed_by_team: Incomplete | None = None,
        shared_links_viewed_by_outside_user: Incomplete | None = None,
        shared_links_viewed_by_not_logged_in: Incomplete | None = None,
        shared_links_viewed_total: Incomplete | None = None,
    ) -> None: ...

GetActivityReport_validator: Incomplete

class GetDevicesReport(BaseDfbReport):
    active_1_day: Incomplete
    active_7_day: Incomplete
    active_28_day: Incomplete
    def __init__(
        self,
        start_date: Incomplete | None = None,
        active_1_day: Incomplete | None = None,
        active_7_day: Incomplete | None = None,
        active_28_day: Incomplete | None = None,
    ) -> None: ...

GetDevicesReport_validator: Incomplete

class GetMembershipReport(BaseDfbReport):
    team_size: Incomplete
    pending_invites: Incomplete
    members_joined: Incomplete
    suspended_members: Incomplete
    licenses: Incomplete
    def __init__(
        self,
        start_date: Incomplete | None = None,
        team_size: Incomplete | None = None,
        pending_invites: Incomplete | None = None,
        members_joined: Incomplete | None = None,
        suspended_members: Incomplete | None = None,
        licenses: Incomplete | None = None,
    ) -> None: ...

GetMembershipReport_validator: Incomplete

class GetStorageReport(BaseDfbReport):
    total_usage: Incomplete
    shared_usage: Incomplete
    unshared_usage: Incomplete
    shared_folders: Incomplete
    member_storage_map: Incomplete
    def __init__(
        self,
        start_date: Incomplete | None = None,
        total_usage: Incomplete | None = None,
        shared_usage: Incomplete | None = None,
        unshared_usage: Incomplete | None = None,
        shared_folders: Incomplete | None = None,
        member_storage_map: Incomplete | None = None,
    ) -> None: ...

GetStorageReport_validator: Incomplete

class GroupAccessType(bb.Union):
    member: Incomplete
    owner: Incomplete
    def is_member(self): ...
    def is_owner(self): ...

GroupAccessType_validator: Incomplete

class GroupCreateArg(bb.Struct):
    group_name: Incomplete
    add_creator_as_owner: Incomplete
    group_external_id: Incomplete
    group_management_type: Incomplete
    def __init__(
        self,
        group_name: Incomplete | None = None,
        add_creator_as_owner: Incomplete | None = None,
        group_external_id: Incomplete | None = None,
        group_management_type: Incomplete | None = None,
    ) -> None: ...

GroupCreateArg_validator: Incomplete

class GroupCreateError(bb.Union):
    group_name_already_used: Incomplete
    group_name_invalid: Incomplete
    external_id_already_in_use: Incomplete
    system_managed_group_disallowed: Incomplete
    other: Incomplete
    def is_group_name_already_used(self): ...
    def is_group_name_invalid(self): ...
    def is_external_id_already_in_use(self): ...
    def is_system_managed_group_disallowed(self): ...
    def is_other(self): ...

GroupCreateError_validator: Incomplete

class GroupSelectorError(bb.Union):
    group_not_found: Incomplete
    other: Incomplete
    def is_group_not_found(self): ...
    def is_other(self): ...

GroupSelectorError_validator: Incomplete

class GroupSelectorWithTeamGroupError(GroupSelectorError):
    system_managed_group_disallowed: Incomplete
    def is_system_managed_group_disallowed(self): ...

GroupSelectorWithTeamGroupError_validator: Incomplete

class GroupDeleteError(GroupSelectorWithTeamGroupError):
    group_already_deleted: Incomplete
    def is_group_already_deleted(self): ...

GroupDeleteError_validator: Incomplete

class GroupFullInfo(team_common.GroupSummary):
    members: Incomplete
    created: Incomplete
    def __init__(
        self,
        group_name: Incomplete | None = None,
        group_id: Incomplete | None = None,
        group_management_type: Incomplete | None = None,
        created: Incomplete | None = None,
        group_external_id: Incomplete | None = None,
        member_count: Incomplete | None = None,
        members: Incomplete | None = None,
    ) -> None: ...

GroupFullInfo_validator: Incomplete

class GroupMemberInfo(bb.Struct):
    profile: Incomplete
    access_type: Incomplete
    def __init__(self, profile: Incomplete | None = None, access_type: Incomplete | None = None) -> None: ...

GroupMemberInfo_validator: Incomplete

class GroupMemberSelector(bb.Struct):
    group: Incomplete
    user: Incomplete
    def __init__(self, group: Incomplete | None = None, user: Incomplete | None = None) -> None: ...

GroupMemberSelector_validator: Incomplete

class GroupMemberSelectorError(GroupSelectorWithTeamGroupError):
    member_not_in_group: Incomplete
    def is_member_not_in_group(self): ...

GroupMemberSelectorError_validator: Incomplete

class GroupMemberSetAccessTypeError(GroupMemberSelectorError):
    user_cannot_be_manager_of_company_managed_group: Incomplete
    def is_user_cannot_be_manager_of_company_managed_group(self): ...

GroupMemberSetAccessTypeError_validator: Incomplete

class IncludeMembersArg(bb.Struct):
    return_members: Incomplete
    def __init__(self, return_members: Incomplete | None = None) -> None: ...

IncludeMembersArg_validator: Incomplete

class GroupMembersAddArg(IncludeMembersArg):
    group: Incomplete
    members: Incomplete
    def __init__(
        self, group: Incomplete | None = None, members: Incomplete | None = None, return_members: Incomplete | None = None
    ) -> None: ...

GroupMembersAddArg_validator: Incomplete

class GroupMembersAddError(GroupSelectorWithTeamGroupError):
    duplicate_user: Incomplete
    group_not_in_team: Incomplete
    user_must_be_active_to_be_owner: Incomplete
    @classmethod
    def members_not_in_team(cls, val): ...
    @classmethod
    def users_not_found(cls, val): ...
    @classmethod
    def user_cannot_be_manager_of_company_managed_group(cls, val): ...
    def is_duplicate_user(self): ...
    def is_group_not_in_team(self): ...
    def is_members_not_in_team(self): ...
    def is_users_not_found(self): ...
    def is_user_must_be_active_to_be_owner(self): ...
    def is_user_cannot_be_manager_of_company_managed_group(self): ...
    def get_members_not_in_team(self): ...
    def get_users_not_found(self): ...
    def get_user_cannot_be_manager_of_company_managed_group(self): ...

GroupMembersAddError_validator: Incomplete

class GroupMembersChangeResult(bb.Struct):
    group_info: Incomplete
    async_job_id: Incomplete
    def __init__(self, group_info: Incomplete | None = None, async_job_id: Incomplete | None = None) -> None: ...

GroupMembersChangeResult_validator: Incomplete

class GroupMembersRemoveArg(IncludeMembersArg):
    group: Incomplete
    users: Incomplete
    def __init__(
        self, group: Incomplete | None = None, users: Incomplete | None = None, return_members: Incomplete | None = None
    ) -> None: ...

GroupMembersRemoveArg_validator: Incomplete

class GroupMembersSelectorError(GroupSelectorWithTeamGroupError):
    member_not_in_group: Incomplete
    def is_member_not_in_group(self): ...

GroupMembersSelectorError_validator: Incomplete

class GroupMembersRemoveError(GroupMembersSelectorError):
    group_not_in_team: Incomplete
    @classmethod
    def members_not_in_team(cls, val): ...
    @classmethod
    def users_not_found(cls, val): ...
    def is_group_not_in_team(self): ...
    def is_members_not_in_team(self): ...
    def is_users_not_found(self): ...
    def get_members_not_in_team(self): ...
    def get_users_not_found(self): ...

GroupMembersRemoveError_validator: Incomplete

class GroupMembersSelector(bb.Struct):
    group: Incomplete
    users: Incomplete
    def __init__(self, group: Incomplete | None = None, users: Incomplete | None = None) -> None: ...

GroupMembersSelector_validator: Incomplete

class GroupMembersSetAccessTypeArg(GroupMemberSelector):
    access_type: Incomplete
    return_members: Incomplete
    def __init__(
        self,
        group: Incomplete | None = None,
        user: Incomplete | None = None,
        access_type: Incomplete | None = None,
        return_members: Incomplete | None = None,
    ) -> None: ...

GroupMembersSetAccessTypeArg_validator: Incomplete

class GroupSelector(bb.Union):
    @classmethod
    def group_id(cls, val): ...
    @classmethod
    def group_external_id(cls, val): ...
    def is_group_id(self): ...
    def is_group_external_id(self): ...
    def get_group_id(self): ...
    def get_group_external_id(self): ...

GroupSelector_validator: Incomplete

class GroupUpdateArgs(IncludeMembersArg):
    group: Incomplete
    new_group_name: Incomplete
    new_group_external_id: Incomplete
    new_group_management_type: Incomplete
    def __init__(
        self,
        group: Incomplete | None = None,
        return_members: Incomplete | None = None,
        new_group_name: Incomplete | None = None,
        new_group_external_id: Incomplete | None = None,
        new_group_management_type: Incomplete | None = None,
    ) -> None: ...

GroupUpdateArgs_validator: Incomplete

class GroupUpdateError(GroupSelectorWithTeamGroupError):
    group_name_already_used: Incomplete
    group_name_invalid: Incomplete
    external_id_already_in_use: Incomplete
    def is_group_name_already_used(self): ...
    def is_group_name_invalid(self): ...
    def is_external_id_already_in_use(self): ...

GroupUpdateError_validator: Incomplete

class GroupsGetInfoError(bb.Union):
    group_not_on_team: Incomplete
    other: Incomplete
    def is_group_not_on_team(self): ...
    def is_other(self): ...

GroupsGetInfoError_validator: Incomplete

class GroupsGetInfoItem(bb.Union):
    @classmethod
    def id_not_found(cls, val): ...
    @classmethod
    def group_info(cls, val): ...
    def is_id_not_found(self): ...
    def is_group_info(self): ...
    def get_id_not_found(self): ...
    def get_group_info(self): ...

GroupsGetInfoItem_validator: Incomplete

class GroupsListArg(bb.Struct):
    limit: Incomplete
    def __init__(self, limit: Incomplete | None = None) -> None: ...

GroupsListArg_validator: Incomplete

class GroupsListContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

GroupsListContinueArg_validator: Incomplete

class GroupsListContinueError(bb.Union):
    invalid_cursor: Incomplete
    other: Incomplete
    def is_invalid_cursor(self): ...
    def is_other(self): ...

GroupsListContinueError_validator: Incomplete

class GroupsListResult(bb.Struct):
    groups: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self, groups: Incomplete | None = None, cursor: Incomplete | None = None, has_more: Incomplete | None = None
    ) -> None: ...

GroupsListResult_validator: Incomplete

class GroupsMembersListArg(bb.Struct):
    group: Incomplete
    limit: Incomplete
    def __init__(self, group: Incomplete | None = None, limit: Incomplete | None = None) -> None: ...

GroupsMembersListArg_validator: Incomplete

class GroupsMembersListContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

GroupsMembersListContinueArg_validator: Incomplete

class GroupsMembersListContinueError(bb.Union):
    invalid_cursor: Incomplete
    other: Incomplete
    def is_invalid_cursor(self): ...
    def is_other(self): ...

GroupsMembersListContinueError_validator: Incomplete

class GroupsMembersListResult(bb.Struct):
    members: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self, members: Incomplete | None = None, cursor: Incomplete | None = None, has_more: Incomplete | None = None
    ) -> None: ...

GroupsMembersListResult_validator: Incomplete

class GroupsPollError(async_.PollError):
    access_denied: Incomplete
    def is_access_denied(self): ...

GroupsPollError_validator: Incomplete

class GroupsSelector(bb.Union):
    @classmethod
    def group_ids(cls, val): ...
    @classmethod
    def group_external_ids(cls, val): ...
    def is_group_ids(self): ...
    def is_group_external_ids(self): ...
    def get_group_ids(self): ...
    def get_group_external_ids(self): ...

GroupsSelector_validator: Incomplete

class HasTeamFileEventsValue(bb.Union):
    other: Incomplete
    @classmethod
    def enabled(cls, val): ...
    def is_enabled(self): ...
    def is_other(self): ...
    def get_enabled(self): ...

HasTeamFileEventsValue_validator: Incomplete

class HasTeamSelectiveSyncValue(bb.Union):
    other: Incomplete
    @classmethod
    def has_team_selective_sync(cls, val): ...
    def is_has_team_selective_sync(self): ...
    def is_other(self): ...
    def get_has_team_selective_sync(self): ...

HasTeamSelectiveSyncValue_validator: Incomplete

class HasTeamSharedDropboxValue(bb.Union):
    other: Incomplete
    @classmethod
    def has_team_shared_dropbox(cls, val): ...
    def is_has_team_shared_dropbox(self): ...
    def is_other(self): ...
    def get_has_team_shared_dropbox(self): ...

HasTeamSharedDropboxValue_validator: Incomplete

class LegalHoldHeldRevisionMetadata(bb.Struct):
    new_filename: Incomplete
    original_revision_id: Incomplete
    original_file_path: Incomplete
    server_modified: Incomplete
    author_member_id: Incomplete
    author_member_status: Incomplete
    author_email: Incomplete
    file_type: Incomplete
    size: Incomplete
    content_hash: Incomplete
    def __init__(
        self,
        new_filename: Incomplete | None = None,
        original_revision_id: Incomplete | None = None,
        original_file_path: Incomplete | None = None,
        server_modified: Incomplete | None = None,
        author_member_id: Incomplete | None = None,
        author_member_status: Incomplete | None = None,
        author_email: Incomplete | None = None,
        file_type: Incomplete | None = None,
        size: Incomplete | None = None,
        content_hash: Incomplete | None = None,
    ) -> None: ...

LegalHoldHeldRevisionMetadata_validator: Incomplete

class LegalHoldPolicy(bb.Struct):
    id: Incomplete
    name: Incomplete
    description: Incomplete
    activation_time: Incomplete
    members: Incomplete
    status: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        name: Incomplete | None = None,
        members: Incomplete | None = None,
        status: Incomplete | None = None,
        start_date: Incomplete | None = None,
        description: Incomplete | None = None,
        activation_time: Incomplete | None = None,
        end_date: Incomplete | None = None,
    ) -> None: ...

LegalHoldPolicy_validator: Incomplete

class LegalHoldStatus(bb.Union):
    active: Incomplete
    released: Incomplete
    activating: Incomplete
    updating: Incomplete
    exporting: Incomplete
    releasing: Incomplete
    other: Incomplete
    def is_active(self): ...
    def is_released(self): ...
    def is_activating(self): ...
    def is_updating(self): ...
    def is_exporting(self): ...
    def is_releasing(self): ...
    def is_other(self): ...

LegalHoldStatus_validator: Incomplete

class LegalHoldsError(bb.Union):
    unknown_legal_hold_error: Incomplete
    insufficient_permissions: Incomplete
    other: Incomplete
    def is_unknown_legal_hold_error(self): ...
    def is_insufficient_permissions(self): ...
    def is_other(self): ...

LegalHoldsError_validator: Incomplete

class LegalHoldsGetPolicyArg(bb.Struct):
    id: Incomplete
    def __init__(self, id: Incomplete | None = None) -> None: ...

LegalHoldsGetPolicyArg_validator: Incomplete

class LegalHoldsGetPolicyError(LegalHoldsError):
    legal_hold_policy_not_found: Incomplete
    def is_legal_hold_policy_not_found(self): ...

LegalHoldsGetPolicyError_validator: Incomplete

class LegalHoldsListHeldRevisionResult(bb.Struct):
    entries: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self, entries: Incomplete | None = None, has_more: Incomplete | None = None, cursor: Incomplete | None = None
    ) -> None: ...

LegalHoldsListHeldRevisionResult_validator: Incomplete

class LegalHoldsListHeldRevisionsArg(bb.Struct):
    id: Incomplete
    def __init__(self, id: Incomplete | None = None) -> None: ...

LegalHoldsListHeldRevisionsArg_validator: Incomplete

class LegalHoldsListHeldRevisionsContinueArg(bb.Struct):
    id: Incomplete
    cursor: Incomplete
    def __init__(self, id: Incomplete | None = None, cursor: Incomplete | None = None) -> None: ...

LegalHoldsListHeldRevisionsContinueArg_validator: Incomplete

class LegalHoldsListHeldRevisionsContinueError(bb.Union):
    unknown_legal_hold_error: Incomplete
    transient_error: Incomplete
    reset: Incomplete
    other: Incomplete
    def is_unknown_legal_hold_error(self): ...
    def is_transient_error(self): ...
    def is_reset(self): ...
    def is_other(self): ...

LegalHoldsListHeldRevisionsContinueError_validator: Incomplete

class LegalHoldsListHeldRevisionsError(LegalHoldsError):
    transient_error: Incomplete
    legal_hold_still_empty: Incomplete
    inactive_legal_hold: Incomplete
    def is_transient_error(self): ...
    def is_legal_hold_still_empty(self): ...
    def is_inactive_legal_hold(self): ...

LegalHoldsListHeldRevisionsError_validator: Incomplete

class LegalHoldsListPoliciesArg(bb.Struct):
    include_released: Incomplete
    def __init__(self, include_released: Incomplete | None = None) -> None: ...

LegalHoldsListPoliciesArg_validator: Incomplete

class LegalHoldsListPoliciesError(LegalHoldsError):
    transient_error: Incomplete
    def is_transient_error(self): ...

LegalHoldsListPoliciesError_validator: Incomplete

class LegalHoldsListPoliciesResult(bb.Struct):
    policies: Incomplete
    def __init__(self, policies: Incomplete | None = None) -> None: ...

LegalHoldsListPoliciesResult_validator: Incomplete

class LegalHoldsPolicyCreateArg(bb.Struct):
    name: Incomplete
    description: Incomplete
    members: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        members: Incomplete | None = None,
        description: Incomplete | None = None,
        start_date: Incomplete | None = None,
        end_date: Incomplete | None = None,
    ) -> None: ...

LegalHoldsPolicyCreateArg_validator: Incomplete

class LegalHoldsPolicyCreateError(LegalHoldsError):
    start_date_is_later_than_end_date: Incomplete
    empty_members_list: Incomplete
    invalid_members: Incomplete
    number_of_users_on_hold_is_greater_than_hold_limitation: Incomplete
    transient_error: Incomplete
    name_must_be_unique: Incomplete
    team_exceeded_legal_hold_quota: Incomplete
    invalid_date: Incomplete
    def is_start_date_is_later_than_end_date(self): ...
    def is_empty_members_list(self): ...
    def is_invalid_members(self): ...
    def is_number_of_users_on_hold_is_greater_than_hold_limitation(self): ...
    def is_transient_error(self): ...
    def is_name_must_be_unique(self): ...
    def is_team_exceeded_legal_hold_quota(self): ...
    def is_invalid_date(self): ...

LegalHoldsPolicyCreateError_validator: Incomplete

class LegalHoldsPolicyReleaseArg(bb.Struct):
    id: Incomplete
    def __init__(self, id: Incomplete | None = None) -> None: ...

LegalHoldsPolicyReleaseArg_validator: Incomplete

class LegalHoldsPolicyReleaseError(LegalHoldsError):
    legal_hold_performing_another_operation: Incomplete
    legal_hold_already_releasing: Incomplete
    legal_hold_policy_not_found: Incomplete
    def is_legal_hold_performing_another_operation(self): ...
    def is_legal_hold_already_releasing(self): ...
    def is_legal_hold_policy_not_found(self): ...

LegalHoldsPolicyReleaseError_validator: Incomplete

class LegalHoldsPolicyUpdateArg(bb.Struct):
    id: Incomplete
    name: Incomplete
    description: Incomplete
    members: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        members: Incomplete | None = None,
    ) -> None: ...

LegalHoldsPolicyUpdateArg_validator: Incomplete

class LegalHoldsPolicyUpdateError(LegalHoldsError):
    transient_error: Incomplete
    inactive_legal_hold: Incomplete
    legal_hold_performing_another_operation: Incomplete
    invalid_members: Incomplete
    number_of_users_on_hold_is_greater_than_hold_limitation: Incomplete
    empty_members_list: Incomplete
    name_must_be_unique: Incomplete
    legal_hold_policy_not_found: Incomplete
    def is_transient_error(self): ...
    def is_inactive_legal_hold(self): ...
    def is_legal_hold_performing_another_operation(self): ...
    def is_invalid_members(self): ...
    def is_number_of_users_on_hold_is_greater_than_hold_limitation(self): ...
    def is_empty_members_list(self): ...
    def is_name_must_be_unique(self): ...
    def is_legal_hold_policy_not_found(self): ...

LegalHoldsPolicyUpdateError_validator: Incomplete

class ListMemberAppsArg(bb.Struct):
    team_member_id: Incomplete
    def __init__(self, team_member_id: Incomplete | None = None) -> None: ...

ListMemberAppsArg_validator: Incomplete

class ListMemberAppsError(bb.Union):
    member_not_found: Incomplete
    other: Incomplete
    def is_member_not_found(self): ...
    def is_other(self): ...

ListMemberAppsError_validator: Incomplete

class ListMemberAppsResult(bb.Struct):
    linked_api_apps: Incomplete
    def __init__(self, linked_api_apps: Incomplete | None = None) -> None: ...

ListMemberAppsResult_validator: Incomplete

class ListMemberDevicesArg(bb.Struct):
    team_member_id: Incomplete
    include_web_sessions: Incomplete
    include_desktop_clients: Incomplete
    include_mobile_clients: Incomplete
    def __init__(
        self,
        team_member_id: Incomplete | None = None,
        include_web_sessions: Incomplete | None = None,
        include_desktop_clients: Incomplete | None = None,
        include_mobile_clients: Incomplete | None = None,
    ) -> None: ...

ListMemberDevicesArg_validator: Incomplete

class ListMemberDevicesError(bb.Union):
    member_not_found: Incomplete
    other: Incomplete
    def is_member_not_found(self): ...
    def is_other(self): ...

ListMemberDevicesError_validator: Incomplete

class ListMemberDevicesResult(bb.Struct):
    active_web_sessions: Incomplete
    desktop_client_sessions: Incomplete
    mobile_client_sessions: Incomplete
    def __init__(
        self,
        active_web_sessions: Incomplete | None = None,
        desktop_client_sessions: Incomplete | None = None,
        mobile_client_sessions: Incomplete | None = None,
    ) -> None: ...

ListMemberDevicesResult_validator: Incomplete

class ListMembersAppsArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

ListMembersAppsArg_validator: Incomplete

class ListMembersAppsError(bb.Union):
    reset: Incomplete
    other: Incomplete
    def is_reset(self): ...
    def is_other(self): ...

ListMembersAppsError_validator: Incomplete

class ListMembersAppsResult(bb.Struct):
    apps: Incomplete
    has_more: Incomplete
    cursor: Incomplete
    def __init__(
        self, apps: Incomplete | None = None, has_more: Incomplete | None = None, cursor: Incomplete | None = None
    ) -> None: ...

ListMembersAppsResult_validator: Incomplete

class ListMembersDevicesArg(bb.Struct):
    cursor: Incomplete
    include_web_sessions: Incomplete
    include_desktop_clients: Incomplete
    include_mobile_clients: Incomplete
    def __init__(
        self,
        cursor: Incomplete | None = None,
        include_web_sessions: Incomplete | None = None,
        include_desktop_clients: Incomplete | None = None,
        include_mobile_clients: Incomplete | None = None,
    ) -> None: ...

ListMembersDevicesArg_validator: Incomplete

class ListMembersDevicesError(bb.Union):
    reset: Incomplete
    other: Incomplete
    def is_reset(self): ...
    def is_other(self): ...

ListMembersDevicesError_validator: Incomplete

class ListMembersDevicesResult(bb.Struct):
    devices: Incomplete
    has_more: Incomplete
    cursor: Incomplete
    def __init__(
        self, devices: Incomplete | None = None, has_more: Incomplete | None = None, cursor: Incomplete | None = None
    ) -> None: ...

ListMembersDevicesResult_validator: Incomplete

class ListTeamAppsArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

ListTeamAppsArg_validator: Incomplete

class ListTeamAppsError(bb.Union):
    reset: Incomplete
    other: Incomplete
    def is_reset(self): ...
    def is_other(self): ...

ListTeamAppsError_validator: Incomplete

class ListTeamAppsResult(bb.Struct):
    apps: Incomplete
    has_more: Incomplete
    cursor: Incomplete
    def __init__(
        self, apps: Incomplete | None = None, has_more: Incomplete | None = None, cursor: Incomplete | None = None
    ) -> None: ...

ListTeamAppsResult_validator: Incomplete

class ListTeamDevicesArg(bb.Struct):
    cursor: Incomplete
    include_web_sessions: Incomplete
    include_desktop_clients: Incomplete
    include_mobile_clients: Incomplete
    def __init__(
        self,
        cursor: Incomplete | None = None,
        include_web_sessions: Incomplete | None = None,
        include_desktop_clients: Incomplete | None = None,
        include_mobile_clients: Incomplete | None = None,
    ) -> None: ...

ListTeamDevicesArg_validator: Incomplete

class ListTeamDevicesError(bb.Union):
    reset: Incomplete
    other: Incomplete
    def is_reset(self): ...
    def is_other(self): ...

ListTeamDevicesError_validator: Incomplete

class ListTeamDevicesResult(bb.Struct):
    devices: Incomplete
    has_more: Incomplete
    cursor: Incomplete
    def __init__(
        self, devices: Incomplete | None = None, has_more: Incomplete | None = None, cursor: Incomplete | None = None
    ) -> None: ...

ListTeamDevicesResult_validator: Incomplete

class MemberAccess(bb.Struct):
    user: Incomplete
    access_type: Incomplete
    def __init__(self, user: Incomplete | None = None, access_type: Incomplete | None = None) -> None: ...

MemberAccess_validator: Incomplete

class MemberAddArgBase(bb.Struct):
    member_email: Incomplete
    member_given_name: Incomplete
    member_surname: Incomplete
    member_external_id: Incomplete
    member_persistent_id: Incomplete
    send_welcome_email: Incomplete
    is_directory_restricted: Incomplete
    def __init__(
        self,
        member_email: Incomplete | None = None,
        member_given_name: Incomplete | None = None,
        member_surname: Incomplete | None = None,
        member_external_id: Incomplete | None = None,
        member_persistent_id: Incomplete | None = None,
        send_welcome_email: Incomplete | None = None,
        is_directory_restricted: Incomplete | None = None,
    ) -> None: ...

MemberAddArgBase_validator: Incomplete

class MemberAddArg(MemberAddArgBase):
    role: Incomplete
    def __init__(
        self,
        member_email: Incomplete | None = None,
        member_given_name: Incomplete | None = None,
        member_surname: Incomplete | None = None,
        member_external_id: Incomplete | None = None,
        member_persistent_id: Incomplete | None = None,
        send_welcome_email: Incomplete | None = None,
        is_directory_restricted: Incomplete | None = None,
        role: Incomplete | None = None,
    ) -> None: ...

MemberAddArg_validator: Incomplete

class MemberAddResultBase(bb.Union):
    @classmethod
    def team_license_limit(cls, val): ...
    @classmethod
    def free_team_member_limit_reached(cls, val): ...
    @classmethod
    def user_already_on_team(cls, val): ...
    @classmethod
    def user_on_another_team(cls, val): ...
    @classmethod
    def user_already_paired(cls, val): ...
    @classmethod
    def user_migration_failed(cls, val): ...
    @classmethod
    def duplicate_external_member_id(cls, val): ...
    @classmethod
    def duplicate_member_persistent_id(cls, val): ...
    @classmethod
    def persistent_id_disabled(cls, val): ...
    @classmethod
    def user_creation_failed(cls, val): ...
    def is_team_license_limit(self): ...
    def is_free_team_member_limit_reached(self): ...
    def is_user_already_on_team(self): ...
    def is_user_on_another_team(self): ...
    def is_user_already_paired(self): ...
    def is_user_migration_failed(self): ...
    def is_duplicate_external_member_id(self): ...
    def is_duplicate_member_persistent_id(self): ...
    def is_persistent_id_disabled(self): ...
    def is_user_creation_failed(self): ...
    def get_team_license_limit(self): ...
    def get_free_team_member_limit_reached(self): ...
    def get_user_already_on_team(self): ...
    def get_user_on_another_team(self): ...
    def get_user_already_paired(self): ...
    def get_user_migration_failed(self): ...
    def get_duplicate_external_member_id(self): ...
    def get_duplicate_member_persistent_id(self): ...
    def get_persistent_id_disabled(self): ...
    def get_user_creation_failed(self): ...

MemberAddResultBase_validator: Incomplete

class MemberAddResult(MemberAddResultBase):
    @classmethod
    def success(cls, val): ...
    def is_success(self): ...
    def get_success(self): ...

MemberAddResult_validator: Incomplete

class MemberAddV2Arg(MemberAddArgBase):
    role_ids: Incomplete
    def __init__(
        self,
        member_email: Incomplete | None = None,
        member_given_name: Incomplete | None = None,
        member_surname: Incomplete | None = None,
        member_external_id: Incomplete | None = None,
        member_persistent_id: Incomplete | None = None,
        send_welcome_email: Incomplete | None = None,
        is_directory_restricted: Incomplete | None = None,
        role_ids: Incomplete | None = None,
    ) -> None: ...

MemberAddV2Arg_validator: Incomplete

class MemberAddV2Result(MemberAddResultBase):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    def is_success(self): ...
    def is_other(self): ...
    def get_success(self): ...

MemberAddV2Result_validator: Incomplete

class MemberDevices(bb.Struct):
    team_member_id: Incomplete
    web_sessions: Incomplete
    desktop_clients: Incomplete
    mobile_clients: Incomplete
    def __init__(
        self,
        team_member_id: Incomplete | None = None,
        web_sessions: Incomplete | None = None,
        desktop_clients: Incomplete | None = None,
        mobile_clients: Incomplete | None = None,
    ) -> None: ...

MemberDevices_validator: Incomplete

class MemberLinkedApps(bb.Struct):
    team_member_id: Incomplete
    linked_api_apps: Incomplete
    def __init__(self, team_member_id: Incomplete | None = None, linked_api_apps: Incomplete | None = None) -> None: ...

MemberLinkedApps_validator: Incomplete

class MemberProfile(bb.Struct):
    team_member_id: Incomplete
    external_id: Incomplete
    account_id: Incomplete
    email: Incomplete
    email_verified: Incomplete
    secondary_emails: Incomplete
    status: Incomplete
    name: Incomplete
    membership_type: Incomplete
    invited_on: Incomplete
    joined_on: Incomplete
    suspended_on: Incomplete
    persistent_id: Incomplete
    is_directory_restricted: Incomplete
    profile_photo_url: Incomplete
    def __init__(
        self,
        team_member_id: Incomplete | None = None,
        email: Incomplete | None = None,
        email_verified: Incomplete | None = None,
        status: Incomplete | None = None,
        name: Incomplete | None = None,
        membership_type: Incomplete | None = None,
        external_id: Incomplete | None = None,
        account_id: Incomplete | None = None,
        secondary_emails: Incomplete | None = None,
        invited_on: Incomplete | None = None,
        joined_on: Incomplete | None = None,
        suspended_on: Incomplete | None = None,
        persistent_id: Incomplete | None = None,
        is_directory_restricted: Incomplete | None = None,
        profile_photo_url: Incomplete | None = None,
    ) -> None: ...

MemberProfile_validator: Incomplete

class UserSelectorError(bb.Union):
    user_not_found: Incomplete
    def is_user_not_found(self): ...

UserSelectorError_validator: Incomplete

class MemberSelectorError(UserSelectorError):
    user_not_in_team: Incomplete
    def is_user_not_in_team(self): ...

MemberSelectorError_validator: Incomplete

class MembersAddArgBase(bb.Struct):
    force_async: Incomplete
    def __init__(self, force_async: Incomplete | None = None) -> None: ...

MembersAddArgBase_validator: Incomplete

class MembersAddArg(MembersAddArgBase):
    new_members: Incomplete
    def __init__(self, new_members: Incomplete | None = None, force_async: Incomplete | None = None) -> None: ...

MembersAddArg_validator: Incomplete

class MembersAddJobStatus(async_.PollResultBase):
    @classmethod
    def complete(cls, val): ...
    @classmethod
    def failed(cls, val): ...
    def is_complete(self): ...
    def is_failed(self): ...
    def get_complete(self): ...
    def get_failed(self): ...

MembersAddJobStatus_validator: Incomplete

class MembersAddJobStatusV2Result(async_.PollResultBase):
    other: Incomplete
    @classmethod
    def complete(cls, val): ...
    @classmethod
    def failed(cls, val): ...
    def is_complete(self): ...
    def is_failed(self): ...
    def is_other(self): ...
    def get_complete(self): ...
    def get_failed(self): ...

MembersAddJobStatusV2Result_validator: Incomplete

class MembersAddLaunch(async_.LaunchResultBase):
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def get_complete(self): ...

MembersAddLaunch_validator: Incomplete

class MembersAddLaunchV2Result(async_.LaunchResultBase):
    other: Incomplete
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def is_other(self): ...
    def get_complete(self): ...

MembersAddLaunchV2Result_validator: Incomplete

class MembersAddV2Arg(MembersAddArgBase):
    new_members: Incomplete
    def __init__(self, new_members: Incomplete | None = None, force_async: Incomplete | None = None) -> None: ...

MembersAddV2Arg_validator: Incomplete

class MembersDeactivateBaseArg(bb.Struct):
    user: Incomplete
    def __init__(self, user: Incomplete | None = None) -> None: ...

MembersDeactivateBaseArg_validator: Incomplete

class MembersDataTransferArg(MembersDeactivateBaseArg):
    transfer_dest_id: Incomplete
    transfer_admin_id: Incomplete
    def __init__(
        self,
        user: Incomplete | None = None,
        transfer_dest_id: Incomplete | None = None,
        transfer_admin_id: Incomplete | None = None,
    ) -> None: ...

MembersDataTransferArg_validator: Incomplete

class MembersDeactivateArg(MembersDeactivateBaseArg):
    wipe_data: Incomplete
    def __init__(self, user: Incomplete | None = None, wipe_data: Incomplete | None = None) -> None: ...

MembersDeactivateArg_validator: Incomplete

class MembersDeactivateError(UserSelectorError):
    user_not_in_team: Incomplete
    other: Incomplete
    def is_user_not_in_team(self): ...
    def is_other(self): ...

MembersDeactivateError_validator: Incomplete

class MembersDeleteProfilePhotoArg(bb.Struct):
    user: Incomplete
    def __init__(self, user: Incomplete | None = None) -> None: ...

MembersDeleteProfilePhotoArg_validator: Incomplete

class MembersDeleteProfilePhotoError(MemberSelectorError):
    set_profile_disallowed: Incomplete
    other: Incomplete
    def is_set_profile_disallowed(self): ...
    def is_other(self): ...

MembersDeleteProfilePhotoError_validator: Incomplete

class MembersGetAvailableTeamMemberRolesResult(bb.Struct):
    roles: Incomplete
    def __init__(self, roles: Incomplete | None = None) -> None: ...

MembersGetAvailableTeamMemberRolesResult_validator: Incomplete

class MembersGetInfoArgs(bb.Struct):
    members: Incomplete
    def __init__(self, members: Incomplete | None = None) -> None: ...

MembersGetInfoArgs_validator: Incomplete

class MembersGetInfoError(bb.Union):
    other: Incomplete
    def is_other(self): ...

MembersGetInfoError_validator: Incomplete

class MembersGetInfoItemBase(bb.Union):
    @classmethod
    def id_not_found(cls, val): ...
    def is_id_not_found(self): ...
    def get_id_not_found(self): ...

MembersGetInfoItemBase_validator: Incomplete

class MembersGetInfoItem(MembersGetInfoItemBase):
    @classmethod
    def member_info(cls, val): ...
    def is_member_info(self): ...
    def get_member_info(self): ...

MembersGetInfoItem_validator: Incomplete

class MembersGetInfoItemV2(MembersGetInfoItemBase):
    other: Incomplete
    @classmethod
    def member_info(cls, val): ...
    def is_member_info(self): ...
    def is_other(self): ...
    def get_member_info(self): ...

MembersGetInfoItemV2_validator: Incomplete

class MembersGetInfoV2Arg(bb.Struct):
    members: Incomplete
    def __init__(self, members: Incomplete | None = None) -> None: ...

MembersGetInfoV2Arg_validator: Incomplete

class MembersGetInfoV2Result(bb.Struct):
    members_info: Incomplete
    def __init__(self, members_info: Incomplete | None = None) -> None: ...

MembersGetInfoV2Result_validator: Incomplete

class MembersInfo(bb.Struct):
    team_member_ids: Incomplete
    permanently_deleted_users: Incomplete
    def __init__(
        self, team_member_ids: Incomplete | None = None, permanently_deleted_users: Incomplete | None = None
    ) -> None: ...

MembersInfo_validator: Incomplete

class MembersListArg(bb.Struct):
    limit: Incomplete
    include_removed: Incomplete
    def __init__(self, limit: Incomplete | None = None, include_removed: Incomplete | None = None) -> None: ...

MembersListArg_validator: Incomplete

class MembersListContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

MembersListContinueArg_validator: Incomplete

class MembersListContinueError(bb.Union):
    invalid_cursor: Incomplete
    other: Incomplete
    def is_invalid_cursor(self): ...
    def is_other(self): ...

MembersListContinueError_validator: Incomplete

class MembersListError(bb.Union):
    other: Incomplete
    def is_other(self): ...

MembersListError_validator: Incomplete

class MembersListResult(bb.Struct):
    members: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self, members: Incomplete | None = None, cursor: Incomplete | None = None, has_more: Incomplete | None = None
    ) -> None: ...

MembersListResult_validator: Incomplete

class MembersListV2Result(bb.Struct):
    members: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self, members: Incomplete | None = None, cursor: Incomplete | None = None, has_more: Incomplete | None = None
    ) -> None: ...

MembersListV2Result_validator: Incomplete

class MembersRecoverArg(bb.Struct):
    user: Incomplete
    def __init__(self, user: Incomplete | None = None) -> None: ...

MembersRecoverArg_validator: Incomplete

class MembersRecoverError(UserSelectorError):
    user_unrecoverable: Incomplete
    user_not_in_team: Incomplete
    team_license_limit: Incomplete
    other: Incomplete
    def is_user_unrecoverable(self): ...
    def is_user_not_in_team(self): ...
    def is_team_license_limit(self): ...
    def is_other(self): ...

MembersRecoverError_validator: Incomplete

class MembersRemoveArg(MembersDeactivateArg):
    transfer_dest_id: Incomplete
    transfer_admin_id: Incomplete
    keep_account: Incomplete
    retain_team_shares: Incomplete
    def __init__(
        self,
        user: Incomplete | None = None,
        wipe_data: Incomplete | None = None,
        transfer_dest_id: Incomplete | None = None,
        transfer_admin_id: Incomplete | None = None,
        keep_account: Incomplete | None = None,
        retain_team_shares: Incomplete | None = None,
    ) -> None: ...

MembersRemoveArg_validator: Incomplete

class MembersTransferFilesError(MembersDeactivateError):
    removed_and_transfer_dest_should_differ: Incomplete
    removed_and_transfer_admin_should_differ: Incomplete
    transfer_dest_user_not_found: Incomplete
    transfer_dest_user_not_in_team: Incomplete
    transfer_admin_user_not_in_team: Incomplete
    transfer_admin_user_not_found: Incomplete
    unspecified_transfer_admin_id: Incomplete
    transfer_admin_is_not_admin: Incomplete
    recipient_not_verified: Incomplete
    def is_removed_and_transfer_dest_should_differ(self): ...
    def is_removed_and_transfer_admin_should_differ(self): ...
    def is_transfer_dest_user_not_found(self): ...
    def is_transfer_dest_user_not_in_team(self): ...
    def is_transfer_admin_user_not_in_team(self): ...
    def is_transfer_admin_user_not_found(self): ...
    def is_unspecified_transfer_admin_id(self): ...
    def is_transfer_admin_is_not_admin(self): ...
    def is_recipient_not_verified(self): ...

MembersTransferFilesError_validator: Incomplete

class MembersRemoveError(MembersTransferFilesError):
    remove_last_admin: Incomplete
    cannot_keep_account_and_transfer: Incomplete
    cannot_keep_account_and_delete_data: Incomplete
    email_address_too_long_to_be_disabled: Incomplete
    cannot_keep_invited_user_account: Incomplete
    cannot_retain_shares_when_data_wiped: Incomplete
    cannot_retain_shares_when_no_account_kept: Incomplete
    cannot_retain_shares_when_team_external_sharing_off: Incomplete
    cannot_keep_account: Incomplete
    cannot_keep_account_under_legal_hold: Incomplete
    cannot_keep_account_required_to_sign_tos: Incomplete
    def is_remove_last_admin(self): ...
    def is_cannot_keep_account_and_transfer(self): ...
    def is_cannot_keep_account_and_delete_data(self): ...
    def is_email_address_too_long_to_be_disabled(self): ...
    def is_cannot_keep_invited_user_account(self): ...
    def is_cannot_retain_shares_when_data_wiped(self): ...
    def is_cannot_retain_shares_when_no_account_kept(self): ...
    def is_cannot_retain_shares_when_team_external_sharing_off(self): ...
    def is_cannot_keep_account(self): ...
    def is_cannot_keep_account_under_legal_hold(self): ...
    def is_cannot_keep_account_required_to_sign_tos(self): ...

MembersRemoveError_validator: Incomplete

class MembersSendWelcomeError(MemberSelectorError):
    other: Incomplete
    def is_other(self): ...

MembersSendWelcomeError_validator: Incomplete

class MembersSetPermissions2Arg(bb.Struct):
    user: Incomplete
    new_roles: Incomplete
    def __init__(self, user: Incomplete | None = None, new_roles: Incomplete | None = None) -> None: ...

MembersSetPermissions2Arg_validator: Incomplete

class MembersSetPermissions2Error(UserSelectorError):
    last_admin: Incomplete
    user_not_in_team: Incomplete
    cannot_set_permissions: Incomplete
    role_not_found: Incomplete
    other: Incomplete
    def is_last_admin(self): ...
    def is_user_not_in_team(self): ...
    def is_cannot_set_permissions(self): ...
    def is_role_not_found(self): ...
    def is_other(self): ...

MembersSetPermissions2Error_validator: Incomplete

class MembersSetPermissions2Result(bb.Struct):
    team_member_id: Incomplete
    roles: Incomplete
    def __init__(self, team_member_id: Incomplete | None = None, roles: Incomplete | None = None) -> None: ...

MembersSetPermissions2Result_validator: Incomplete

class MembersSetPermissionsArg(bb.Struct):
    user: Incomplete
    new_role: Incomplete
    def __init__(self, user: Incomplete | None = None, new_role: Incomplete | None = None) -> None: ...

MembersSetPermissionsArg_validator: Incomplete

class MembersSetPermissionsError(UserSelectorError):
    last_admin: Incomplete
    user_not_in_team: Incomplete
    cannot_set_permissions: Incomplete
    team_license_limit: Incomplete
    other: Incomplete
    def is_last_admin(self): ...
    def is_user_not_in_team(self): ...
    def is_cannot_set_permissions(self): ...
    def is_team_license_limit(self): ...
    def is_other(self): ...

MembersSetPermissionsError_validator: Incomplete

class MembersSetPermissionsResult(bb.Struct):
    team_member_id: Incomplete
    role: Incomplete
    def __init__(self, team_member_id: Incomplete | None = None, role: Incomplete | None = None) -> None: ...

MembersSetPermissionsResult_validator: Incomplete

class MembersSetProfileArg(bb.Struct):
    user: Incomplete
    new_email: Incomplete
    new_external_id: Incomplete
    new_given_name: Incomplete
    new_surname: Incomplete
    new_persistent_id: Incomplete
    new_is_directory_restricted: Incomplete
    def __init__(
        self,
        user: Incomplete | None = None,
        new_email: Incomplete | None = None,
        new_external_id: Incomplete | None = None,
        new_given_name: Incomplete | None = None,
        new_surname: Incomplete | None = None,
        new_persistent_id: Incomplete | None = None,
        new_is_directory_restricted: Incomplete | None = None,
    ) -> None: ...

MembersSetProfileArg_validator: Incomplete

class MembersSetProfileError(MemberSelectorError):
    external_id_and_new_external_id_unsafe: Incomplete
    no_new_data_specified: Incomplete
    email_reserved_for_other_user: Incomplete
    external_id_used_by_other_user: Incomplete
    set_profile_disallowed: Incomplete
    param_cannot_be_empty: Incomplete
    persistent_id_disabled: Incomplete
    persistent_id_used_by_other_user: Incomplete
    directory_restricted_off: Incomplete
    other: Incomplete
    def is_external_id_and_new_external_id_unsafe(self): ...
    def is_no_new_data_specified(self): ...
    def is_email_reserved_for_other_user(self): ...
    def is_external_id_used_by_other_user(self): ...
    def is_set_profile_disallowed(self): ...
    def is_param_cannot_be_empty(self): ...
    def is_persistent_id_disabled(self): ...
    def is_persistent_id_used_by_other_user(self): ...
    def is_directory_restricted_off(self): ...
    def is_other(self): ...

MembersSetProfileError_validator: Incomplete

class MembersSetProfilePhotoArg(bb.Struct):
    user: Incomplete
    photo: Incomplete
    def __init__(self, user: Incomplete | None = None, photo: Incomplete | None = None) -> None: ...

MembersSetProfilePhotoArg_validator: Incomplete

class MembersSetProfilePhotoError(MemberSelectorError):
    set_profile_disallowed: Incomplete
    other: Incomplete
    @classmethod
    def photo_error(cls, val): ...
    def is_set_profile_disallowed(self): ...
    def is_photo_error(self): ...
    def is_other(self): ...
    def get_photo_error(self): ...

MembersSetProfilePhotoError_validator: Incomplete

class MembersSuspendError(MembersDeactivateError):
    suspend_inactive_user: Incomplete
    suspend_last_admin: Incomplete
    team_license_limit: Incomplete
    def is_suspend_inactive_user(self): ...
    def is_suspend_last_admin(self): ...
    def is_team_license_limit(self): ...

MembersSuspendError_validator: Incomplete

class MembersTransferFormerMembersFilesError(MembersTransferFilesError):
    user_data_is_being_transferred: Incomplete
    user_not_removed: Incomplete
    user_data_cannot_be_transferred: Incomplete
    user_data_already_transferred: Incomplete
    def is_user_data_is_being_transferred(self): ...
    def is_user_not_removed(self): ...
    def is_user_data_cannot_be_transferred(self): ...
    def is_user_data_already_transferred(self): ...

MembersTransferFormerMembersFilesError_validator: Incomplete

class MembersUnsuspendArg(bb.Struct):
    user: Incomplete
    def __init__(self, user: Incomplete | None = None) -> None: ...

MembersUnsuspendArg_validator: Incomplete

class MembersUnsuspendError(MembersDeactivateError):
    unsuspend_non_suspended_member: Incomplete
    team_license_limit: Incomplete
    def is_unsuspend_non_suspended_member(self): ...
    def is_team_license_limit(self): ...

MembersUnsuspendError_validator: Incomplete

class MobileClientPlatform(bb.Union):
    iphone: Incomplete
    ipad: Incomplete
    android: Incomplete
    windows_phone: Incomplete
    blackberry: Incomplete
    other: Incomplete
    def is_iphone(self): ...
    def is_ipad(self): ...
    def is_android(self): ...
    def is_windows_phone(self): ...
    def is_blackberry(self): ...
    def is_other(self): ...

MobileClientPlatform_validator: Incomplete

class MobileClientSession(DeviceSession):
    device_name: Incomplete
    client_type: Incomplete
    client_version: Incomplete
    os_version: Incomplete
    last_carrier: Incomplete
    def __init__(
        self,
        session_id: Incomplete | None = None,
        device_name: Incomplete | None = None,
        client_type: Incomplete | None = None,
        ip_address: Incomplete | None = None,
        country: Incomplete | None = None,
        created: Incomplete | None = None,
        updated: Incomplete | None = None,
        client_version: Incomplete | None = None,
        os_version: Incomplete | None = None,
        last_carrier: Incomplete | None = None,
    ) -> None: ...

MobileClientSession_validator: Incomplete

class NamespaceMetadata(bb.Struct):
    name: Incomplete
    namespace_id: Incomplete
    namespace_type: Incomplete
    team_member_id: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        namespace_id: Incomplete | None = None,
        namespace_type: Incomplete | None = None,
        team_member_id: Incomplete | None = None,
    ) -> None: ...

NamespaceMetadata_validator: Incomplete

class NamespaceType(bb.Union):
    app_folder: Incomplete
    shared_folder: Incomplete
    team_folder: Incomplete
    team_member_folder: Incomplete
    other: Incomplete
    def is_app_folder(self): ...
    def is_shared_folder(self): ...
    def is_team_folder(self): ...
    def is_team_member_folder(self): ...
    def is_other(self): ...

NamespaceType_validator: Incomplete

class RemoveCustomQuotaResult(bb.Union):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    @classmethod
    def invalid_user(cls, val): ...
    def is_success(self): ...
    def is_invalid_user(self): ...
    def is_other(self): ...
    def get_success(self): ...
    def get_invalid_user(self): ...

RemoveCustomQuotaResult_validator: Incomplete

class RemovedStatus(bb.Struct):
    is_recoverable: Incomplete
    is_disconnected: Incomplete
    def __init__(self, is_recoverable: Incomplete | None = None, is_disconnected: Incomplete | None = None) -> None: ...

RemovedStatus_validator: Incomplete

class ResendSecondaryEmailResult(bb.Union):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    @classmethod
    def not_pending(cls, val): ...
    @classmethod
    def rate_limited(cls, val): ...
    def is_success(self): ...
    def is_not_pending(self): ...
    def is_rate_limited(self): ...
    def is_other(self): ...
    def get_success(self): ...
    def get_not_pending(self): ...
    def get_rate_limited(self): ...

ResendSecondaryEmailResult_validator: Incomplete

class ResendVerificationEmailArg(bb.Struct):
    emails_to_resend: Incomplete
    def __init__(self, emails_to_resend: Incomplete | None = None) -> None: ...

ResendVerificationEmailArg_validator: Incomplete

class ResendVerificationEmailResult(bb.Struct):
    results: Incomplete
    def __init__(self, results: Incomplete | None = None) -> None: ...

ResendVerificationEmailResult_validator: Incomplete

class RevokeDesktopClientArg(DeviceSessionArg):
    delete_on_unlink: Incomplete
    def __init__(
        self,
        session_id: Incomplete | None = None,
        team_member_id: Incomplete | None = None,
        delete_on_unlink: Incomplete | None = None,
    ) -> None: ...

RevokeDesktopClientArg_validator: Incomplete

class RevokeDeviceSessionArg(bb.Union):
    @classmethod
    def web_session(cls, val): ...
    @classmethod
    def desktop_client(cls, val): ...
    @classmethod
    def mobile_client(cls, val): ...
    def is_web_session(self): ...
    def is_desktop_client(self): ...
    def is_mobile_client(self): ...
    def get_web_session(self): ...
    def get_desktop_client(self): ...
    def get_mobile_client(self): ...

RevokeDeviceSessionArg_validator: Incomplete

class RevokeDeviceSessionBatchArg(bb.Struct):
    revoke_devices: Incomplete
    def __init__(self, revoke_devices: Incomplete | None = None) -> None: ...

RevokeDeviceSessionBatchArg_validator: Incomplete

class RevokeDeviceSessionBatchError(bb.Union):
    other: Incomplete
    def is_other(self): ...

RevokeDeviceSessionBatchError_validator: Incomplete

class RevokeDeviceSessionBatchResult(bb.Struct):
    revoke_devices_status: Incomplete
    def __init__(self, revoke_devices_status: Incomplete | None = None) -> None: ...

RevokeDeviceSessionBatchResult_validator: Incomplete

class RevokeDeviceSessionError(bb.Union):
    device_session_not_found: Incomplete
    member_not_found: Incomplete
    other: Incomplete
    def is_device_session_not_found(self): ...
    def is_member_not_found(self): ...
    def is_other(self): ...

RevokeDeviceSessionError_validator: Incomplete

class RevokeDeviceSessionStatus(bb.Struct):
    success: Incomplete
    error_type: Incomplete
    def __init__(self, success: Incomplete | None = None, error_type: Incomplete | None = None) -> None: ...

RevokeDeviceSessionStatus_validator: Incomplete

class RevokeLinkedApiAppArg(bb.Struct):
    app_id: Incomplete
    team_member_id: Incomplete
    keep_app_folder: Incomplete
    def __init__(
        self,
        app_id: Incomplete | None = None,
        team_member_id: Incomplete | None = None,
        keep_app_folder: Incomplete | None = None,
    ) -> None: ...

RevokeLinkedApiAppArg_validator: Incomplete

class RevokeLinkedApiAppBatchArg(bb.Struct):
    revoke_linked_app: Incomplete
    def __init__(self, revoke_linked_app: Incomplete | None = None) -> None: ...

RevokeLinkedApiAppBatchArg_validator: Incomplete

class RevokeLinkedAppBatchError(bb.Union):
    other: Incomplete
    def is_other(self): ...

RevokeLinkedAppBatchError_validator: Incomplete

class RevokeLinkedAppBatchResult(bb.Struct):
    revoke_linked_app_status: Incomplete
    def __init__(self, revoke_linked_app_status: Incomplete | None = None) -> None: ...

RevokeLinkedAppBatchResult_validator: Incomplete

class RevokeLinkedAppError(bb.Union):
    app_not_found: Incomplete
    member_not_found: Incomplete
    app_folder_removal_not_supported: Incomplete
    other: Incomplete
    def is_app_not_found(self): ...
    def is_member_not_found(self): ...
    def is_app_folder_removal_not_supported(self): ...
    def is_other(self): ...

RevokeLinkedAppError_validator: Incomplete

class RevokeLinkedAppStatus(bb.Struct):
    success: Incomplete
    error_type: Incomplete
    def __init__(self, success: Incomplete | None = None, error_type: Incomplete | None = None) -> None: ...

RevokeLinkedAppStatus_validator: Incomplete

class SetCustomQuotaArg(bb.Struct):
    users_and_quotas: Incomplete
    def __init__(self, users_and_quotas: Incomplete | None = None) -> None: ...

SetCustomQuotaArg_validator: Incomplete

class SetCustomQuotaError(CustomQuotaError):
    some_users_are_excluded: Incomplete
    def is_some_users_are_excluded(self): ...

SetCustomQuotaError_validator: Incomplete

class SharingAllowlistAddArgs(bb.Struct):
    domains: Incomplete
    emails: Incomplete
    def __init__(self, domains: Incomplete | None = None, emails: Incomplete | None = None) -> None: ...

SharingAllowlistAddArgs_validator: Incomplete

class SharingAllowlistAddError(bb.Union):
    no_entries_provided: Incomplete
    too_many_entries_provided: Incomplete
    team_limit_reached: Incomplete
    unknown_error: Incomplete
    other: Incomplete
    @classmethod
    def malformed_entry(cls, val): ...
    @classmethod
    def entries_already_exist(cls, val): ...
    def is_malformed_entry(self): ...
    def is_no_entries_provided(self): ...
    def is_too_many_entries_provided(self): ...
    def is_team_limit_reached(self): ...
    def is_unknown_error(self): ...
    def is_entries_already_exist(self): ...
    def is_other(self): ...
    def get_malformed_entry(self): ...
    def get_entries_already_exist(self): ...

SharingAllowlistAddError_validator: Incomplete

class SharingAllowlistAddResponse(bb.Struct):
    def __init__(self) -> None: ...

SharingAllowlistAddResponse_validator: Incomplete

class SharingAllowlistListArg(bb.Struct):
    limit: Incomplete
    def __init__(self, limit: Incomplete | None = None) -> None: ...

SharingAllowlistListArg_validator: Incomplete

class SharingAllowlistListContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

SharingAllowlistListContinueArg_validator: Incomplete

class SharingAllowlistListContinueError(bb.Union):
    invalid_cursor: Incomplete
    other: Incomplete
    def is_invalid_cursor(self): ...
    def is_other(self): ...

SharingAllowlistListContinueError_validator: Incomplete

class SharingAllowlistListError(bb.Struct):
    def __init__(self) -> None: ...

SharingAllowlistListError_validator: Incomplete

class SharingAllowlistListResponse(bb.Struct):
    domains: Incomplete
    emails: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self,
        domains: Incomplete | None = None,
        emails: Incomplete | None = None,
        cursor: Incomplete | None = None,
        has_more: Incomplete | None = None,
    ) -> None: ...

SharingAllowlistListResponse_validator: Incomplete

class SharingAllowlistRemoveArgs(bb.Struct):
    domains: Incomplete
    emails: Incomplete
    def __init__(self, domains: Incomplete | None = None, emails: Incomplete | None = None) -> None: ...

SharingAllowlistRemoveArgs_validator: Incomplete

class SharingAllowlistRemoveError(bb.Union):
    no_entries_provided: Incomplete
    too_many_entries_provided: Incomplete
    unknown_error: Incomplete
    other: Incomplete
    @classmethod
    def malformed_entry(cls, val): ...
    @classmethod
    def entries_do_not_exist(cls, val): ...
    def is_malformed_entry(self): ...
    def is_entries_do_not_exist(self): ...
    def is_no_entries_provided(self): ...
    def is_too_many_entries_provided(self): ...
    def is_unknown_error(self): ...
    def is_other(self): ...
    def get_malformed_entry(self): ...
    def get_entries_do_not_exist(self): ...

SharingAllowlistRemoveError_validator: Incomplete

class SharingAllowlistRemoveResponse(bb.Struct):
    def __init__(self) -> None: ...

SharingAllowlistRemoveResponse_validator: Incomplete

class StorageBucket(bb.Struct):
    bucket: Incomplete
    users: Incomplete
    def __init__(self, bucket: Incomplete | None = None, users: Incomplete | None = None) -> None: ...

StorageBucket_validator: Incomplete

class TeamFolderAccessError(bb.Union):
    invalid_team_folder_id: Incomplete
    no_access: Incomplete
    other: Incomplete
    def is_invalid_team_folder_id(self): ...
    def is_no_access(self): ...
    def is_other(self): ...

TeamFolderAccessError_validator: Incomplete

class TeamFolderActivateError(BaseTeamFolderError): ...

TeamFolderActivateError_validator: Incomplete

class TeamFolderIdArg(bb.Struct):
    team_folder_id: Incomplete
    def __init__(self, team_folder_id: Incomplete | None = None) -> None: ...

TeamFolderIdArg_validator: Incomplete

class TeamFolderArchiveArg(TeamFolderIdArg):
    force_async_off: Incomplete
    def __init__(self, team_folder_id: Incomplete | None = None, force_async_off: Incomplete | None = None) -> None: ...

TeamFolderArchiveArg_validator: Incomplete

class TeamFolderArchiveError(BaseTeamFolderError): ...

TeamFolderArchiveError_validator: Incomplete

class TeamFolderArchiveJobStatus(async_.PollResultBase):
    @classmethod
    def complete(cls, val): ...
    @classmethod
    def failed(cls, val): ...
    def is_complete(self): ...
    def is_failed(self): ...
    def get_complete(self): ...
    def get_failed(self): ...

TeamFolderArchiveJobStatus_validator: Incomplete

class TeamFolderArchiveLaunch(async_.LaunchResultBase):
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def get_complete(self): ...

TeamFolderArchiveLaunch_validator: Incomplete

class TeamFolderCreateArg(bb.Struct):
    name: Incomplete
    sync_setting: Incomplete
    def __init__(self, name: Incomplete | None = None, sync_setting: Incomplete | None = None) -> None: ...

TeamFolderCreateArg_validator: Incomplete

class TeamFolderCreateError(bb.Union):
    invalid_folder_name: Incomplete
    folder_name_already_used: Incomplete
    folder_name_reserved: Incomplete
    other: Incomplete
    @classmethod
    def sync_settings_error(cls, val): ...
    def is_invalid_folder_name(self): ...
    def is_folder_name_already_used(self): ...
    def is_folder_name_reserved(self): ...
    def is_sync_settings_error(self): ...
    def is_other(self): ...
    def get_sync_settings_error(self): ...

TeamFolderCreateError_validator: Incomplete

class TeamFolderGetInfoItem(bb.Union):
    @classmethod
    def id_not_found(cls, val): ...
    @classmethod
    def team_folder_metadata(cls, val): ...
    def is_id_not_found(self): ...
    def is_team_folder_metadata(self): ...
    def get_id_not_found(self): ...
    def get_team_folder_metadata(self): ...

TeamFolderGetInfoItem_validator: Incomplete

class TeamFolderIdListArg(bb.Struct):
    team_folder_ids: Incomplete
    def __init__(self, team_folder_ids: Incomplete | None = None) -> None: ...

TeamFolderIdListArg_validator: Incomplete

class TeamFolderInvalidStatusError(bb.Union):
    active: Incomplete
    archived: Incomplete
    archive_in_progress: Incomplete
    other: Incomplete
    def is_active(self): ...
    def is_archived(self): ...
    def is_archive_in_progress(self): ...
    def is_other(self): ...

TeamFolderInvalidStatusError_validator: Incomplete

class TeamFolderListArg(bb.Struct):
    limit: Incomplete
    def __init__(self, limit: Incomplete | None = None) -> None: ...

TeamFolderListArg_validator: Incomplete

class TeamFolderListContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

TeamFolderListContinueArg_validator: Incomplete

class TeamFolderListContinueError(bb.Union):
    invalid_cursor: Incomplete
    other: Incomplete
    def is_invalid_cursor(self): ...
    def is_other(self): ...

TeamFolderListContinueError_validator: Incomplete

class TeamFolderListError(bb.Struct):
    access_error: Incomplete
    def __init__(self, access_error: Incomplete | None = None) -> None: ...

TeamFolderListError_validator: Incomplete

class TeamFolderListResult(bb.Struct):
    team_folders: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self, team_folders: Incomplete | None = None, cursor: Incomplete | None = None, has_more: Incomplete | None = None
    ) -> None: ...

TeamFolderListResult_validator: Incomplete

class TeamFolderMetadata(bb.Struct):
    team_folder_id: Incomplete
    name: Incomplete
    status: Incomplete
    is_team_shared_dropbox: Incomplete
    sync_setting: Incomplete
    content_sync_settings: Incomplete
    def __init__(
        self,
        team_folder_id: Incomplete | None = None,
        name: Incomplete | None = None,
        status: Incomplete | None = None,
        is_team_shared_dropbox: Incomplete | None = None,
        sync_setting: Incomplete | None = None,
        content_sync_settings: Incomplete | None = None,
    ) -> None: ...

TeamFolderMetadata_validator: Incomplete

class TeamFolderPermanentlyDeleteError(BaseTeamFolderError): ...

TeamFolderPermanentlyDeleteError_validator: Incomplete

class TeamFolderRenameArg(TeamFolderIdArg):
    name: Incomplete
    def __init__(self, team_folder_id: Incomplete | None = None, name: Incomplete | None = None) -> None: ...

TeamFolderRenameArg_validator: Incomplete

class TeamFolderRenameError(BaseTeamFolderError):
    invalid_folder_name: Incomplete
    folder_name_already_used: Incomplete
    folder_name_reserved: Incomplete
    def is_invalid_folder_name(self): ...
    def is_folder_name_already_used(self): ...
    def is_folder_name_reserved(self): ...

TeamFolderRenameError_validator: Incomplete

class TeamFolderStatus(bb.Union):
    active: Incomplete
    archived: Incomplete
    archive_in_progress: Incomplete
    other: Incomplete
    def is_active(self): ...
    def is_archived(self): ...
    def is_archive_in_progress(self): ...
    def is_other(self): ...

TeamFolderStatus_validator: Incomplete

class TeamFolderTeamSharedDropboxError(bb.Union):
    disallowed: Incomplete
    other: Incomplete
    def is_disallowed(self): ...
    def is_other(self): ...

TeamFolderTeamSharedDropboxError_validator: Incomplete

class TeamFolderUpdateSyncSettingsArg(TeamFolderIdArg):
    sync_setting: Incomplete
    content_sync_settings: Incomplete
    def __init__(
        self,
        team_folder_id: Incomplete | None = None,
        sync_setting: Incomplete | None = None,
        content_sync_settings: Incomplete | None = None,
    ) -> None: ...

TeamFolderUpdateSyncSettingsArg_validator: Incomplete

class TeamFolderUpdateSyncSettingsError(BaseTeamFolderError):
    @classmethod
    def sync_settings_error(cls, val): ...
    def is_sync_settings_error(self): ...
    def get_sync_settings_error(self): ...

TeamFolderUpdateSyncSettingsError_validator: Incomplete

class TeamGetInfoResult(bb.Struct):
    name: Incomplete
    team_id: Incomplete
    num_licensed_users: Incomplete
    num_provisioned_users: Incomplete
    num_used_licenses: Incomplete
    policies: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        team_id: Incomplete | None = None,
        num_licensed_users: Incomplete | None = None,
        num_provisioned_users: Incomplete | None = None,
        policies: Incomplete | None = None,
        num_used_licenses: Incomplete | None = None,
    ) -> None: ...

TeamGetInfoResult_validator: Incomplete

class TeamMemberInfo(bb.Struct):
    profile: Incomplete
    role: Incomplete
    def __init__(self, profile: Incomplete | None = None, role: Incomplete | None = None) -> None: ...

TeamMemberInfo_validator: Incomplete

class TeamMemberInfoV2(bb.Struct):
    profile: Incomplete
    roles: Incomplete
    def __init__(self, profile: Incomplete | None = None, roles: Incomplete | None = None) -> None: ...

TeamMemberInfoV2_validator: Incomplete

class TeamMemberInfoV2Result(bb.Struct):
    member_info: Incomplete
    def __init__(self, member_info: Incomplete | None = None) -> None: ...

TeamMemberInfoV2Result_validator: Incomplete

class TeamMemberProfile(MemberProfile):
    groups: Incomplete
    member_folder_id: Incomplete
    def __init__(
        self,
        team_member_id: Incomplete | None = None,
        email: Incomplete | None = None,
        email_verified: Incomplete | None = None,
        status: Incomplete | None = None,
        name: Incomplete | None = None,
        membership_type: Incomplete | None = None,
        groups: Incomplete | None = None,
        member_folder_id: Incomplete | None = None,
        external_id: Incomplete | None = None,
        account_id: Incomplete | None = None,
        secondary_emails: Incomplete | None = None,
        invited_on: Incomplete | None = None,
        joined_on: Incomplete | None = None,
        suspended_on: Incomplete | None = None,
        persistent_id: Incomplete | None = None,
        is_directory_restricted: Incomplete | None = None,
        profile_photo_url: Incomplete | None = None,
    ) -> None: ...

TeamMemberProfile_validator: Incomplete

class TeamMemberRole(bb.Struct):
    role_id: Incomplete
    name: Incomplete
    description: Incomplete
    def __init__(
        self, role_id: Incomplete | None = None, name: Incomplete | None = None, description: Incomplete | None = None
    ) -> None: ...

TeamMemberRole_validator: Incomplete

class TeamMemberStatus(bb.Union):
    active: Incomplete
    invited: Incomplete
    suspended: Incomplete
    @classmethod
    def removed(cls, val): ...
    def is_active(self): ...
    def is_invited(self): ...
    def is_suspended(self): ...
    def is_removed(self): ...
    def get_removed(self): ...

TeamMemberStatus_validator: Incomplete

class TeamMembershipType(bb.Union):
    full: Incomplete
    limited: Incomplete
    def is_full(self): ...
    def is_limited(self): ...

TeamMembershipType_validator: Incomplete

class TeamNamespacesListArg(bb.Struct):
    limit: Incomplete
    def __init__(self, limit: Incomplete | None = None) -> None: ...

TeamNamespacesListArg_validator: Incomplete

class TeamNamespacesListContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

TeamNamespacesListContinueArg_validator: Incomplete

class TeamNamespacesListError(bb.Union):
    invalid_arg: Incomplete
    other: Incomplete
    def is_invalid_arg(self): ...
    def is_other(self): ...

TeamNamespacesListError_validator: Incomplete

class TeamNamespacesListContinueError(TeamNamespacesListError):
    invalid_cursor: Incomplete
    def is_invalid_cursor(self): ...

TeamNamespacesListContinueError_validator: Incomplete

class TeamNamespacesListResult(bb.Struct):
    namespaces: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self, namespaces: Incomplete | None = None, cursor: Incomplete | None = None, has_more: Incomplete | None = None
    ) -> None: ...

TeamNamespacesListResult_validator: Incomplete

class TeamReportFailureReason(bb.Union):
    temporary_error: Incomplete
    many_reports_at_once: Incomplete
    too_much_data: Incomplete
    other: Incomplete
    def is_temporary_error(self): ...
    def is_many_reports_at_once(self): ...
    def is_too_much_data(self): ...
    def is_other(self): ...

TeamReportFailureReason_validator: Incomplete

class TokenGetAuthenticatedAdminError(bb.Union):
    mapping_not_found: Incomplete
    admin_not_active: Incomplete
    other: Incomplete
    def is_mapping_not_found(self): ...
    def is_admin_not_active(self): ...
    def is_other(self): ...

TokenGetAuthenticatedAdminError_validator: Incomplete

class TokenGetAuthenticatedAdminResult(bb.Struct):
    admin_profile: Incomplete
    def __init__(self, admin_profile: Incomplete | None = None) -> None: ...

TokenGetAuthenticatedAdminResult_validator: Incomplete

class UploadApiRateLimitValue(bb.Union):
    unlimited: Incomplete
    other: Incomplete
    @classmethod
    def limit(cls, val): ...
    def is_unlimited(self): ...
    def is_limit(self): ...
    def is_other(self): ...
    def get_limit(self): ...

UploadApiRateLimitValue_validator: Incomplete

class UserAddResult(bb.Union):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    @classmethod
    def invalid_user(cls, val): ...
    @classmethod
    def unverified(cls, val): ...
    @classmethod
    def placeholder_user(cls, val): ...
    def is_success(self): ...
    def is_invalid_user(self): ...
    def is_unverified(self): ...
    def is_placeholder_user(self): ...
    def is_other(self): ...
    def get_success(self): ...
    def get_invalid_user(self): ...
    def get_unverified(self): ...
    def get_placeholder_user(self): ...

UserAddResult_validator: Incomplete

class UserCustomQuotaArg(bb.Struct):
    user: Incomplete
    quota_gb: Incomplete
    def __init__(self, user: Incomplete | None = None, quota_gb: Incomplete | None = None) -> None: ...

UserCustomQuotaArg_validator: Incomplete

class UserCustomQuotaResult(bb.Struct):
    user: Incomplete
    quota_gb: Incomplete
    def __init__(self, user: Incomplete | None = None, quota_gb: Incomplete | None = None) -> None: ...

UserCustomQuotaResult_validator: Incomplete

class UserDeleteEmailsResult(bb.Struct):
    user: Incomplete
    results: Incomplete
    def __init__(self, user: Incomplete | None = None, results: Incomplete | None = None) -> None: ...

UserDeleteEmailsResult_validator: Incomplete

class UserDeleteResult(bb.Union):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    @classmethod
    def invalid_user(cls, val): ...
    def is_success(self): ...
    def is_invalid_user(self): ...
    def is_other(self): ...
    def get_success(self): ...
    def get_invalid_user(self): ...

UserDeleteResult_validator: Incomplete

class UserResendEmailsResult(bb.Struct):
    user: Incomplete
    results: Incomplete
    def __init__(self, user: Incomplete | None = None, results: Incomplete | None = None) -> None: ...

UserResendEmailsResult_validator: Incomplete

class UserResendResult(bb.Union):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    @classmethod
    def invalid_user(cls, val): ...
    def is_success(self): ...
    def is_invalid_user(self): ...
    def is_other(self): ...
    def get_success(self): ...
    def get_invalid_user(self): ...

UserResendResult_validator: Incomplete

class UserSecondaryEmailsArg(bb.Struct):
    user: Incomplete
    secondary_emails: Incomplete
    def __init__(self, user: Incomplete | None = None, secondary_emails: Incomplete | None = None) -> None: ...

UserSecondaryEmailsArg_validator: Incomplete

class UserSecondaryEmailsResult(bb.Struct):
    user: Incomplete
    results: Incomplete
    def __init__(self, user: Incomplete | None = None, results: Incomplete | None = None) -> None: ...

UserSecondaryEmailsResult_validator: Incomplete

class UserSelectorArg(bb.Union):
    @classmethod
    def team_member_id(cls, val): ...
    @classmethod
    def external_id(cls, val): ...
    @classmethod
    def email(cls, val): ...
    def is_team_member_id(self): ...
    def is_external_id(self): ...
    def is_email(self): ...
    def get_team_member_id(self): ...
    def get_external_id(self): ...
    def get_email(self): ...

UserSelectorArg_validator: Incomplete

class UsersSelectorArg(bb.Union):
    @classmethod
    def team_member_ids(cls, val): ...
    @classmethod
    def external_ids(cls, val): ...
    @classmethod
    def emails(cls, val): ...
    def is_team_member_ids(self): ...
    def is_external_ids(self): ...
    def is_emails(self): ...
    def get_team_member_ids(self): ...
    def get_external_ids(self): ...
    def get_emails(self): ...

UsersSelectorArg_validator: Incomplete
GroupsGetInfoResult_validator: Incomplete
LegalHoldId_validator: Incomplete
LegalHoldPolicyDescription_validator: Incomplete
LegalHoldPolicyName_validator: Incomplete
LegalHoldsGetPolicyResult_validator = LegalHoldPolicy_validator
LegalHoldsGetPolicyResult = LegalHoldPolicy
LegalHoldsPolicyCreateResult_validator = LegalHoldPolicy_validator
LegalHoldsPolicyCreateResult = LegalHoldPolicy
LegalHoldsPolicyUpdateResult_validator = LegalHoldPolicy_validator
LegalHoldsPolicyUpdateResult = LegalHoldPolicy
ListHeldRevisionCursor_validator: Incomplete
MembersGetInfoResult_validator: Incomplete
NumberPerDay_validator: Incomplete
Path_validator: Incomplete
SecondaryEmail_validator: Incomplete
SecondaryEmail: Incomplete
TeamMemberRoleId_validator: Incomplete
UserQuota_validator: Incomplete
devices_list_member_devices: Incomplete
devices_list_members_devices: Incomplete
devices_list_team_devices: Incomplete
devices_revoke_device_session: Incomplete
devices_revoke_device_session_batch: Incomplete
features_get_values: Incomplete
get_info: Incomplete
groups_create: Incomplete
groups_delete: Incomplete
groups_get_info: Incomplete
groups_job_status_get: Incomplete
groups_list: Incomplete
groups_list_continue: Incomplete
groups_members_add: Incomplete
groups_members_list: Incomplete
groups_members_list_continue: Incomplete
groups_members_remove: Incomplete
groups_members_set_access_type: Incomplete
groups_update: Incomplete
legal_holds_create_policy: Incomplete
legal_holds_get_policy: Incomplete
legal_holds_list_held_revisions: Incomplete
legal_holds_list_held_revisions_continue: Incomplete
legal_holds_list_policies: Incomplete
legal_holds_release_policy: Incomplete
legal_holds_update_policy: Incomplete
linked_apps_list_member_linked_apps: Incomplete
linked_apps_list_members_linked_apps: Incomplete
linked_apps_list_team_linked_apps: Incomplete
linked_apps_revoke_linked_app: Incomplete
linked_apps_revoke_linked_app_batch: Incomplete
member_space_limits_excluded_users_add: Incomplete
member_space_limits_excluded_users_list: Incomplete
member_space_limits_excluded_users_list_continue: Incomplete
member_space_limits_excluded_users_remove: Incomplete
member_space_limits_get_custom_quota: Incomplete
member_space_limits_remove_custom_quota: Incomplete
member_space_limits_set_custom_quota: Incomplete
members_add_v2: Incomplete
members_add: Incomplete
members_add_job_status_get_v2: Incomplete
members_add_job_status_get: Incomplete
members_delete_profile_photo_v2: Incomplete
members_delete_profile_photo: Incomplete
members_get_available_team_member_roles: Incomplete
members_get_info_v2: Incomplete
members_get_info: Incomplete
members_list_v2: Incomplete
members_list: Incomplete
members_list_continue_v2: Incomplete
members_list_continue: Incomplete
members_move_former_member_files: Incomplete
members_move_former_member_files_job_status_check: Incomplete
members_recover: Incomplete
members_remove: Incomplete
members_remove_job_status_get: Incomplete
members_secondary_emails_add: Incomplete
members_secondary_emails_delete: Incomplete
members_secondary_emails_resend_verification_emails: Incomplete
members_send_welcome_email: Incomplete
members_set_admin_permissions_v2: Incomplete
members_set_admin_permissions: Incomplete
members_set_profile_v2: Incomplete
members_set_profile: Incomplete
members_set_profile_photo_v2: Incomplete
members_set_profile_photo: Incomplete
members_suspend: Incomplete
members_unsuspend: Incomplete
namespaces_list: Incomplete
namespaces_list_continue: Incomplete
properties_template_add: Incomplete
properties_template_get: Incomplete
properties_template_list: Incomplete
properties_template_update: Incomplete
reports_get_activity: Incomplete
reports_get_devices: Incomplete
reports_get_membership: Incomplete
reports_get_storage: Incomplete
sharing_allowlist_add: Incomplete
sharing_allowlist_list: Incomplete
sharing_allowlist_list_continue: Incomplete
sharing_allowlist_remove: Incomplete
team_folder_activate: Incomplete
team_folder_archive: Incomplete
team_folder_archive_check: Incomplete
team_folder_create: Incomplete
team_folder_get_info: Incomplete
team_folder_list: Incomplete
team_folder_list_continue: Incomplete
team_folder_permanently_delete: Incomplete
team_folder_rename: Incomplete
team_folder_update_sync_settings: Incomplete
token_get_authenticated_admin: Incomplete
ROUTES: Incomplete
