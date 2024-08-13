from _typeshed import Incomplete

from dropbox import async_, team_common, users
from stone.backends.python_rsrc import stone_base as bb

class AccessInheritance(bb.Union):
    inherit: Incomplete
    no_inherit: Incomplete
    other: Incomplete
    def is_inherit(self): ...
    def is_no_inherit(self): ...
    def is_other(self): ...

AccessInheritance_validator: Incomplete

class AccessLevel(bb.Union):
    owner: Incomplete
    editor: Incomplete
    viewer: Incomplete
    viewer_no_comment: Incomplete
    traverse: Incomplete
    no_access: Incomplete
    other: Incomplete
    def is_owner(self): ...
    def is_editor(self): ...
    def is_viewer(self): ...
    def is_viewer_no_comment(self): ...
    def is_traverse(self): ...
    def is_no_access(self): ...
    def is_other(self): ...

AccessLevel_validator: Incomplete

class AclUpdatePolicy(bb.Union):
    owner: Incomplete
    editors: Incomplete
    other: Incomplete
    def is_owner(self): ...
    def is_editors(self): ...
    def is_other(self): ...

AclUpdatePolicy_validator: Incomplete

class AddFileMemberArgs(bb.Struct):
    file: Incomplete
    members: Incomplete
    custom_message: Incomplete
    quiet: Incomplete
    access_level: Incomplete
    add_message_as_comment: Incomplete
    def __init__(
        self,
        file: Incomplete | None = None,
        members: Incomplete | None = None,
        custom_message: Incomplete | None = None,
        quiet: Incomplete | None = None,
        access_level: Incomplete | None = None,
        add_message_as_comment: Incomplete | None = None,
    ) -> None: ...

AddFileMemberArgs_validator: Incomplete

class AddFileMemberError(bb.Union):
    rate_limit: Incomplete
    invalid_comment: Incomplete
    other: Incomplete
    @classmethod
    def user_error(cls, val): ...
    @classmethod
    def access_error(cls, val): ...
    def is_user_error(self): ...
    def is_access_error(self): ...
    def is_rate_limit(self): ...
    def is_invalid_comment(self): ...
    def is_other(self): ...
    def get_user_error(self): ...
    def get_access_error(self): ...

AddFileMemberError_validator: Incomplete

class AddFolderMemberArg(bb.Struct):
    shared_folder_id: Incomplete
    members: Incomplete
    quiet: Incomplete
    custom_message: Incomplete
    def __init__(
        self,
        shared_folder_id: Incomplete | None = None,
        members: Incomplete | None = None,
        quiet: Incomplete | None = None,
        custom_message: Incomplete | None = None,
    ) -> None: ...

AddFolderMemberArg_validator: Incomplete

class AddFolderMemberError(bb.Union):
    email_unverified: Incomplete
    banned_member: Incomplete
    cant_share_outside_team: Incomplete
    rate_limit: Incomplete
    too_many_invitees: Incomplete
    insufficient_plan: Incomplete
    team_folder: Incomplete
    no_permission: Incomplete
    invalid_shared_folder: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    @classmethod
    def bad_member(cls, val): ...
    @classmethod
    def too_many_members(cls, val): ...
    @classmethod
    def too_many_pending_invites(cls, val): ...
    def is_access_error(self): ...
    def is_email_unverified(self): ...
    def is_banned_member(self): ...
    def is_bad_member(self): ...
    def is_cant_share_outside_team(self): ...
    def is_too_many_members(self): ...
    def is_too_many_pending_invites(self): ...
    def is_rate_limit(self): ...
    def is_too_many_invitees(self): ...
    def is_insufficient_plan(self): ...
    def is_team_folder(self): ...
    def is_no_permission(self): ...
    def is_invalid_shared_folder(self): ...
    def is_other(self): ...
    def get_access_error(self): ...
    def get_bad_member(self): ...
    def get_too_many_members(self): ...
    def get_too_many_pending_invites(self): ...

AddFolderMemberError_validator: Incomplete

class AddMember(bb.Struct):
    member: Incomplete
    access_level: Incomplete
    def __init__(self, member: Incomplete | None = None, access_level: Incomplete | None = None) -> None: ...

AddMember_validator: Incomplete

class AddMemberSelectorError(bb.Union):
    automatic_group: Incomplete
    group_deleted: Incomplete
    group_not_on_team: Incomplete
    other: Incomplete
    @classmethod
    def invalid_dropbox_id(cls, val): ...
    @classmethod
    def invalid_email(cls, val): ...
    @classmethod
    def unverified_dropbox_id(cls, val): ...
    def is_automatic_group(self): ...
    def is_invalid_dropbox_id(self): ...
    def is_invalid_email(self): ...
    def is_unverified_dropbox_id(self): ...
    def is_group_deleted(self): ...
    def is_group_not_on_team(self): ...
    def is_other(self): ...
    def get_invalid_dropbox_id(self): ...
    def get_invalid_email(self): ...
    def get_unverified_dropbox_id(self): ...

AddMemberSelectorError_validator: Incomplete

class RequestedVisibility(bb.Union):
    public: Incomplete
    team_only: Incomplete
    password: Incomplete
    def is_public(self): ...
    def is_team_only(self): ...
    def is_password(self): ...

RequestedVisibility_validator: Incomplete

class ResolvedVisibility(RequestedVisibility):
    team_and_password: Incomplete
    shared_folder_only: Incomplete
    no_one: Incomplete
    only_you: Incomplete
    other: Incomplete
    def is_team_and_password(self): ...
    def is_shared_folder_only(self): ...
    def is_no_one(self): ...
    def is_only_you(self): ...
    def is_other(self): ...

ResolvedVisibility_validator: Incomplete

class AlphaResolvedVisibility(ResolvedVisibility): ...

AlphaResolvedVisibility_validator: Incomplete

class AudienceExceptionContentInfo(bb.Struct):
    name: Incomplete
    def __init__(self, name: Incomplete | None = None) -> None: ...

AudienceExceptionContentInfo_validator: Incomplete

class AudienceExceptions(bb.Struct):
    count: Incomplete
    exceptions: Incomplete
    def __init__(self, count: Incomplete | None = None, exceptions: Incomplete | None = None) -> None: ...

AudienceExceptions_validator: Incomplete

class AudienceRestrictingSharedFolder(bb.Struct):
    shared_folder_id: Incomplete
    name: Incomplete
    audience: Incomplete
    def __init__(
        self, shared_folder_id: Incomplete | None = None, name: Incomplete | None = None, audience: Incomplete | None = None
    ) -> None: ...

AudienceRestrictingSharedFolder_validator: Incomplete

class LinkMetadata(bb.Struct):
    url: Incomplete
    visibility: Incomplete
    expires: Incomplete
    def __init__(
        self, url: Incomplete | None = None, visibility: Incomplete | None = None, expires: Incomplete | None = None
    ) -> None: ...

LinkMetadata_validator: Incomplete

class CollectionLinkMetadata(LinkMetadata):
    def __init__(
        self, url: Incomplete | None = None, visibility: Incomplete | None = None, expires: Incomplete | None = None
    ) -> None: ...

CollectionLinkMetadata_validator: Incomplete

class CreateSharedLinkArg(bb.Struct):
    path: Incomplete
    short_url: Incomplete
    pending_upload: Incomplete
    def __init__(
        self, path: Incomplete | None = None, short_url: Incomplete | None = None, pending_upload: Incomplete | None = None
    ) -> None: ...

CreateSharedLinkArg_validator: Incomplete

class CreateSharedLinkError(bb.Union):
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_other(self): ...
    def get_path(self): ...

CreateSharedLinkError_validator: Incomplete

class CreateSharedLinkWithSettingsArg(bb.Struct):
    path: Incomplete
    settings: Incomplete
    def __init__(self, path: Incomplete | None = None, settings: Incomplete | None = None) -> None: ...

CreateSharedLinkWithSettingsArg_validator: Incomplete

class CreateSharedLinkWithSettingsError(bb.Union):
    email_not_verified: Incomplete
    access_denied: Incomplete
    @classmethod
    def path(cls, val): ...
    @classmethod
    def shared_link_already_exists(cls, val): ...
    @classmethod
    def settings_error(cls, val): ...
    def is_path(self): ...
    def is_email_not_verified(self): ...
    def is_shared_link_already_exists(self): ...
    def is_settings_error(self): ...
    def is_access_denied(self): ...
    def get_path(self): ...
    def get_shared_link_already_exists(self): ...
    def get_settings_error(self): ...

