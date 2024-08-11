from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class AddMember(bb.Struct):
    permission_level: Incomplete
    member: Incomplete
    def __init__(self, member: Incomplete | None = None, permission_level: Incomplete | None = None) -> None: ...

AddMember_validator: Incomplete

class RefPaperDoc(bb.Struct):
    doc_id: Incomplete
    def __init__(self, doc_id: Incomplete | None = None) -> None: ...

RefPaperDoc_validator: Incomplete

class AddPaperDocUser(RefPaperDoc):
    members: Incomplete
    custom_message: Incomplete
    quiet: Incomplete
    def __init__(
        self,
        doc_id: Incomplete | None = None,
        members: Incomplete | None = None,
        custom_message: Incomplete | None = None,
        quiet: Incomplete | None = None,
    ) -> None: ...

AddPaperDocUser_validator: Incomplete

class AddPaperDocUserMemberResult(bb.Struct):
    member: Incomplete
    result: Incomplete
    def __init__(self, member: Incomplete | None = None, result: Incomplete | None = None) -> None: ...

AddPaperDocUserMemberResult_validator: Incomplete

class AddPaperDocUserResult(bb.Union):
    success: Incomplete
    unknown_error: Incomplete
    sharing_outside_team_disabled: Incomplete
    daily_limit_reached: Incomplete
    user_is_owner: Incomplete
    failed_user_data_retrieval: Incomplete
    permission_already_granted: Incomplete
    other: Incomplete
    def is_success(self): ...
    def is_unknown_error(self): ...
    def is_sharing_outside_team_disabled(self): ...
    def is_daily_limit_reached(self): ...
    def is_user_is_owner(self): ...
    def is_failed_user_data_retrieval(self): ...
    def is_permission_already_granted(self): ...
    def is_other(self): ...

AddPaperDocUserResult_validator: Incomplete

class Cursor(bb.Struct):
    value: Incomplete
    expiration: Incomplete
    def __init__(self, value: Incomplete | None = None, expiration: Incomplete | None = None) -> None: ...

Cursor_validator: Incomplete

class PaperApiBaseError(bb.Union):
    insufficient_permissions: Incomplete
    other: Incomplete
    def is_insufficient_permissions(self): ...
    def is_other(self): ...

PaperApiBaseError_validator: Incomplete

class DocLookupError(PaperApiBaseError):
    doc_not_found: Incomplete
    def is_doc_not_found(self): ...

DocLookupError_validator: Incomplete

class DocSubscriptionLevel(bb.Union):
    default: Incomplete
    ignore: Incomplete
    every: Incomplete
    no_email: Incomplete
    def is_default(self): ...
    def is_ignore(self): ...
    def is_every(self): ...
    def is_no_email(self): ...

DocSubscriptionLevel_validator: Incomplete

class ExportFormat(bb.Union):
    html: Incomplete
    markdown: Incomplete
    other: Incomplete
    def is_html(self): ...
    def is_markdown(self): ...
    def is_other(self): ...

ExportFormat_validator: Incomplete

class Folder(bb.Struct):
    id: Incomplete
    name: Incomplete
    def __init__(self, id: Incomplete | None = None, name: Incomplete | None = None) -> None: ...

Folder_validator: Incomplete

class FolderSharingPolicyType(bb.Union):
    team: Incomplete
    invite_only: Incomplete
    def is_team(self): ...
    def is_invite_only(self): ...

FolderSharingPolicyType_validator: Incomplete

class FolderSubscriptionLevel(bb.Union):
    none: Incomplete
    activity_only: Incomplete
    daily_emails: Incomplete
    weekly_emails: Incomplete
    def is_none(self): ...
    def is_activity_only(self): ...
    def is_daily_emails(self): ...
    def is_weekly_emails(self): ...

FolderSubscriptionLevel_validator: Incomplete

class FoldersContainingPaperDoc(bb.Struct):
    folder_sharing_policy_type: Incomplete
    folders: Incomplete
    def __init__(self, folder_sharing_policy_type: Incomplete | None = None, folders: Incomplete | None = None) -> None: ...