CreateSharedLinkWithSettingsError_validator: Incomplete

class SharedContentLinkMetadataBase(bb.Struct):
    access_level: Incomplete
    audience_options: Incomplete
    audience_restricting_shared_folder: Incomplete
    current_audience: Incomplete
    expiry: Incomplete
    link_permissions: Incomplete
    password_protected: Incomplete
    def __init__(
        self,
        audience_options: Incomplete | None = None,
        current_audience: Incomplete | None = None,
        link_permissions: Incomplete | None = None,
        password_protected: Incomplete | None = None,
        access_level: Incomplete | None = None,
        audience_restricting_shared_folder: Incomplete | None = None,
        expiry: Incomplete | None = None,
    ) -> None: ...

SharedContentLinkMetadataBase_validator: Incomplete

class ExpectedSharedContentLinkMetadata(SharedContentLinkMetadataBase):
    def __init__(
        self,
        audience_options: Incomplete | None = None,
        current_audience: Incomplete | None = None,
        link_permissions: Incomplete | None = None,
        password_protected: Incomplete | None = None,
        access_level: Incomplete | None = None,
        audience_restricting_shared_folder: Incomplete | None = None,
        expiry: Incomplete | None = None,
    ) -> None: ...

ExpectedSharedContentLinkMetadata_validator: Incomplete

class FileAction(bb.Union):
    disable_viewer_info: Incomplete
    edit_contents: Incomplete
    enable_viewer_info: Incomplete
    invite_viewer: Incomplete
    invite_viewer_no_comment: Incomplete
    invite_editor: Incomplete
    unshare: Incomplete
    relinquish_membership: Incomplete
    share_link: Incomplete
    create_link: Incomplete
    create_view_link: Incomplete
    create_edit_link: Incomplete
    other: Incomplete
    def is_disable_viewer_info(self): ...
    def is_edit_contents(self): ...
    def is_enable_viewer_info(self): ...
    def is_invite_viewer(self): ...
    def is_invite_viewer_no_comment(self): ...
    def is_invite_editor(self): ...
    def is_unshare(self): ...
    def is_relinquish_membership(self): ...
    def is_share_link(self): ...
    def is_create_link(self): ...
    def is_create_view_link(self): ...
    def is_create_edit_link(self): ...
    def is_other(self): ...

FileAction_validator: Incomplete

class FileErrorResult(bb.Union):
    other: Incomplete
    @classmethod
    def file_not_found_error(cls, val): ...
    @classmethod
    def invalid_file_action_error(cls, val): ...
    @classmethod
    def permission_denied_error(cls, val): ...
    def is_file_not_found_error(self): ...
    def is_invalid_file_action_error(self): ...
    def is_permission_denied_error(self): ...
    def is_other(self): ...
    def get_file_not_found_error(self): ...
    def get_invalid_file_action_error(self): ...
    def get_permission_denied_error(self): ...

FileErrorResult_validator: Incomplete

class SharedLinkMetadata(bb.Struct):
    url: Incomplete
    id: Incomplete
    name: Incomplete
    expires: Incomplete
    path_lower: Incomplete
    link_permissions: Incomplete
    team_member_info: Incomplete
    content_owner_team_info: Incomplete
    def __init__(
        self,
        url: Incomplete | None = None,
        name: Incomplete | None = None,
        link_permissions: Incomplete | None = None,
        id: Incomplete | None = None,
        expires: Incomplete | None = None,
        path_lower: Incomplete | None = None,
        team_member_info: Incomplete | None = None,
        content_owner_team_info: Incomplete | None = None,
    ) -> None: ...

SharedLinkMetadata_validator: Incomplete

class FileLinkMetadata(SharedLinkMetadata):
    client_modified: Incomplete
    server_modified: Incomplete
    rev: Incomplete
    size: Incomplete
    def __init__(
        self,
        url: Incomplete | None = None,
        name: Incomplete | None = None,
        link_permissions: Incomplete | None = None,
        client_modified: Incomplete | None = None,
        server_modified: Incomplete | None = None,
        rev: Incomplete | None = None,
        size: Incomplete | None = None,
        id: Incomplete | None = None,
        expires: Incomplete | None = None,
        path_lower: Incomplete | None = None,
        team_member_info: Incomplete | None = None,
        content_owner_team_info: Incomplete | None = None,
    ) -> None: ...

FileLinkMetadata_validator: Incomplete

class FileMemberActionError(bb.Union):
    invalid_member: Incomplete
    no_permission: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    @classmethod
    def no_explicit_access(cls, val): ...
    def is_invalid_member(self): ...
    def is_no_permission(self): ...
    def is_access_error(self): ...
    def is_no_explicit_access(self): ...
    def is_other(self): ...
    def get_access_error(self): ...
    def get_no_explicit_access(self): ...

FileMemberActionError_validator: Incomplete

class FileMemberActionIndividualResult(bb.Union):
    @classmethod
    def success(cls, val): ...
    @classmethod
    def member_error(cls, val): ...
    def is_success(self): ...
    def is_member_error(self): ...
    def get_success(self): ...
    def get_member_error(self): ...

FileMemberActionIndividualResult_validator: Incomplete

class FileMemberActionResult(bb.Struct):
    member: Incomplete
    result: Incomplete
    sckey_sha1: Incomplete
    invitation_signature: Incomplete
    def __init__(
        self,
        member: Incomplete | None = None,
        result: Incomplete | None = None,
        sckey_sha1: Incomplete | None = None,
        invitation_signature: Incomplete | None = None,
    ) -> None: ...

FileMemberActionResult_validator: Incomplete

class FileMemberRemoveActionResult(bb.Union):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    @classmethod
    def member_error(cls, val): ...
    def is_success(self): ...
    def is_member_error(self): ...
    def is_other(self): ...
    def get_success(self): ...
    def get_member_error(self): ...

FileMemberRemoveActionResult_validator: Incomplete

class FilePermission(bb.Struct):
    action: Incomplete
    allow: Incomplete
    reason: Incomplete
    def __init__(
        self, action: Incomplete | None = None, allow: Incomplete | None = None, reason: Incomplete | None = None
    ) -> None: ...

FilePermission_validator: Incomplete

class FolderAction(bb.Union):
    change_options: Incomplete
    disable_viewer_info: Incomplete
    edit_contents: Incomplete
    enable_viewer_info: Incomplete
    invite_editor: Incomplete
    invite_viewer: Incomplete
    invite_viewer_no_comment: Incomplete
    relinquish_membership: Incomplete
    unmount: Incomplete
    unshare: Incomplete
    leave_a_copy: Incomplete
    share_link: Incomplete
    create_link: Incomplete
    set_access_inheritance: Incomplete
    other: Incomplete
    def is_change_options(self): ...
    def is_disable_viewer_info(self): ...
    def is_edit_contents(self): ...
    def is_enable_viewer_info(self): ...
    def is_invite_editor(self): ...
    def is_invite_viewer(self): ...
    def is_invite_viewer_no_comment(self): ...
    def is_relinquish_membership(self): ...
    def is_unmount(self): ...
    def is_unshare(self): ...
    def is_leave_a_copy(self): ...
    def is_share_link(self): ...
    def is_create_link(self): ...
    def is_set_access_inheritance(self): ...
    def is_other(self): ...

FolderAction_validator: Incomplete

class FolderLinkMetadata(SharedLinkMetadata):
    def __init__(
        self,
        url: Incomplete | None = None,
        name: Incomplete | None = None,
        link_permissions: Incomplete | None = None,
        id: Incomplete | None = None,
        expires: Incomplete | None = None,
        path_lower: Incomplete | None = None,
        team_member_info: Incomplete | None = None,
        content_owner_team_info: Incomplete | None = None,
    ) -> None: ...

FolderLinkMetadata_validator: Incomplete

class FolderPermission(bb.Struct):
    action: Incomplete
    allow: Incomplete
    reason: Incomplete
    def __init__(
        self, action: Incomplete | None = None, allow: Incomplete | None = None, reason: Incomplete | None = None
    ) -> None: ...

FolderPermission_validator: Incomplete

class FolderPolicy(bb.Struct):
    member_policy: Incomplete
    resolved_member_policy: Incomplete
    acl_update_policy: Incomplete
    shared_link_policy: Incomplete
    viewer_info_policy: Incomplete
    def __init__(
        self,
        acl_update_policy: Incomplete | None = None,
        shared_link_policy: Incomplete | None = None,
        member_policy: Incomplete | None = None,
        resolved_member_policy: Incomplete | None = None,
        viewer_info_policy: Incomplete | None = None,
    ) -> None: ...

FolderPolicy_validator: Incomplete

class GetFileMetadataArg(bb.Struct):
    file: Incomplete
    actions: Incomplete
    def __init__(self, file: Incomplete | None = None, actions: Incomplete | None = None) -> None: ...

GetFileMetadataArg_validator: Incomplete

class GetFileMetadataBatchArg(bb.Struct):
    files: Incomplete
    actions: Incomplete
    def __init__(self, files: Incomplete | None = None, actions: Incomplete | None = None) -> None: ...

GetFileMetadataBatchArg_validator: Incomplete

class GetFileMetadataBatchResult(bb.Struct):
    file: Incomplete
    result: Incomplete
    def __init__(self, file: Incomplete | None = None, result: Incomplete | None = None) -> None: ...

GetFileMetadataBatchResult_validator: Incomplete

class GetFileMetadataError(bb.Union):
    other: Incomplete
    @classmethod
    def user_error(cls, val): ...
    @classmethod
    def access_error(cls, val): ...
    def is_user_error(self): ...
    def is_access_error(self): ...
    def is_other(self): ...
    def get_user_error(self): ...
    def get_access_error(self): ...

GetFileMetadataError_validator: Incomplete

class GetFileMetadataIndividualResult(bb.Union):
    other: Incomplete
    @classmethod
    def metadata(cls, val): ...
    @classmethod
    def access_error(cls, val): ...
    def is_metadata(self): ...
    def is_access_error(self): ...
    def is_other(self): ...
    def get_metadata(self): ...
    def get_access_error(self): ...

GetFileMetadataIndividualResult_validator: Incomplete

class GetMetadataArgs(bb.Struct):
    shared_folder_id: Incomplete
    actions: Incomplete
    def __init__(self, shared_folder_id: Incomplete | None = None, actions: Incomplete | None = None) -> None: ...

GetMetadataArgs_validator: Incomplete

class SharedLinkError(bb.Union):
    shared_link_not_found: Incomplete
    shared_link_access_denied: Incomplete
    unsupported_link_type: Incomplete
    other: Incomplete
    def is_shared_link_not_found(self): ...
    def is_shared_link_access_denied(self): ...
    def is_unsupported_link_type(self): ...
    def is_other(self): ...

SharedLinkError_validator: Incomplete

class GetSharedLinkFileError(SharedLinkError):
    shared_link_is_directory: Incomplete
    def is_shared_link_is_directory(self): ...

GetSharedLinkFileError_validator: Incomplete

class GetSharedLinkMetadataArg(bb.Struct):
    url: Incomplete
    path: Incomplete
    link_password: Incomplete
    def __init__(
        self, url: Incomplete | None = None, path: Incomplete | None = None, link_password: Incomplete | None = None
    ) -> None: ...

GetSharedLinkMetadataArg_validator: Incomplete

class GetSharedLinksArg(bb.Struct):
    path: Incomplete
    def __init__(self, path: Incomplete | None = None) -> None: ...

GetSharedLinksArg_validator: Incomplete

class GetSharedLinksError(bb.Union):
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_other(self): ...
    def get_path(self): ...

GetSharedLinksError_validator: Incomplete

class GetSharedLinksResult(bb.Struct):
    links: Incomplete
    def __init__(self, links: Incomplete | None = None) -> None: ...

GetSharedLinksResult_validator: Incomplete

class GroupInfo(team_common.GroupSummary):
    group_type: Incomplete
    is_member: Incomplete
    is_owner: Incomplete
    same_team: Incomplete
    def __init__(
        self,
        group_name: Incomplete | None = None,
        group_id: Incomplete | None = None,
        group_management_type: Incomplete | None = None,
        group_type: Incomplete | None = None,
        is_member: Incomplete | None = None,
        is_owner: Incomplete | None = None,
        same_team: Incomplete | None = None,
        group_external_id: Incomplete | None = None,
        member_count: Incomplete | None = None,
    ) -> None: ...

GroupInfo_validator: Incomplete

class MembershipInfo(bb.Struct):
    access_type: Incomplete
    permissions: Incomplete
    initials: Incomplete
    is_inherited: Incomplete
    def __init__(
        self,
        access_type: Incomplete | None = None,
        permissions: Incomplete | None = None,
        initials: Incomplete | None = None,
        is_inherited: Incomplete | None = None,
    ) -> None: ...

MembershipInfo_validator: Incomplete

class GroupMembershipInfo(MembershipInfo):
    group: Incomplete
    def __init__(
        self,
        access_type: Incomplete | None = None,
        group: Incomplete | None = None,
        permissions: Incomplete | None = None,
        initials: Incomplete | None = None,
        is_inherited: Incomplete | None = None,
    ) -> None: ...

GroupMembershipInfo_validator: Incomplete

class InsufficientPlan(bb.Struct):
    message: Incomplete
    upsell_url: Incomplete
    def __init__(self, message: Incomplete | None = None, upsell_url: Incomplete | None = None) -> None: ...

InsufficientPlan_validator: Incomplete

class InsufficientQuotaAmounts(bb.Struct):
    space_needed: Incomplete
    space_shortage: Incomplete
    space_left: Incomplete
    def __init__(
        self,
        space_needed: Incomplete | None = None,
        space_shortage: Incomplete | None = None,
        space_left: Incomplete | None = None,
    ) -> None: ...

InsufficientQuotaAmounts_validator: Incomplete

class InviteeInfo(bb.Union):
    other: Incomplete
    @classmethod
    def email(cls, val): ...
    def is_email(self): ...
    def is_other(self): ...
    def get_email(self): ...

InviteeInfo_validator: Incomplete

class InviteeMembershipInfo(MembershipInfo):
    invitee: Incomplete
    user: Incomplete
    def __init__(
        self,
        access_type: Incomplete | None = None,
        invitee: Incomplete | None = None,
        permissions: Incomplete | None = None,
        initials: Incomplete | None = None,
        is_inherited: Incomplete | None = None,
        user: Incomplete | None = None,
    ) -> None: ...

InviteeMembershipInfo_validator: Incomplete

class JobError(bb.Union):
    other: Incomplete
    @classmethod
    def unshare_folder_error(cls, val): ...
    @classmethod
    def remove_folder_member_error(cls, val): ...
    @classmethod
    def relinquish_folder_membership_error(cls, val): ...
    def is_unshare_folder_error(self): ...
    def is_remove_folder_member_error(self): ...
    def is_relinquish_folder_membership_error(self): ...
    def is_other(self): ...
    def get_unshare_folder_error(self): ...
    def get_remove_folder_member_error(self): ...
    def get_relinquish_folder_membership_error(self): ...

JobError_validator: Incomplete

class JobStatus(async_.PollResultBase):
    complete: Incomplete
    @classmethod
    def failed(cls, val): ...
    def is_complete(self): ...
    def is_failed(self): ...
    def get_failed(self): ...

JobStatus_validator: Incomplete

class LinkAccessLevel(bb.Union):
    viewer: Incomplete
    editor: Incomplete
    other: Incomplete
    def is_viewer(self): ...
    def is_editor(self): ...
    def is_other(self): ...

LinkAccessLevel_validator: Incomplete

class LinkAction(bb.Union):
    change_access_level: Incomplete
    change_audience: Incomplete
    remove_expiry: Incomplete
    remove_password: Incomplete
    set_expiry: Incomplete
    set_password: Incomplete
    other: Incomplete
    def is_change_access_level(self): ...
    def is_change_audience(self): ...
    def is_remove_expiry(self): ...
    def is_remove_password(self): ...
    def is_set_expiry(self): ...
    def is_set_password(self): ...
    def is_other(self): ...

LinkAction_validator: Incomplete

class LinkAudience(bb.Union):
    public: Incomplete
    team: Incomplete
    no_one: Incomplete
    password: Incomplete
    members: Incomplete
    other: Incomplete
    def is_public(self): ...
    def is_team(self): ...
    def is_no_one(self): ...
    def is_password(self): ...
    def is_members(self): ...
    def is_other(self): ...

LinkAudience_validator: Incomplete

class VisibilityPolicyDisallowedReason(bb.Union):
    delete_and_recreate: Incomplete
    restricted_by_shared_folder: Incomplete
    restricted_by_team: Incomplete
    user_not_on_team: Incomplete
    user_account_type: Incomplete
    permission_denied: Incomplete
    other: Incomplete
    def is_delete_and_recreate(self): ...
    def is_restricted_by_shared_folder(self): ...
    def is_restricted_by_team(self): ...
    def is_user_not_on_team(self): ...
    def is_user_account_type(self): ...
    def is_permission_denied(self): ...
    def is_other(self): ...