FoldersContainingPaperDoc_validator: Incomplete

class ImportFormat(bb.Union):
    html: Incomplete
    markdown: Incomplete
    plain_text: Incomplete
    other: Incomplete
    def is_html(self): ...
    def is_markdown(self): ...
    def is_plain_text(self): ...
    def is_other(self): ...

ImportFormat_validator: Incomplete

class InviteeInfoWithPermissionLevel(bb.Struct):
    invitee: Incomplete
    permission_level: Incomplete
    def __init__(self, invitee: Incomplete | None = None, permission_level: Incomplete | None = None) -> None: ...

InviteeInfoWithPermissionLevel_validator: Incomplete

class ListDocsCursorError(bb.Union):
    other: Incomplete
    @classmethod
    def cursor_error(cls, val): ...
    def is_cursor_error(self): ...
    def is_other(self): ...
    def get_cursor_error(self): ...

ListDocsCursorError_validator: Incomplete

class ListPaperDocsArgs(bb.Struct):
    filter_by: Incomplete
    sort_by: Incomplete
    sort_order: Incomplete
    limit: Incomplete
    def __init__(
        self,
        filter_by: Incomplete | None = None,
        sort_by: Incomplete | None = None,
        sort_order: Incomplete | None = None,
        limit: Incomplete | None = None,
    ) -> None: ...

ListPaperDocsArgs_validator: Incomplete

class ListPaperDocsContinueArgs(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

ListPaperDocsContinueArgs_validator: Incomplete

class ListPaperDocsFilterBy(bb.Union):
    docs_accessed: Incomplete
    docs_created: Incomplete
    other: Incomplete
    def is_docs_accessed(self): ...
    def is_docs_created(self): ...
    def is_other(self): ...

ListPaperDocsFilterBy_validator: Incomplete

class ListPaperDocsResponse(bb.Struct):
    doc_ids: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self, doc_ids: Incomplete | None = None, cursor: Incomplete | None = None, has_more: Incomplete | None = None
    ) -> None: ...

ListPaperDocsResponse_validator: Incomplete

class ListPaperDocsSortBy(bb.Union):
    accessed: Incomplete
    modified: Incomplete
    created: Incomplete
    other: Incomplete
    def is_accessed(self): ...
    def is_modified(self): ...
    def is_created(self): ...
    def is_other(self): ...

ListPaperDocsSortBy_validator: Incomplete

class ListPaperDocsSortOrder(bb.Union):
    ascending: Incomplete
    descending: Incomplete
    other: Incomplete
    def is_ascending(self): ...
    def is_descending(self): ...
    def is_other(self): ...

ListPaperDocsSortOrder_validator: Incomplete

class ListUsersCursorError(PaperApiBaseError):
    doc_not_found: Incomplete
    @classmethod
    def cursor_error(cls, val): ...
    def is_doc_not_found(self): ...
    def is_cursor_error(self): ...
    def get_cursor_error(self): ...

ListUsersCursorError_validator: Incomplete

class ListUsersOnFolderArgs(RefPaperDoc):
    limit: Incomplete
    def __init__(self, doc_id: Incomplete | None = None, limit: Incomplete | None = None) -> None: ...

ListUsersOnFolderArgs_validator: Incomplete

class ListUsersOnFolderContinueArgs(RefPaperDoc):
    cursor: Incomplete
    def __init__(self, doc_id: Incomplete | None = None, cursor: Incomplete | None = None) -> None: ...

ListUsersOnFolderContinueArgs_validator: Incomplete

class ListUsersOnFolderResponse(bb.Struct):
    invitees: Incomplete
    users: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self,
        invitees: Incomplete | None = None,
        users: Incomplete | None = None,
        cursor: Incomplete | None = None,
        has_more: Incomplete | None = None,
    ) -> None: ...

ListUsersOnFolderResponse_validator: Incomplete

class ListUsersOnPaperDocArgs(RefPaperDoc):
    limit: Incomplete
    filter_by: Incomplete
    def __init__(
        self, doc_id: Incomplete | None = None, limit: Incomplete | None = None, filter_by: Incomplete | None = None
    ) -> None: ...