VisibilityPolicyDisallowedReason_validator: Incomplete

class LinkAudienceDisallowedReason(VisibilityPolicyDisallowedReason): ...

LinkAudienceDisallowedReason_validator: Incomplete

class LinkAudienceOption(bb.Struct):
    audience: Incomplete
    allowed: Incomplete
    disallowed_reason: Incomplete
    def __init__(
        self, audience: Incomplete | None = None, allowed: Incomplete | None = None, disallowed_reason: Incomplete | None = None
    ) -> None: ...

LinkAudienceOption_validator: Incomplete

class LinkExpiry(bb.Union):
    remove_expiry: Incomplete
    other: Incomplete
    @classmethod
    def set_expiry(cls, val): ...
    def is_remove_expiry(self): ...
    def is_set_expiry(self): ...
    def is_other(self): ...
    def get_set_expiry(self): ...

LinkExpiry_validator: Incomplete

class LinkPassword(bb.Union):
    remove_password: Incomplete
    other: Incomplete
    @classmethod
    def set_password(cls, val): ...
    def is_remove_password(self): ...
    def is_set_password(self): ...
    def is_other(self): ...
    def get_set_password(self): ...

LinkPassword_validator: Incomplete

class LinkPermission(bb.Struct):
    action: Incomplete
    allow: Incomplete
    reason: Incomplete
    def __init__(
        self, action: Incomplete | None = None, allow: Incomplete | None = None, reason: Incomplete | None = None
    ) -> None: ...

LinkPermission_validator: Incomplete

class LinkPermissions(bb.Struct):
    resolved_visibility: Incomplete
    requested_visibility: Incomplete
    can_revoke: Incomplete
    revoke_failure_reason: Incomplete
    effective_audience: Incomplete
    link_access_level: Incomplete
    visibility_policies: Incomplete
    can_set_expiry: Incomplete
    can_remove_expiry: Incomplete
    allow_download: Incomplete
    can_allow_download: Incomplete
    can_disallow_download: Incomplete
    allow_comments: Incomplete
    team_restricts_comments: Incomplete
    audience_options: Incomplete
    can_set_password: Incomplete
    can_remove_password: Incomplete
    require_password: Incomplete
    can_use_extended_sharing_controls: Incomplete
    def __init__(
        self,
        can_revoke: Incomplete | None = None,
        visibility_policies: Incomplete | None = None,
        can_set_expiry: Incomplete | None = None,
        can_remove_expiry: Incomplete | None = None,
        allow_download: Incomplete | None = None,
        can_allow_download: Incomplete | None = None,
        can_disallow_download: Incomplete | None = None,
        allow_comments: Incomplete | None = None,
        team_restricts_comments: Incomplete | None = None,
        resolved_visibility: Incomplete | None = None,
        requested_visibility: Incomplete | None = None,
        revoke_failure_reason: Incomplete | None = None,
        effective_audience: Incomplete | None = None,
        link_access_level: Incomplete | None = None,
        audience_options: Incomplete | None = None,
        can_set_password: Incomplete | None = None,
        can_remove_password: Incomplete | None = None,
        require_password: Incomplete | None = None,
        can_use_extended_sharing_controls: Incomplete | None = None,
    ) -> None: ...

LinkPermissions_validator: Incomplete

class LinkSettings(bb.Struct):
    access_level: Incomplete
    audience: Incomplete
    expiry: Incomplete
    password: Incomplete
    def __init__(
        self,
        access_level: Incomplete | None = None,
        audience: Incomplete | None = None,
        expiry: Incomplete | None = None,
        password: Incomplete | None = None,
    ) -> None: ...

LinkSettings_validator: Incomplete

class ListFileMembersArg(bb.Struct):
    file: Incomplete
    actions: Incomplete
    include_inherited: Incomplete
    limit: Incomplete
    def __init__(
        self,
        file: Incomplete | None = None,
        actions: Incomplete | None = None,
        include_inherited: Incomplete | None = None,
        limit: Incomplete | None = None,
    ) -> None: ...

ListFileMembersArg_validator: Incomplete

class ListFileMembersBatchArg(bb.Struct):
    files: Incomplete
    limit: Incomplete
    def __init__(self, files: Incomplete | None = None, limit: Incomplete | None = None) -> None: ...

ListFileMembersBatchArg_validator: Incomplete

class ListFileMembersBatchResult(bb.Struct):
    file: Incomplete
    result: Incomplete
    def __init__(self, file: Incomplete | None = None, result: Incomplete | None = None) -> None: ...

ListFileMembersBatchResult_validator: Incomplete

class ListFileMembersContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

ListFileMembersContinueArg_validator: Incomplete

class ListFileMembersContinueError(bb.Union):
    invalid_cursor: Incomplete
    other: Incomplete
    @classmethod
    def user_error(cls, val): ...
    @classmethod
    def access_error(cls, val): ...
    def is_user_error(self): ...
    def is_access_error(self): ...
    def is_invalid_cursor(self): ...
    def is_other(self): ...
    def get_user_error(self): ...
    def get_access_error(self): ...

ListFileMembersContinueError_validator: Incomplete

class ListFileMembersCountResult(bb.Struct):
    members: Incomplete
    member_count: Incomplete
    def __init__(self, members: Incomplete | None = None, member_count: Incomplete | None = None) -> None: ...

ListFileMembersCountResult_validator: Incomplete

class ListFileMembersError(bb.Union):
    other: Incomplete
    @classmethod
    def user_error(cls, val): ...
    @classmethod
    def access_error(cls, val): ...
    def is_user_error(self): ...
    def is_access_error(self): ...
    def is_other(self): ...
    def get_user_error(self): ...
    def get_access_error(self): ...

ListFileMembersError_validator: Incomplete

class ListFileMembersIndividualResult(bb.Union):
    other: Incomplete
    @classmethod
    def result(cls, val): ...
    @classmethod
    def access_error(cls, val): ...
    def is_result(self): ...
    def is_access_error(self): ...
    def is_other(self): ...
    def get_result(self): ...
    def get_access_error(self): ...

ListFileMembersIndividualResult_validator: Incomplete

class ListFilesArg(bb.Struct):
    limit: Incomplete
    actions: Incomplete
    def __init__(self, limit: Incomplete | None = None, actions: Incomplete | None = None) -> None: ...

ListFilesArg_validator: Incomplete

class ListFilesContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

ListFilesContinueArg_validator: Incomplete

class ListFilesContinueError(bb.Union):
    invalid_cursor: Incomplete
    other: Incomplete
    @classmethod
    def user_error(cls, val): ...
    def is_user_error(self): ...
    def is_invalid_cursor(self): ...
    def is_other(self): ...
    def get_user_error(self): ...

ListFilesContinueError_validator: Incomplete

class ListFilesResult(bb.Struct):
    entries: Incomplete
    cursor: Incomplete
    def __init__(self, entries: Incomplete | None = None, cursor: Incomplete | None = None) -> None: ...

ListFilesResult_validator: Incomplete

class ListFolderMembersCursorArg(bb.Struct):
    actions: Incomplete
    limit: Incomplete
    def __init__(self, actions: Incomplete | None = None, limit: Incomplete | None = None) -> None: ...

ListFolderMembersCursorArg_validator: Incomplete

class ListFolderMembersArgs(ListFolderMembersCursorArg):
    shared_folder_id: Incomplete
    def __init__(
        self, shared_folder_id: Incomplete | None = None, actions: Incomplete | None = None, limit: Incomplete | None = None
    ) -> None: ...

ListFolderMembersArgs_validator: Incomplete

class ListFolderMembersContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

ListFolderMembersContinueArg_validator: Incomplete

class ListFolderMembersContinueError(bb.Union):
    invalid_cursor: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    def is_access_error(self): ...
    def is_invalid_cursor(self): ...
    def is_other(self): ...
    def get_access_error(self): ...

ListFolderMembersContinueError_validator: Incomplete

class ListFoldersArgs(bb.Struct):
    limit: Incomplete
    actions: Incomplete
    def __init__(self, limit: Incomplete | None = None, actions: Incomplete | None = None) -> None: ...

ListFoldersArgs_validator: Incomplete

class ListFoldersContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

ListFoldersContinueArg_validator: Incomplete

class ListFoldersContinueError(bb.Union):
    invalid_cursor: Incomplete
    other: Incomplete
    def is_invalid_cursor(self): ...
    def is_other(self): ...

ListFoldersContinueError_validator: Incomplete

class ListFoldersResult(bb.Struct):
    entries: Incomplete
    cursor: Incomplete
    def __init__(self, entries: Incomplete | None = None, cursor: Incomplete | None = None) -> None: ...

ListFoldersResult_validator: Incomplete

class ListSharedLinksArg(bb.Struct):
    path: Incomplete
    cursor: Incomplete
    direct_only: Incomplete
    def __init__(
        self, path: Incomplete | None = None, cursor: Incomplete | None = None, direct_only: Incomplete | None = None
    ) -> None: ...

ListSharedLinksArg_validator: Incomplete

class ListSharedLinksError(bb.Union):
    reset: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_reset(self): ...
    def is_other(self): ...
    def get_path(self): ...

ListSharedLinksError_validator: Incomplete

class ListSharedLinksResult(bb.Struct):
    links: Incomplete
    has_more: Incomplete
    cursor: Incomplete
    def __init__(
        self, links: Incomplete | None = None, has_more: Incomplete | None = None, cursor: Incomplete | None = None
    ) -> None: ...

ListSharedLinksResult_validator: Incomplete

class MemberAccessLevelResult(bb.Struct):
    access_level: Incomplete
    warning: Incomplete
    access_details: Incomplete
    def __init__(
        self, access_level: Incomplete | None = None, warning: Incomplete | None = None, access_details: Incomplete | None = None
    ) -> None: ...

MemberAccessLevelResult_validator: Incomplete

class MemberAction(bb.Union):
    leave_a_copy: Incomplete
    make_editor: Incomplete
    make_owner: Incomplete
    make_viewer: Incomplete
    make_viewer_no_comment: Incomplete
    remove: Incomplete
    other: Incomplete
    def is_leave_a_copy(self): ...
    def is_make_editor(self): ...
    def is_make_owner(self): ...
    def is_make_viewer(self): ...
    def is_make_viewer_no_comment(self): ...
    def is_remove(self): ...
    def is_other(self): ...

MemberAction_validator: Incomplete

class MemberPermission(bb.Struct):
    action: Incomplete
    allow: Incomplete
    reason: Incomplete
    def __init__(
        self, action: Incomplete | None = None, allow: Incomplete | None = None, reason: Incomplete | None = None
    ) -> None: ...

MemberPermission_validator: Incomplete

class MemberPolicy(bb.Union):
    team: Incomplete
    anyone: Incomplete
    other: Incomplete
    def is_team(self): ...
    def is_anyone(self): ...
    def is_other(self): ...

MemberPolicy_validator: Incomplete

class MemberSelector(bb.Union):
    other: Incomplete
    @classmethod
    def dropbox_id(cls, val): ...
    @classmethod
    def email(cls, val): ...
    def is_dropbox_id(self): ...
    def is_email(self): ...
    def is_other(self): ...
    def get_dropbox_id(self): ...
    def get_email(self): ...

MemberSelector_validator: Incomplete

class ModifySharedLinkSettingsArgs(bb.Struct):
    url: Incomplete
    settings: Incomplete
    remove_expiration: Incomplete
    def __init__(
        self, url: Incomplete | None = None, settings: Incomplete | None = None, remove_expiration: Incomplete | None = None
    ) -> None: ...

ModifySharedLinkSettingsArgs_validator: Incomplete

class ModifySharedLinkSettingsError(SharedLinkError):
    email_not_verified: Incomplete
    @classmethod
    def settings_error(cls, val): ...
    def is_settings_error(self): ...
    def is_email_not_verified(self): ...
    def get_settings_error(self): ...

ModifySharedLinkSettingsError_validator: Incomplete

class MountFolderArg(bb.Struct):
    shared_folder_id: Incomplete
    def __init__(self, shared_folder_id: Incomplete | None = None) -> None: ...

MountFolderArg_validator: Incomplete

class MountFolderError(bb.Union):
    inside_shared_folder: Incomplete
    already_mounted: Incomplete
    no_permission: Incomplete
    not_mountable: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    @classmethod
    def insufficient_quota(cls, val): ...
    def is_access_error(self): ...
    def is_inside_shared_folder(self): ...
    def is_insufficient_quota(self): ...
    def is_already_mounted(self): ...
    def is_no_permission(self): ...
    def is_not_mountable(self): ...
    def is_other(self): ...
    def get_access_error(self): ...
    def get_insufficient_quota(self): ...

MountFolderError_validator: Incomplete

class ParentFolderAccessInfo(bb.Struct):
    folder_name: Incomplete
    shared_folder_id: Incomplete
    permissions: Incomplete
    path: Incomplete
    def __init__(
        self,
        folder_name: Incomplete | None = None,
        shared_folder_id: Incomplete | None = None,
        permissions: Incomplete | None = None,
        path: Incomplete | None = None,
    ) -> None: ...

ParentFolderAccessInfo_validator: Incomplete

class PathLinkMetadata(LinkMetadata):
    path: Incomplete
    def __init__(
        self,
        url: Incomplete | None = None,
        visibility: Incomplete | None = None,
        path: Incomplete | None = None,
        expires: Incomplete | None = None,
    ) -> None: ...

PathLinkMetadata_validator: Incomplete

class PendingUploadMode(bb.Union):
    file: Incomplete
    folder: Incomplete
    def is_file(self): ...
    def is_folder(self): ...

PendingUploadMode_validator: Incomplete

class PermissionDeniedReason(bb.Union):
    user_not_same_team_as_owner: Incomplete
    user_not_allowed_by_owner: Incomplete
    target_is_indirect_member: Incomplete
    target_is_owner: Incomplete
    target_is_self: Incomplete
    target_not_active: Incomplete
    folder_is_limited_team_folder: Incomplete
    owner_not_on_team: Incomplete
    permission_denied: Incomplete
    restricted_by_team: Incomplete
    user_account_type: Incomplete
    user_not_on_team: Incomplete
    folder_is_inside_shared_folder: Incomplete
    restricted_by_parent_folder: Incomplete
    other: Incomplete
    @classmethod
    def insufficient_plan(cls, val): ...
    def is_user_not_same_team_as_owner(self): ...
    def is_user_not_allowed_by_owner(self): ...
    def is_target_is_indirect_member(self): ...
    def is_target_is_owner(self): ...
    def is_target_is_self(self): ...
    def is_target_not_active(self): ...
    def is_folder_is_limited_team_folder(self): ...
    def is_owner_not_on_team(self): ...
    def is_permission_denied(self): ...
    def is_restricted_by_team(self): ...
    def is_user_account_type(self): ...
    def is_user_not_on_team(self): ...
    def is_folder_is_inside_shared_folder(self): ...
    def is_restricted_by_parent_folder(self): ...
    def is_insufficient_plan(self): ...
    def is_other(self): ...
    def get_insufficient_plan(self): ...

PermissionDeniedReason_validator: Incomplete

class RelinquishFileMembershipArg(bb.Struct):
    file: Incomplete
    def __init__(self, file: Incomplete | None = None) -> None: ...

RelinquishFileMembershipArg_validator: Incomplete

class RelinquishFileMembershipError(bb.Union):
    group_access: Incomplete
    no_permission: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    def is_access_error(self): ...
    def is_group_access(self): ...
    def is_no_permission(self): ...
    def is_other(self): ...
    def get_access_error(self): ...

RelinquishFileMembershipError_validator: Incomplete

class RelinquishFolderMembershipArg(bb.Struct):
    shared_folder_id: Incomplete
    leave_a_copy: Incomplete
    def __init__(self, shared_folder_id: Incomplete | None = None, leave_a_copy: Incomplete | None = None) -> None: ...

RelinquishFolderMembershipArg_validator: Incomplete

class RelinquishFolderMembershipError(bb.Union):
    folder_owner: Incomplete
    mounted: Incomplete
    group_access: Incomplete
    team_folder: Incomplete
    no_permission: Incomplete
    no_explicit_access: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    def is_access_error(self): ...
    def is_folder_owner(self): ...
    def is_mounted(self): ...
    def is_group_access(self): ...
    def is_team_folder(self): ...
    def is_no_permission(self): ...
    def is_no_explicit_access(self): ...
    def is_other(self): ...
    def get_access_error(self): ...

RelinquishFolderMembershipError_validator: Incomplete