ListUsersOnPaperDocArgs_validator: Incomplete

class ListUsersOnPaperDocContinueArgs(RefPaperDoc):
    cursor: Incomplete
    def __init__(self, doc_id: Incomplete | None = None, cursor: Incomplete | None = None) -> None: ...

ListUsersOnPaperDocContinueArgs_validator: Incomplete

class ListUsersOnPaperDocResponse(bb.Struct):
    invitees: Incomplete
    users: Incomplete
    doc_owner: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self,
        invitees: Incomplete | None = None,
        users: Incomplete | None = None,
        doc_owner: Incomplete | None = None,
        cursor: Incomplete | None = None,
        has_more: Incomplete | None = None,
    ) -> None: ...

ListUsersOnPaperDocResponse_validator: Incomplete

class PaperApiCursorError(bb.Union):
    expired_cursor: Incomplete
    invalid_cursor: Incomplete
    wrong_user_in_cursor: Incomplete
    reset: Incomplete
    other: Incomplete
    def is_expired_cursor(self): ...
    def is_invalid_cursor(self): ...
    def is_wrong_user_in_cursor(self): ...
    def is_reset(self): ...
    def is_other(self): ...

PaperApiCursorError_validator: Incomplete

class PaperDocCreateArgs(bb.Struct):
    parent_folder_id: Incomplete
    import_format: Incomplete
    def __init__(self, import_format: Incomplete | None = None, parent_folder_id: Incomplete | None = None) -> None: ...

PaperDocCreateArgs_validator: Incomplete

class PaperDocCreateError(PaperApiBaseError):
    content_malformed: Incomplete
    folder_not_found: Incomplete
    doc_length_exceeded: Incomplete
    image_size_exceeded: Incomplete
    def is_content_malformed(self): ...
    def is_folder_not_found(self): ...
    def is_doc_length_exceeded(self): ...
    def is_image_size_exceeded(self): ...

PaperDocCreateError_validator: Incomplete

class PaperDocCreateUpdateResult(bb.Struct):
    doc_id: Incomplete
    revision: Incomplete
    title: Incomplete
    def __init__(
        self, doc_id: Incomplete | None = None, revision: Incomplete | None = None, title: Incomplete | None = None
    ) -> None: ...

PaperDocCreateUpdateResult_validator: Incomplete

class PaperDocExport(RefPaperDoc):
    export_format: Incomplete
    def __init__(self, doc_id: Incomplete | None = None, export_format: Incomplete | None = None) -> None: ...

PaperDocExport_validator: Incomplete

class PaperDocExportResult(bb.Struct):
    owner: Incomplete
    title: Incomplete
    revision: Incomplete
    mime_type: Incomplete
    def __init__(
        self,
        owner: Incomplete | None = None,
        title: Incomplete | None = None,
        revision: Incomplete | None = None,
        mime_type: Incomplete | None = None,
    ) -> None: ...

PaperDocExportResult_validator: Incomplete

class PaperDocPermissionLevel(bb.Union):
    edit: Incomplete
    view_and_comment: Incomplete
    other: Incomplete
    def is_edit(self): ...
    def is_view_and_comment(self): ...
    def is_other(self): ...

PaperDocPermissionLevel_validator: Incomplete

class PaperDocSharingPolicy(RefPaperDoc):
    sharing_policy: Incomplete
    def __init__(self, doc_id: Incomplete | None = None, sharing_policy: Incomplete | None = None) -> None: ...

PaperDocSharingPolicy_validator: Incomplete

class PaperDocUpdateArgs(RefPaperDoc):
    doc_update_policy: Incomplete
    revision: Incomplete
    import_format: Incomplete
    def __init__(
        self,
        doc_id: Incomplete | None = None,
        doc_update_policy: Incomplete | None = None,
        revision: Incomplete | None = None,
        import_format: Incomplete | None = None,
    ) -> None: ...

PaperDocUpdateArgs_validator: Incomplete