class RemoveFileMemberArg(bb.Struct):
    file: Incomplete
    member: Incomplete
    def __init__(self, file: Incomplete | None = None, member: Incomplete | None = None) -> None: ...

RemoveFileMemberArg_validator: Incomplete

class RemoveFileMemberError(bb.Union):
    other: Incomplete
    @classmethod
    def user_error(cls, val): ...
    @classmethod
    def access_error(cls, val): ...
    @classmethod
    def no_explicit_access(cls, val): ...
    def is_user_error(self): ...
    def is_access_error(self): ...
    def is_no_explicit_access(self): ...
    def is_other(self): ...
    def get_user_error(self): ...
    def get_access_error(self): ...
    def get_no_explicit_access(self): ...

RemoveFileMemberError_validator: Incomplete

class RemoveFolderMemberArg(bb.Struct):
    shared_folder_id: Incomplete
    member: Incomplete
    leave_a_copy: Incomplete
    def __init__(
        self, shared_folder_id: Incomplete | None = None, member: Incomplete | None = None, leave_a_copy: Incomplete | None = None
    ) -> None: ...

RemoveFolderMemberArg_validator: Incomplete

class RemoveFolderMemberError(bb.Union):
    folder_owner: Incomplete
    group_access: Incomplete
    team_folder: Incomplete
    no_permission: Incomplete
    too_many_files: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    @classmethod
    def member_error(cls, val): ...
    def is_access_error(self): ...
    def is_member_error(self): ...
    def is_folder_owner(self): ...
    def is_group_access(self): ...
    def is_team_folder(self): ...
    def is_no_permission(self): ...
    def is_too_many_files(self): ...
    def is_other(self): ...
    def get_access_error(self): ...
    def get_member_error(self): ...

RemoveFolderMemberError_validator: Incomplete

class RemoveMemberJobStatus(async_.PollResultBase):
    @classmethod
    def complete(cls, val): ...
    @classmethod
    def failed(cls, val): ...
    def is_complete(self): ...
    def is_failed(self): ...
    def get_complete(self): ...
    def get_failed(self): ...

RemoveMemberJobStatus_validator: Incomplete

class RequestedLinkAccessLevel(bb.Union):
    viewer: Incomplete
    editor: Incomplete
    max: Incomplete
    default: Incomplete
    other: Incomplete
    def is_viewer(self): ...
    def is_editor(self): ...
    def is_max(self): ...
    def is_default(self): ...
    def is_other(self): ...

RequestedLinkAccessLevel_validator: Incomplete

class RevokeSharedLinkArg(bb.Struct):
    url: Incomplete
    def __init__(self, url: Incomplete | None = None) -> None: ...

RevokeSharedLinkArg_validator: Incomplete

class RevokeSharedLinkError(SharedLinkError):
    shared_link_malformed: Incomplete
    def is_shared_link_malformed(self): ...

RevokeSharedLinkError_validator: Incomplete

class SetAccessInheritanceArg(bb.Struct):
    access_inheritance: Incomplete
    shared_folder_id: Incomplete
    def __init__(self, shared_folder_id: Incomplete | None = None, access_inheritance: Incomplete | None = None) -> None: ...

SetAccessInheritanceArg_validator: Incomplete

class SetAccessInheritanceError(bb.Union):
    no_permission: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    def is_access_error(self): ...
    def is_no_permission(self): ...
    def is_other(self): ...
    def get_access_error(self): ...

SetAccessInheritanceError_validator: Incomplete

class ShareFolderArgBase(bb.Struct):
    acl_update_policy: Incomplete
    force_async: Incomplete
    member_policy: Incomplete
    path: Incomplete
    shared_link_policy: Incomplete
    viewer_info_policy: Incomplete
    access_inheritance: Incomplete
    def __init__(
        self,
        path: Incomplete | None = None,
        acl_update_policy: Incomplete | None = None,
        force_async: Incomplete | None = None,
        member_policy: Incomplete | None = None,
        shared_link_policy: Incomplete | None = None,
        viewer_info_policy: Incomplete | None = None,
        access_inheritance: Incomplete | None = None,
    ) -> None: ...

ShareFolderArgBase_validator: Incomplete

class ShareFolderArg(ShareFolderArgBase):
    actions: Incomplete
    link_settings: Incomplete
    def __init__(
        self,
        path: Incomplete | None = None,
        acl_update_policy: Incomplete | None = None,
        force_async: Incomplete | None = None,
        member_policy: Incomplete | None = None,
        shared_link_policy: Incomplete | None = None,
        viewer_info_policy: Incomplete | None = None,
        access_inheritance: Incomplete | None = None,
        actions: Incomplete | None = None,
        link_settings: Incomplete | None = None,
    ) -> None: ...

ShareFolderArg_validator: Incomplete

class ShareFolderErrorBase(bb.Union):
    email_unverified: Incomplete
    team_policy_disallows_member_policy: Incomplete
    disallowed_shared_link_policy: Incomplete
    other: Incomplete
    @classmethod
    def bad_path(cls, val): ...
    def is_email_unverified(self): ...
    def is_bad_path(self): ...
    def is_team_policy_disallows_member_policy(self): ...
    def is_disallowed_shared_link_policy(self): ...
    def is_other(self): ...
    def get_bad_path(self): ...

ShareFolderErrorBase_validator: Incomplete

class ShareFolderError(ShareFolderErrorBase):
    no_permission: Incomplete
    def is_no_permission(self): ...

ShareFolderError_validator: Incomplete

class ShareFolderJobStatus(async_.PollResultBase):
    @classmethod
    def complete(cls, val): ...
    @classmethod
    def failed(cls, val): ...
    def is_complete(self): ...
    def is_failed(self): ...
    def get_complete(self): ...
    def get_failed(self): ...

ShareFolderJobStatus_validator: Incomplete

class ShareFolderLaunch(async_.LaunchResultBase):
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def get_complete(self): ...

ShareFolderLaunch_validator: Incomplete

class SharePathError(bb.Union):
    is_file: Incomplete
    inside_shared_folder: Incomplete
    contains_shared_folder: Incomplete
    contains_app_folder: Incomplete
    contains_team_folder: Incomplete
    is_app_folder: Incomplete
    inside_app_folder: Incomplete
    is_public_folder: Incomplete
    inside_public_folder: Incomplete
    invalid_path: Incomplete
    is_osx_package: Incomplete
    inside_osx_package: Incomplete
    is_vault: Incomplete
    is_vault_locked: Incomplete
    is_family: Incomplete
    other: Incomplete
    @classmethod
    def already_shared(cls, val): ...
    def is_is_file(self): ...
    def is_inside_shared_folder(self): ...
    def is_contains_shared_folder(self): ...
    def is_contains_app_folder(self): ...
    def is_contains_team_folder(self): ...
    def is_is_app_folder(self): ...
    def is_inside_app_folder(self): ...
    def is_is_public_folder(self): ...
    def is_inside_public_folder(self): ...
    def is_already_shared(self): ...
    def is_invalid_path(self): ...
    def is_is_osx_package(self): ...
    def is_inside_osx_package(self): ...
    def is_is_vault(self): ...
    def is_is_vault_locked(self): ...
    def is_is_family(self): ...
    def is_other(self): ...
    def get_already_shared(self): ...

SharePathError_validator: Incomplete

class SharedContentLinkMetadata(SharedContentLinkMetadataBase):
    audience_exceptions: Incomplete
    url: Incomplete
    def __init__(
        self,
        audience_options: Incomplete | None = None,
        current_audience: Incomplete | None = None,
        link_permissions: Incomplete | None = None,
        password_protected: Incomplete | None = None,
        url: Incomplete | None = None,
        access_level: Incomplete | None = None,
        audience_restricting_shared_folder: Incomplete | None = None,
        expiry: Incomplete | None = None,
        audience_exceptions: Incomplete | None = None,
    ) -> None: ...

SharedContentLinkMetadata_validator: Incomplete

class SharedFileMembers(bb.Struct):
    users: Incomplete
    groups: Incomplete
    invitees: Incomplete
    cursor: Incomplete
    def __init__(
        self,
        users: Incomplete | None = None,
        groups: Incomplete | None = None,
        invitees: Incomplete | None = None,
        cursor: Incomplete | None = None,
    ) -> None: ...

SharedFileMembers_validator: Incomplete

class SharedFileMetadata(bb.Struct):
    access_type: Incomplete
    id: Incomplete
    expected_link_metadata: Incomplete
    link_metadata: Incomplete
    name: Incomplete
    owner_display_names: Incomplete
    owner_team: Incomplete
    parent_shared_folder_id: Incomplete
    path_display: Incomplete
    path_lower: Incomplete
    permissions: Incomplete
    policy: Incomplete
    preview_url: Incomplete
    time_invited: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        name: Incomplete | None = None,
        policy: Incomplete | None = None,
        preview_url: Incomplete | None = None,
        access_type: Incomplete | None = None,
        expected_link_metadata: Incomplete | None = None,
        link_metadata: Incomplete | None = None,
        owner_display_names: Incomplete | None = None,
        owner_team: Incomplete | None = None,
        parent_shared_folder_id: Incomplete | None = None,
        path_display: Incomplete | None = None,
        path_lower: Incomplete | None = None,
        permissions: Incomplete | None = None,
        time_invited: Incomplete | None = None,
    ) -> None: ...

SharedFileMetadata_validator: Incomplete

class SharedFolderAccessError(bb.Union):
    invalid_id: Incomplete
    not_a_member: Incomplete
    invalid_member: Incomplete
    email_unverified: Incomplete
    unmounted: Incomplete
    other: Incomplete
    def is_invalid_id(self): ...
    def is_not_a_member(self): ...
    def is_invalid_member(self): ...
    def is_email_unverified(self): ...
    def is_unmounted(self): ...
    def is_other(self): ...

SharedFolderAccessError_validator: Incomplete

class SharedFolderMemberError(bb.Union):
    invalid_dropbox_id: Incomplete
    not_a_member: Incomplete
    other: Incomplete
    @classmethod
    def no_explicit_access(cls, val): ...
    def is_invalid_dropbox_id(self): ...
    def is_not_a_member(self): ...
    def is_no_explicit_access(self): ...
    def is_other(self): ...
    def get_no_explicit_access(self): ...

SharedFolderMemberError_validator: Incomplete

class SharedFolderMembers(bb.Struct):
    users: Incomplete
    groups: Incomplete
    invitees: Incomplete
    cursor: Incomplete
    def __init__(
        self,
        users: Incomplete | None = None,
        groups: Incomplete | None = None,
        invitees: Incomplete | None = None,
        cursor: Incomplete | None = None,
    ) -> None: ...

SharedFolderMembers_validator: Incomplete

class SharedFolderMetadataBase(bb.Struct):
    access_type: Incomplete
    is_inside_team_folder: Incomplete
    is_team_folder: Incomplete
    owner_display_names: Incomplete
    owner_team: Incomplete
    parent_shared_folder_id: Incomplete
    path_display: Incomplete
    path_lower: Incomplete
    parent_folder_name: Incomplete
    def __init__(
        self,
        access_type: Incomplete | None = None,
        is_inside_team_folder: Incomplete | None = None,
        is_team_folder: Incomplete | None = None,
        owner_display_names: Incomplete | None = None,
        owner_team: Incomplete | None = None,
        parent_shared_folder_id: Incomplete | None = None,
        path_display: Incomplete | None = None,
        path_lower: Incomplete | None = None,
        parent_folder_name: Incomplete | None = None,
    ) -> None: ...

SharedFolderMetadataBase_validator: Incomplete

class SharedFolderMetadata(SharedFolderMetadataBase):
    link_metadata: Incomplete
    name: Incomplete
    permissions: Incomplete
    policy: Incomplete
    preview_url: Incomplete
    shared_folder_id: Incomplete
    time_invited: Incomplete
    access_inheritance: Incomplete
    def __init__(
        self,
        access_type: Incomplete | None = None,
        is_inside_team_folder: Incomplete | None = None,
        is_team_folder: Incomplete | None = None,
        name: Incomplete | None = None,
        policy: Incomplete | None = None,
        preview_url: Incomplete | None = None,
        shared_folder_id: Incomplete | None = None,
        time_invited: Incomplete | None = None,
        owner_display_names: Incomplete | None = None,
        owner_team: Incomplete | None = None,
        parent_shared_folder_id: Incomplete | None = None,
        path_display: Incomplete | None = None,
        path_lower: Incomplete | None = None,
        parent_folder_name: Incomplete | None = None,
        link_metadata: Incomplete | None = None,
        permissions: Incomplete | None = None,
        access_inheritance: Incomplete | None = None,
    ) -> None: ...

SharedFolderMetadata_validator: Incomplete

class SharedLinkAccessFailureReason(bb.Union):
    login_required: Incomplete
    email_verify_required: Incomplete
    password_required: Incomplete
    team_only: Incomplete
    owner_only: Incomplete
    other: Incomplete
    def is_login_required(self): ...
    def is_email_verify_required(self): ...
    def is_password_required(self): ...
    def is_team_only(self): ...
    def is_owner_only(self): ...
    def is_other(self): ...

SharedLinkAccessFailureReason_validator: Incomplete

class SharedLinkAlreadyExistsMetadata(bb.Union):
    other: Incomplete
    @classmethod
    def metadata(cls, val): ...
    def is_metadata(self): ...
    def is_other(self): ...
    def get_metadata(self): ...

SharedLinkAlreadyExistsMetadata_validator: Incomplete

class SharedLinkPolicy(bb.Union):
    anyone: Incomplete
    team: Incomplete
    members: Incomplete
    other: Incomplete
    def is_anyone(self): ...
    def is_team(self): ...
    def is_members(self): ...
    def is_other(self): ...

SharedLinkPolicy_validator: Incomplete

class SharedLinkSettings(bb.Struct):
    require_password: Incomplete
    link_password: Incomplete
    expires: Incomplete
    audience: Incomplete
    access: Incomplete
    requested_visibility: Incomplete
    allow_download: Incomplete
    def __init__(
        self,
        require_password: Incomplete | None = None,
        link_password: Incomplete | None = None,
        expires: Incomplete | None = None,
        audience: Incomplete | None = None,
        access: Incomplete | None = None,
        requested_visibility: Incomplete | None = None,
        allow_download: Incomplete | None = None,
    ) -> None: ...

SharedLinkSettings_validator: Incomplete

class SharedLinkSettingsError(bb.Union):
    invalid_settings: Incomplete
    not_authorized: Incomplete
    def is_invalid_settings(self): ...
    def is_not_authorized(self): ...

SharedLinkSettingsError_validator: Incomplete

class SharingFileAccessError(bb.Union):
    no_permission: Incomplete
    invalid_file: Incomplete
    is_folder: Incomplete
    inside_public_folder: Incomplete
    inside_osx_package: Incomplete
    other: Incomplete
    def is_no_permission(self): ...
    def is_invalid_file(self): ...
    def is_is_folder(self): ...
    def is_inside_public_folder(self): ...
    def is_inside_osx_package(self): ...
    def is_other(self): ...

SharingFileAccessError_validator: Incomplete

class SharingUserError(bb.Union):
    email_unverified: Incomplete
    other: Incomplete
    def is_email_unverified(self): ...
    def is_other(self): ...

SharingUserError_validator: Incomplete

class TeamMemberInfo(bb.Struct):
    team_info: Incomplete
    display_name: Incomplete
    member_id: Incomplete
    def __init__(
        self, team_info: Incomplete | None = None, display_name: Incomplete | None = None, member_id: Incomplete | None = None
    ) -> None: ...

TeamMemberInfo_validator: Incomplete

class TransferFolderArg(bb.Struct):
    shared_folder_id: Incomplete
    to_dropbox_id: Incomplete
    def __init__(self, shared_folder_id: Incomplete | None = None, to_dropbox_id: Incomplete | None = None) -> None: ...

TransferFolderArg_validator: Incomplete

class TransferFolderError(bb.Union):
    invalid_dropbox_id: Incomplete
    new_owner_not_a_member: Incomplete
    new_owner_unmounted: Incomplete
    new_owner_email_unverified: Incomplete
    team_folder: Incomplete
    no_permission: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    def is_access_error(self): ...
    def is_invalid_dropbox_id(self): ...
    def is_new_owner_not_a_member(self): ...
    def is_new_owner_unmounted(self): ...
    def is_new_owner_email_unverified(self): ...
    def is_team_folder(self): ...
    def is_no_permission(self): ...
    def is_other(self): ...
    def get_access_error(self): ...

TransferFolderError_validator: Incomplete

class UnmountFolderArg(bb.Struct):
    shared_folder_id: Incomplete
    def __init__(self, shared_folder_id: Incomplete | None = None) -> None: ...

UnmountFolderArg_validator: Incomplete