class PaperDocUpdateError(DocLookupError):
    content_malformed: Incomplete
    revision_mismatch: Incomplete
    doc_length_exceeded: Incomplete
    image_size_exceeded: Incomplete
    doc_archived: Incomplete
    doc_deleted: Incomplete
    def is_content_malformed(self): ...
    def is_revision_mismatch(self): ...
    def is_doc_length_exceeded(self): ...
    def is_image_size_exceeded(self): ...
    def is_doc_archived(self): ...
    def is_doc_deleted(self): ...

PaperDocUpdateError_validator: Incomplete

class PaperDocUpdatePolicy(bb.Union):
    append: Incomplete
    prepend: Incomplete
    overwrite_all: Incomplete
    other: Incomplete
    def is_append(self): ...
    def is_prepend(self): ...
    def is_overwrite_all(self): ...
    def is_other(self): ...

PaperDocUpdatePolicy_validator: Incomplete

class PaperFolderCreateArg(bb.Struct):
    name: Incomplete
    parent_folder_id: Incomplete
    is_team_folder: Incomplete
    def __init__(
        self, name: Incomplete | None = None, parent_folder_id: Incomplete | None = None, is_team_folder: Incomplete | None = None
    ) -> None: ...

PaperFolderCreateArg_validator: Incomplete

class PaperFolderCreateError(PaperApiBaseError):
    folder_not_found: Incomplete
    invalid_folder_id: Incomplete
    def is_folder_not_found(self): ...
    def is_invalid_folder_id(self): ...

PaperFolderCreateError_validator: Incomplete

class PaperFolderCreateResult(bb.Struct):
    folder_id: Incomplete
    def __init__(self, folder_id: Incomplete | None = None) -> None: ...

PaperFolderCreateResult_validator: Incomplete

class RemovePaperDocUser(RefPaperDoc):
    member: Incomplete
    def __init__(self, doc_id: Incomplete | None = None, member: Incomplete | None = None) -> None: ...

RemovePaperDocUser_validator: Incomplete

class SharingPolicy(bb.Struct):
    public_sharing_policy: Incomplete
    team_sharing_policy: Incomplete
    def __init__(
        self, public_sharing_policy: Incomplete | None = None, team_sharing_policy: Incomplete | None = None
    ) -> None: ...

SharingPolicy_validator: Incomplete

class SharingTeamPolicyType(bb.Union):
    people_with_link_can_edit: Incomplete
    people_with_link_can_view_and_comment: Incomplete
    invite_only: Incomplete
    def is_people_with_link_can_edit(self): ...
    def is_people_with_link_can_view_and_comment(self): ...
    def is_invite_only(self): ...

SharingTeamPolicyType_validator: Incomplete

class SharingPublicPolicyType(SharingTeamPolicyType):
    disabled: Incomplete
    def is_disabled(self): ...

SharingPublicPolicyType_validator: Incomplete

class UserInfoWithPermissionLevel(bb.Struct):
    user: Incomplete
    permission_level: Incomplete
    def __init__(self, user: Incomplete | None = None, permission_level: Incomplete | None = None) -> None: ...

UserInfoWithPermissionLevel_validator: Incomplete

class UserOnPaperDocFilter(bb.Union):
    visited: Incomplete
    shared: Incomplete
    other: Incomplete
    def is_visited(self): ...
    def is_shared(self): ...
    def is_other(self): ...

UserOnPaperDocFilter_validator: Incomplete
PaperDocId_validator: Incomplete
docs_archive: Incomplete
docs_create: Incomplete
docs_download: Incomplete
docs_folder_users_list: Incomplete
docs_folder_users_list_continue: Incomplete
docs_get_folder_info: Incomplete
docs_list: Incomplete
docs_list_continue: Incomplete
docs_permanently_delete: Incomplete
docs_sharing_policy_get: Incomplete
docs_sharing_policy_set: Incomplete
docs_update: Incomplete
docs_users_add: Incomplete
docs_users_list: Incomplete
docs_users_list_continue: Incomplete
docs_users_remove: Incomplete
folders_create: Incomplete
ROUTES: Incomplete