class UnmountFolderError(bb.Union):
    no_permission: Incomplete
    not_unmountable: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    def is_access_error(self): ...
    def is_no_permission(self): ...
    def is_not_unmountable(self): ...
    def is_other(self): ...
    def get_access_error(self): ...

UnmountFolderError_validator: Incomplete

class UnshareFileArg(bb.Struct):
    file: Incomplete
    def __init__(self, file: Incomplete | None = None) -> None: ...

UnshareFileArg_validator: Incomplete

class UnshareFileError(bb.Union):
    other: Incomplete
    @classmethod
    def user_error(cls, val): ...
    @classmethod
    def access_error(cls, val): ...
    def is_user_error(self): ...
    def is_access_error(self): ...
    def is_other(self): ...
    def get_user_error(self): ...
    def get_access_error(self): ...

UnshareFileError_validator: Incomplete

class UnshareFolderArg(bb.Struct):
    shared_folder_id: Incomplete
    leave_a_copy: Incomplete
    def __init__(self, shared_folder_id: Incomplete | None = None, leave_a_copy: Incomplete | None = None) -> None: ...

UnshareFolderArg_validator: Incomplete

class UnshareFolderError(bb.Union):
    team_folder: Incomplete
    no_permission: Incomplete
    too_many_files: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    def is_access_error(self): ...
    def is_team_folder(self): ...
    def is_no_permission(self): ...
    def is_too_many_files(self): ...
    def is_other(self): ...
    def get_access_error(self): ...

UnshareFolderError_validator: Incomplete

class UpdateFileMemberArgs(bb.Struct):
    file: Incomplete
    member: Incomplete
    access_level: Incomplete
    def __init__(
        self, file: Incomplete | None = None, member: Incomplete | None = None, access_level: Incomplete | None = None
    ) -> None: ...

UpdateFileMemberArgs_validator: Incomplete

class UpdateFolderMemberArg(bb.Struct):
    shared_folder_id: Incomplete
    member: Incomplete
    access_level: Incomplete
    def __init__(
        self, shared_folder_id: Incomplete | None = None, member: Incomplete | None = None, access_level: Incomplete | None = None
    ) -> None: ...

UpdateFolderMemberArg_validator: Incomplete

class UpdateFolderMemberError(bb.Union):
    insufficient_plan: Incomplete
    no_permission: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    @classmethod
    def member_error(cls, val): ...
    @classmethod
    def no_explicit_access(cls, val): ...
    def is_access_error(self): ...
    def is_member_error(self): ...
    def is_no_explicit_access(self): ...
    def is_insufficient_plan(self): ...
    def is_no_permission(self): ...
    def is_other(self): ...
    def get_access_error(self): ...
    def get_member_error(self): ...
    def get_no_explicit_access(self): ...

UpdateFolderMemberError_validator: Incomplete

class UpdateFolderPolicyArg(bb.Struct):
    shared_folder_id: Incomplete
    member_policy: Incomplete
    acl_update_policy: Incomplete
    viewer_info_policy: Incomplete
    shared_link_policy: Incomplete
    link_settings: Incomplete
    actions: Incomplete
    def __init__(
        self,
        shared_folder_id: Incomplete | None = None,
        member_policy: Incomplete | None = None,
        acl_update_policy: Incomplete | None = None,
        viewer_info_policy: Incomplete | None = None,
        shared_link_policy: Incomplete | None = None,
        link_settings: Incomplete | None = None,
        actions: Incomplete | None = None,
    ) -> None: ...

UpdateFolderPolicyArg_validator: Incomplete

class UpdateFolderPolicyError(bb.Union):
    not_on_team: Incomplete
    team_policy_disallows_member_policy: Incomplete
    disallowed_shared_link_policy: Incomplete
    no_permission: Incomplete
    team_folder: Incomplete
    other: Incomplete
    @classmethod
    def access_error(cls, val): ...
    def is_access_error(self): ...
    def is_not_on_team(self): ...
    def is_team_policy_disallows_member_policy(self): ...
    def is_disallowed_shared_link_policy(self): ...
    def is_no_permission(self): ...
    def is_team_folder(self): ...
    def is_other(self): ...
    def get_access_error(self): ...

UpdateFolderPolicyError_validator: Incomplete

class UserMembershipInfo(MembershipInfo):
    user: Incomplete
    def __init__(
        self,
        access_type: Incomplete | None = None,
        user: Incomplete | None = None,
        permissions: Incomplete | None = None,
        initials: Incomplete | None = None,
        is_inherited: Incomplete | None = None,
    ) -> None: ...

UserMembershipInfo_validator: Incomplete

class UserFileMembershipInfo(UserMembershipInfo):
    time_last_seen: Incomplete
    platform_type: Incomplete
    def __init__(
        self,
        access_type: Incomplete | None = None,
        user: Incomplete | None = None,
        permissions: Incomplete | None = None,
        initials: Incomplete | None = None,
        is_inherited: Incomplete | None = None,
        time_last_seen: Incomplete | None = None,
        platform_type: Incomplete | None = None,
    ) -> None: ...

UserFileMembershipInfo_validator: Incomplete

class UserInfo(bb.Struct):
    account_id: Incomplete
    email: Incomplete
    display_name: Incomplete
    same_team: Incomplete
    team_member_id: Incomplete
    def __init__(
        self,
        account_id: Incomplete | None = None,
        email: Incomplete | None = None,
        display_name: Incomplete | None = None,
        same_team: Incomplete | None = None,
        team_member_id: Incomplete | None = None,
    ) -> None: ...

UserInfo_validator: Incomplete

class ViewerInfoPolicy(bb.Union):
    enabled: Incomplete
    disabled: Incomplete
    other: Incomplete
    def is_enabled(self): ...
    def is_disabled(self): ...
    def is_other(self): ...

ViewerInfoPolicy_validator: Incomplete

class Visibility(bb.Union):
    public: Incomplete
    team_only: Incomplete
    password: Incomplete
    team_and_password: Incomplete
    shared_folder_only: Incomplete
    other: Incomplete
    def is_public(self): ...
    def is_team_only(self): ...
    def is_password(self): ...
    def is_team_and_password(self): ...
    def is_shared_folder_only(self): ...
    def is_other(self): ...

Visibility_validator: Incomplete

class VisibilityPolicy(bb.Struct):
    policy: Incomplete
    resolved_policy: Incomplete
    allowed: Incomplete
    disallowed_reason: Incomplete
    def __init__(
        self,
        policy: Incomplete | None = None,
        resolved_policy: Incomplete | None = None,
        allowed: Incomplete | None = None,
        disallowed_reason: Incomplete | None = None,
    ) -> None: ...

VisibilityPolicy_validator: Incomplete
DropboxId_validator: Incomplete
GetSharedLinkFileArg_validator = GetSharedLinkMetadataArg_validator
GetSharedLinkFileArg = GetSharedLinkMetadataArg
Id_validator: Incomplete
Path_validator: Incomplete
PathOrId_validator: Incomplete
ReadPath_validator: Incomplete
Rev_validator: Incomplete
TeamInfo_validator: Incomplete
TeamInfo = users.Team
add_file_member: Incomplete
add_folder_member: Incomplete
check_job_status: Incomplete
check_remove_member_job_status: Incomplete
check_share_job_status: Incomplete
create_shared_link: Incomplete
create_shared_link_with_settings: Incomplete
get_file_metadata: Incomplete
get_file_metadata_batch: Incomplete
get_folder_metadata: Incomplete
get_shared_link_file: Incomplete
get_shared_link_metadata: Incomplete
get_shared_links: Incomplete
list_file_members: Incomplete
list_file_members_batch: Incomplete
list_file_members_continue: Incomplete
list_folder_members: Incomplete
list_folder_members_continue: Incomplete
list_folders: Incomplete
list_folders_continue: Incomplete
list_mountable_folders: Incomplete
list_mountable_folders_continue: Incomplete
list_received_files: Incomplete
list_received_files_continue: Incomplete
list_shared_links: Incomplete
modify_shared_link_settings: Incomplete
mount_folder: Incomplete
relinquish_file_membership: Incomplete
relinquish_folder_membership: Incomplete
remove_file_member: Incomplete
remove_file_member_2: Incomplete
remove_folder_member: Incomplete
revoke_shared_link: Incomplete
set_access_inheritance: Incomplete
share_folder: Incomplete
transfer_folder: Incomplete
unmount_folder: Incomplete
unshare_file: Incomplete
unshare_folder: Incomplete
update_file_member: Incomplete
update_folder_member: Incomplete
update_folder_policy: Incomplete
ROUTES: Incomplete
