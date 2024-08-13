from _typeshed import Incomplete

from dropbox import async_
from stone.backends.python_rsrc import stone_base as bb

class AddTagArg(bb.Struct):
    path: Incomplete
    tag_text: Incomplete
    def __init__(self, path: Incomplete | None = None, tag_text: Incomplete | None = None) -> None: ...

AddTagArg_validator: Incomplete

class BaseTagError(bb.Union):
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_other(self): ...
    def get_path(self): ...

BaseTagError_validator: Incomplete

class AddTagError(BaseTagError):
    too_many_tags: Incomplete
    def is_too_many_tags(self): ...

AddTagError_validator: Incomplete

class GetMetadataArg(bb.Struct):
    path: Incomplete
    include_media_info: Incomplete
    include_deleted: Incomplete
    include_has_explicit_shared_members: Incomplete
    include_property_groups: Incomplete
    def __init__(
        self,
        path: Incomplete | None = None,
        include_media_info: Incomplete | None = None,
        include_deleted: Incomplete | None = None,
        include_has_explicit_shared_members: Incomplete | None = None,
        include_property_groups: Incomplete | None = None,
    ) -> None: ...

GetMetadataArg_validator: Incomplete

class AlphaGetMetadataArg(GetMetadataArg):
    include_property_templates: Incomplete
    def __init__(
        self,
        path: Incomplete | None = None,
        include_media_info: Incomplete | None = None,
        include_deleted: Incomplete | None = None,
        include_has_explicit_shared_members: Incomplete | None = None,
        include_property_groups: Incomplete | None = None,
        include_property_templates: Incomplete | None = None,
    ) -> None: ...

AlphaGetMetadataArg_validator: Incomplete

class GetMetadataError(bb.Union):
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def get_path(self): ...

GetMetadataError_validator: Incomplete

class AlphaGetMetadataError(GetMetadataError):
    @classmethod
    def properties_error(cls, val): ...
    def is_properties_error(self): ...
    def get_properties_error(self): ...

AlphaGetMetadataError_validator: Incomplete

class CommitInfo(bb.Struct):
    path: Incomplete
    mode: Incomplete
    autorename: Incomplete
    client_modified: Incomplete
    mute: Incomplete
    property_groups: Incomplete
    strict_conflict: Incomplete
    def __init__(
        self,
        path: Incomplete | None = None,
        mode: Incomplete | None = None,
        autorename: Incomplete | None = None,
        client_modified: Incomplete | None = None,
        mute: Incomplete | None = None,
        property_groups: Incomplete | None = None,
        strict_conflict: Incomplete | None = None,
    ) -> None: ...

CommitInfo_validator: Incomplete

class ContentSyncSetting(bb.Struct):
    id: Incomplete
    sync_setting: Incomplete
    def __init__(self, id: Incomplete | None = None, sync_setting: Incomplete | None = None) -> None: ...

ContentSyncSetting_validator: Incomplete

class ContentSyncSettingArg(bb.Struct):
    id: Incomplete
    sync_setting: Incomplete
    def __init__(self, id: Incomplete | None = None, sync_setting: Incomplete | None = None) -> None: ...

ContentSyncSettingArg_validator: Incomplete

class CreateFolderArg(bb.Struct):
    path: Incomplete
    autorename: Incomplete
    def __init__(self, path: Incomplete | None = None, autorename: Incomplete | None = None) -> None: ...

CreateFolderArg_validator: Incomplete

class CreateFolderBatchArg(bb.Struct):
    paths: Incomplete
    autorename: Incomplete
    force_async: Incomplete
    def __init__(
        self, paths: Incomplete | None = None, autorename: Incomplete | None = None, force_async: Incomplete | None = None
    ) -> None: ...

CreateFolderBatchArg_validator: Incomplete

class CreateFolderBatchError(bb.Union):
    too_many_files: Incomplete
    other: Incomplete
    def is_too_many_files(self): ...
    def is_other(self): ...

CreateFolderBatchError_validator: Incomplete

class CreateFolderBatchJobStatus(async_.PollResultBase):
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

CreateFolderBatchJobStatus_validator: Incomplete

class CreateFolderBatchLaunch(async_.LaunchResultBase):
    other: Incomplete
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def is_other(self): ...
    def get_complete(self): ...

CreateFolderBatchLaunch_validator: Incomplete

class FileOpsResult(bb.Struct):
    def __init__(self) -> None: ...

FileOpsResult_validator: Incomplete

class CreateFolderBatchResult(FileOpsResult):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

CreateFolderBatchResult_validator: Incomplete

class CreateFolderBatchResultEntry(bb.Union):
    @classmethod
    def success(cls, val): ...
    @classmethod
    def failure(cls, val): ...
    def is_success(self): ...
    def is_failure(self): ...
    def get_success(self): ...
    def get_failure(self): ...

CreateFolderBatchResultEntry_validator: Incomplete

class CreateFolderEntryError(bb.Union):
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_other(self): ...
    def get_path(self): ...

CreateFolderEntryError_validator: Incomplete

class CreateFolderEntryResult(bb.Struct):
    metadata: Incomplete
    def __init__(self, metadata: Incomplete | None = None) -> None: ...

CreateFolderEntryResult_validator: Incomplete

class CreateFolderError(bb.Union):
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def get_path(self): ...

CreateFolderError_validator: Incomplete

class CreateFolderResult(FileOpsResult):
    metadata: Incomplete
    def __init__(self, metadata: Incomplete | None = None) -> None: ...

CreateFolderResult_validator: Incomplete

class DeleteArg(bb.Struct):
    path: Incomplete
    parent_rev: Incomplete
    def __init__(self, path: Incomplete | None = None, parent_rev: Incomplete | None = None) -> None: ...

DeleteArg_validator: Incomplete

class DeleteBatchArg(bb.Struct):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

DeleteBatchArg_validator: Incomplete

class DeleteBatchError(bb.Union):
    too_many_write_operations: Incomplete
    other: Incomplete
    def is_too_many_write_operations(self): ...
    def is_other(self): ...

DeleteBatchError_validator: Incomplete

class DeleteBatchJobStatus(async_.PollResultBase):
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

DeleteBatchJobStatus_validator: Incomplete

class DeleteBatchLaunch(async_.LaunchResultBase):
    other: Incomplete
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def is_other(self): ...
    def get_complete(self): ...

DeleteBatchLaunch_validator: Incomplete

class DeleteBatchResult(FileOpsResult):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

DeleteBatchResult_validator: Incomplete

class DeleteBatchResultData(bb.Struct):
    metadata: Incomplete
    def __init__(self, metadata: Incomplete | None = None) -> None: ...

DeleteBatchResultData_validator: Incomplete

class DeleteBatchResultEntry(bb.Union):
    @classmethod
    def success(cls, val): ...
    @classmethod
    def failure(cls, val): ...
    def is_success(self): ...
    def is_failure(self): ...
    def get_success(self): ...
    def get_failure(self): ...

DeleteBatchResultEntry_validator: Incomplete

class DeleteError(bb.Union):
    too_many_write_operations: Incomplete
    too_many_files: Incomplete
    other: Incomplete
    @classmethod
    def path_lookup(cls, val): ...
    @classmethod
    def path_write(cls, val): ...
    def is_path_lookup(self): ...
    def is_path_write(self): ...
    def is_too_many_write_operations(self): ...
    def is_too_many_files(self): ...
    def is_other(self): ...
    def get_path_lookup(self): ...
    def get_path_write(self): ...

DeleteError_validator: Incomplete

class DeleteResult(FileOpsResult):
    metadata: Incomplete
    def __init__(self, metadata: Incomplete | None = None) -> None: ...

DeleteResult_validator: Incomplete

class Metadata(bb.Struct):
    name: Incomplete
    path_lower: Incomplete
    path_display: Incomplete
    parent_shared_folder_id: Incomplete
    preview_url: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        path_lower: Incomplete | None = None,
        path_display: Incomplete | None = None,
        parent_shared_folder_id: Incomplete | None = None,
        preview_url: Incomplete | None = None,
    ) -> None: ...

Metadata_validator: Incomplete

class DeletedMetadata(Metadata):
    def __init__(
        self,
        name: Incomplete | None = None,
        path_lower: Incomplete | None = None,
        path_display: Incomplete | None = None,
        parent_shared_folder_id: Incomplete | None = None,
        preview_url: Incomplete | None = None,
    ) -> None: ...

DeletedMetadata_validator: Incomplete

class Dimensions(bb.Struct):
    height: Incomplete
    width: Incomplete
    def __init__(self, height: Incomplete | None = None, width: Incomplete | None = None) -> None: ...

Dimensions_validator: Incomplete

class DownloadArg(bb.Struct):
    path: Incomplete
    rev: Incomplete
    def __init__(self, path: Incomplete | None = None, rev: Incomplete | None = None) -> None: ...

DownloadArg_validator: Incomplete

class DownloadError(bb.Union):
    unsupported_file: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_unsupported_file(self): ...
    def is_other(self): ...
    def get_path(self): ...

DownloadError_validator: Incomplete

class DownloadZipArg(bb.Struct):
    path: Incomplete
    def __init__(self, path: Incomplete | None = None) -> None: ...

DownloadZipArg_validator: Incomplete

class DownloadZipError(bb.Union):
    too_large: Incomplete
    too_many_files: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_too_large(self): ...
    def is_too_many_files(self): ...
    def is_other(self): ...
    def get_path(self): ...

DownloadZipError_validator: Incomplete

class DownloadZipResult(bb.Struct):
    metadata: Incomplete
    def __init__(self, metadata: Incomplete | None = None) -> None: ...

DownloadZipResult_validator: Incomplete

class ExportArg(bb.Struct):
    path: Incomplete
    export_format: Incomplete
    def __init__(self, path: Incomplete | None = None, export_format: Incomplete | None = None) -> None: ...

ExportArg_validator: Incomplete

class ExportError(bb.Union):
    non_exportable: Incomplete
    invalid_export_format: Incomplete
    retry_error: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_non_exportable(self): ...
    def is_invalid_export_format(self): ...
    def is_retry_error(self): ...
    def is_other(self): ...
    def get_path(self): ...

ExportError_validator: Incomplete

class ExportInfo(bb.Struct):
    export_as: Incomplete
    export_options: Incomplete
    def __init__(self, export_as: Incomplete | None = None, export_options: Incomplete | None = None) -> None: ...

ExportInfo_validator: Incomplete

class ExportMetadata(bb.Struct):
    name: Incomplete
    size: Incomplete
    export_hash: Incomplete
    paper_revision: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        size: Incomplete | None = None,
        export_hash: Incomplete | None = None,
        paper_revision: Incomplete | None = None,
    ) -> None: ...

ExportMetadata_validator: Incomplete

class ExportResult(bb.Struct):
    export_metadata: Incomplete
    file_metadata: Incomplete
    def __init__(self, export_metadata: Incomplete | None = None, file_metadata: Incomplete | None = None) -> None: ...

ExportResult_validator: Incomplete

class FileCategory(bb.Union):
    image: Incomplete
    document: Incomplete
    pdf: Incomplete
    spreadsheet: Incomplete
    presentation: Incomplete
    audio: Incomplete
    video: Incomplete
    folder: Incomplete
    paper: Incomplete
    others: Incomplete
    other: Incomplete
    def is_image(self): ...
    def is_document(self): ...
    def is_pdf(self): ...
    def is_spreadsheet(self): ...
    def is_presentation(self): ...
    def is_audio(self): ...
    def is_video(self): ...
    def is_folder(self): ...
    def is_paper(self): ...
    def is_others(self): ...
    def is_other(self): ...

FileCategory_validator: Incomplete

class FileLock(bb.Struct):
    content: Incomplete
    def __init__(self, content: Incomplete | None = None) -> None: ...

FileLock_validator: Incomplete

class FileLockContent(bb.Union):
    unlocked: Incomplete
    other: Incomplete
    @classmethod
    def single_user(cls, val): ...
    def is_unlocked(self): ...
    def is_single_user(self): ...
    def is_other(self): ...
    def get_single_user(self): ...

FileLockContent_validator: Incomplete

class FileLockMetadata(bb.Struct):
    is_lockholder: Incomplete
    lockholder_name: Incomplete
    lockholder_account_id: Incomplete
    created: Incomplete
    def __init__(
        self,
        is_lockholder: Incomplete | None = None,
        lockholder_name: Incomplete | None = None,
        lockholder_account_id: Incomplete | None = None,
        created: Incomplete | None = None,
    ) -> None: ...

FileLockMetadata_validator: Incomplete

class FileMetadata(Metadata):
    id: Incomplete
    client_modified: Incomplete
    server_modified: Incomplete
    rev: Incomplete
    size: Incomplete
    media_info: Incomplete
    symlink_info: Incomplete
    sharing_info: Incomplete
    is_downloadable: Incomplete
    export_info: Incomplete
    property_groups: Incomplete
    has_explicit_shared_members: Incomplete
    content_hash: Incomplete
    file_lock_info: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        id: Incomplete | None = None,
        client_modified: Incomplete | None = None,
        server_modified: Incomplete | None = None,
        rev: Incomplete | None = None,
        size: Incomplete | None = None,
        path_lower: Incomplete | None = None,
        path_display: Incomplete | None = None,
        parent_shared_folder_id: Incomplete | None = None,
        preview_url: Incomplete | None = None,
        media_info: Incomplete | None = None,
        symlink_info: Incomplete | None = None,
        sharing_info: Incomplete | None = None,
        is_downloadable: Incomplete | None = None,
        export_info: Incomplete | None = None,
        property_groups: Incomplete | None = None,
        has_explicit_shared_members: Incomplete | None = None,
        content_hash: Incomplete | None = None,
        file_lock_info: Incomplete | None = None,
    ) -> None: ...

FileMetadata_validator: Incomplete

class SharingInfo(bb.Struct):
    read_only: Incomplete
    def __init__(self, read_only: Incomplete | None = None) -> None: ...

SharingInfo_validator: Incomplete

class FileSharingInfo(SharingInfo):
    parent_shared_folder_id: Incomplete
    modified_by: Incomplete
    def __init__(
        self,
        read_only: Incomplete | None = None,
        parent_shared_folder_id: Incomplete | None = None,
        modified_by: Incomplete | None = None,
    ) -> None: ...

FileSharingInfo_validator: Incomplete

class FileStatus(bb.Union):
    active: Incomplete
    deleted: Incomplete
    other: Incomplete
    def is_active(self): ...
    def is_deleted(self): ...
    def is_other(self): ...

FileStatus_validator: Incomplete

class FolderMetadata(Metadata):
    id: Incomplete
    shared_folder_id: Incomplete
    sharing_info: Incomplete
    property_groups: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        id: Incomplete | None = None,
        path_lower: Incomplete | None = None,
        path_display: Incomplete | None = None,
        parent_shared_folder_id: Incomplete | None = None,
        preview_url: Incomplete | None = None,
        shared_folder_id: Incomplete | None = None,
        sharing_info: Incomplete | None = None,
        property_groups: Incomplete | None = None,
    ) -> None: ...

FolderMetadata_validator: Incomplete

class FolderSharingInfo(SharingInfo):
    parent_shared_folder_id: Incomplete
    shared_folder_id: Incomplete
    traverse_only: Incomplete
    no_access: Incomplete
    def __init__(
        self,
        read_only: Incomplete | None = None,
        parent_shared_folder_id: Incomplete | None = None,
        shared_folder_id: Incomplete | None = None,
        traverse_only: Incomplete | None = None,
        no_access: Incomplete | None = None,
    ) -> None: ...

FolderSharingInfo_validator: Incomplete

class GetCopyReferenceArg(bb.Struct):
    path: Incomplete
    def __init__(self, path: Incomplete | None = None) -> None: ...

GetCopyReferenceArg_validator: Incomplete

class GetCopyReferenceError(bb.Union):
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_other(self): ...
    def get_path(self): ...

GetCopyReferenceError_validator: Incomplete

class GetCopyReferenceResult(bb.Struct):
    metadata: Incomplete
    copy_reference: Incomplete
    expires: Incomplete
    def __init__(
        self, metadata: Incomplete | None = None, copy_reference: Incomplete | None = None, expires: Incomplete | None = None
    ) -> None: ...

GetCopyReferenceResult_validator: Incomplete

class GetTagsArg(bb.Struct):
    paths: Incomplete
    def __init__(self, paths: Incomplete | None = None) -> None: ...

GetTagsArg_validator: Incomplete

class GetTagsResult(bb.Struct):
    paths_to_tags: Incomplete
    def __init__(self, paths_to_tags: Incomplete | None = None) -> None: ...

GetTagsResult_validator: Incomplete

class GetTemporaryLinkArg(bb.Struct):
    path: Incomplete
    def __init__(self, path: Incomplete | None = None) -> None: ...

GetTemporaryLinkArg_validator: Incomplete

class GetTemporaryLinkError(bb.Union):
    email_not_verified: Incomplete
    unsupported_file: Incomplete
    not_allowed: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_email_not_verified(self): ...
    def is_unsupported_file(self): ...
    def is_not_allowed(self): ...
    def is_other(self): ...
    def get_path(self): ...

GetTemporaryLinkError_validator: Incomplete

class GetTemporaryLinkResult(bb.Struct):
    metadata: Incomplete
    link: Incomplete
    def __init__(self, metadata: Incomplete | None = None, link: Incomplete | None = None) -> None: ...

GetTemporaryLinkResult_validator: Incomplete

class GetTemporaryUploadLinkArg(bb.Struct):
    commit_info: Incomplete
    duration: Incomplete
    def __init__(self, commit_info: Incomplete | None = None, duration: Incomplete | None = None) -> None: ...

GetTemporaryUploadLinkArg_validator: Incomplete

class GetTemporaryUploadLinkResult(bb.Struct):
    link: Incomplete
    def __init__(self, link: Incomplete | None = None) -> None: ...

GetTemporaryUploadLinkResult_validator: Incomplete

class GetThumbnailBatchArg(bb.Struct):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

GetThumbnailBatchArg_validator: Incomplete

class GetThumbnailBatchError(bb.Union):
    too_many_files: Incomplete
    other: Incomplete
    def is_too_many_files(self): ...
    def is_other(self): ...

GetThumbnailBatchError_validator: Incomplete

class GetThumbnailBatchResult(bb.Struct):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

GetThumbnailBatchResult_validator: Incomplete

class GetThumbnailBatchResultData(bb.Struct):
    metadata: Incomplete
    thumbnail: Incomplete
    def __init__(self, metadata: Incomplete | None = None, thumbnail: Incomplete | None = None) -> None: ...

GetThumbnailBatchResultData_validator: Incomplete

class GetThumbnailBatchResultEntry(bb.Union):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    @classmethod
    def failure(cls, val): ...
    def is_success(self): ...
    def is_failure(self): ...
    def is_other(self): ...
    def get_success(self): ...
    def get_failure(self): ...

GetThumbnailBatchResultEntry_validator: Incomplete

class GpsCoordinates(bb.Struct):
    latitude: Incomplete
    longitude: Incomplete
    def __init__(self, latitude: Incomplete | None = None, longitude: Incomplete | None = None) -> None: ...

GpsCoordinates_validator: Incomplete

class HighlightSpan(bb.Struct):
    highlight_str: Incomplete
    is_highlighted: Incomplete
    def __init__(self, highlight_str: Incomplete | None = None, is_highlighted: Incomplete | None = None) -> None: ...

HighlightSpan_validator: Incomplete

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

class ListFolderArg(bb.Struct):
    path: Incomplete
    recursive: Incomplete
    include_media_info: Incomplete
    include_deleted: Incomplete
    include_has_explicit_shared_members: Incomplete
    include_mounted_folders: Incomplete
    limit: Incomplete
    shared_link: Incomplete
    include_property_groups: Incomplete
    include_non_downloadable_files: Incomplete
    def __init__(
        self,
        path: Incomplete | None = None,
        recursive: Incomplete | None = None,
        include_media_info: Incomplete | None = None,
        include_deleted: Incomplete | None = None,
        include_has_explicit_shared_members: Incomplete | None = None,
        include_mounted_folders: Incomplete | None = None,
        limit: Incomplete | None = None,
        shared_link: Incomplete | None = None,
        include_property_groups: Incomplete | None = None,
        include_non_downloadable_files: Incomplete | None = None,
    ) -> None: ...

ListFolderArg_validator: Incomplete

class ListFolderContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

ListFolderContinueArg_validator: Incomplete

class ListFolderContinueError(bb.Union):
    reset: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_reset(self): ...
    def is_other(self): ...
    def get_path(self): ...

ListFolderContinueError_validator: Incomplete

class ListFolderError(bb.Union):
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    @classmethod
    def template_error(cls, val): ...
    def is_path(self): ...
    def is_template_error(self): ...
    def is_other(self): ...
    def get_path(self): ...
    def get_template_error(self): ...

ListFolderError_validator: Incomplete

class ListFolderGetLatestCursorResult(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

ListFolderGetLatestCursorResult_validator: Incomplete

class ListFolderLongpollArg(bb.Struct):
    cursor: Incomplete
    timeout: Incomplete
    def __init__(self, cursor: Incomplete | None = None, timeout: Incomplete | None = None) -> None: ...

ListFolderLongpollArg_validator: Incomplete

class ListFolderLongpollError(bb.Union):
    reset: Incomplete
    other: Incomplete
    def is_reset(self): ...
    def is_other(self): ...

ListFolderLongpollError_validator: Incomplete

class ListFolderLongpollResult(bb.Struct):
    changes: Incomplete
    backoff: Incomplete
    def __init__(self, changes: Incomplete | None = None, backoff: Incomplete | None = None) -> None: ...

ListFolderLongpollResult_validator: Incomplete

class ListFolderResult(bb.Struct):
    entries: Incomplete
    cursor: Incomplete
    has_more: Incomplete
    def __init__(
        self, entries: Incomplete | None = None, cursor: Incomplete | None = None, has_more: Incomplete | None = None
    ) -> None: ...

ListFolderResult_validator: Incomplete

class ListRevisionsArg(bb.Struct):
    path: Incomplete
    mode: Incomplete
    limit: Incomplete
    def __init__(
        self, path: Incomplete | None = None, mode: Incomplete | None = None, limit: Incomplete | None = None
    ) -> None: ...

ListRevisionsArg_validator: Incomplete

class ListRevisionsError(bb.Union):
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_other(self): ...
    def get_path(self): ...

ListRevisionsError_validator: Incomplete

class ListRevisionsMode(bb.Union):
    path: Incomplete
    id: Incomplete
    other: Incomplete
    def is_path(self): ...
    def is_id(self): ...
    def is_other(self): ...

ListRevisionsMode_validator: Incomplete

class ListRevisionsResult(bb.Struct):
    is_deleted: Incomplete
    server_deleted: Incomplete
    entries: Incomplete
    def __init__(
        self, is_deleted: Incomplete | None = None, entries: Incomplete | None = None, server_deleted: Incomplete | None = None
    ) -> None: ...

ListRevisionsResult_validator: Incomplete

class LockConflictError(bb.Struct):
    lock: Incomplete
    def __init__(self, lock: Incomplete | None = None) -> None: ...

LockConflictError_validator: Incomplete

class LockFileArg(bb.Struct):
    path: Incomplete
    def __init__(self, path: Incomplete | None = None) -> None: ...

LockFileArg_validator: Incomplete

class LockFileBatchArg(bb.Struct):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

LockFileBatchArg_validator: Incomplete

class LockFileBatchResult(FileOpsResult):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

LockFileBatchResult_validator: Incomplete

class LockFileError(bb.Union):
    too_many_write_operations: Incomplete
    too_many_files: Incomplete
    no_write_permission: Incomplete
    cannot_be_locked: Incomplete
    file_not_shared: Incomplete
    internal_error: Incomplete
    other: Incomplete
    @classmethod
    def path_lookup(cls, val): ...
    @classmethod
    def lock_conflict(cls, val): ...
    def is_path_lookup(self): ...
    def is_too_many_write_operations(self): ...
    def is_too_many_files(self): ...
    def is_no_write_permission(self): ...
    def is_cannot_be_locked(self): ...
    def is_file_not_shared(self): ...
    def is_lock_conflict(self): ...
    def is_internal_error(self): ...
    def is_other(self): ...
    def get_path_lookup(self): ...
    def get_lock_conflict(self): ...

LockFileError_validator: Incomplete

class LockFileResult(bb.Struct):
    metadata: Incomplete
    lock: Incomplete
    def __init__(self, metadata: Incomplete | None = None, lock: Incomplete | None = None) -> None: ...

LockFileResult_validator: Incomplete

class LockFileResultEntry(bb.Union):
    @classmethod
    def success(cls, val): ...
    @classmethod
    def failure(cls, val): ...
    def is_success(self): ...
    def is_failure(self): ...
    def get_success(self): ...
    def get_failure(self): ...

LockFileResultEntry_validator: Incomplete

class LookupError(bb.Union):
    not_found: Incomplete
    not_file: Incomplete
    not_folder: Incomplete
    restricted_content: Incomplete
    unsupported_content_type: Incomplete
    locked: Incomplete
    other: Incomplete
    @classmethod
    def malformed_path(cls, val): ...
    def is_malformed_path(self): ...
    def is_not_found(self): ...
    def is_not_file(self): ...
    def is_not_folder(self): ...
    def is_restricted_content(self): ...
    def is_unsupported_content_type(self): ...
    def is_locked(self): ...
    def is_other(self): ...
    def get_malformed_path(self): ...

LookupError_validator: Incomplete

class MediaInfo(bb.Union):
    pending: Incomplete
    @classmethod
    def metadata(cls, val): ...
    def is_pending(self): ...
    def is_metadata(self): ...
    def get_metadata(self): ...

MediaInfo_validator: Incomplete

class MediaMetadata(bb.Struct):
    dimensions: Incomplete
    location: Incomplete
    time_taken: Incomplete
    def __init__(
        self, dimensions: Incomplete | None = None, location: Incomplete | None = None, time_taken: Incomplete | None = None
    ) -> None: ...

MediaMetadata_validator: Incomplete

class MetadataV2(bb.Union):
    other: Incomplete
    @classmethod
    def metadata(cls, val): ...
    def is_metadata(self): ...
    def is_other(self): ...
    def get_metadata(self): ...

MetadataV2_validator: Incomplete

class MinimalFileLinkMetadata(bb.Struct):
    url: Incomplete
    id: Incomplete
    path: Incomplete
    rev: Incomplete
    def __init__(
        self,
        url: Incomplete | None = None,
        rev: Incomplete | None = None,
        id: Incomplete | None = None,
        path: Incomplete | None = None,
    ) -> None: ...

MinimalFileLinkMetadata_validator: Incomplete

class RelocationBatchArgBase(bb.Struct):
    entries: Incomplete
    autorename: Incomplete
    def __init__(self, entries: Incomplete | None = None, autorename: Incomplete | None = None) -> None: ...

RelocationBatchArgBase_validator: Incomplete

class MoveBatchArg(RelocationBatchArgBase):
    allow_ownership_transfer: Incomplete
    def __init__(
        self,
        entries: Incomplete | None = None,
        autorename: Incomplete | None = None,
        allow_ownership_transfer: Incomplete | None = None,
    ) -> None: ...

MoveBatchArg_validator: Incomplete

class MoveIntoFamilyError(bb.Union):
    is_shared_folder: Incomplete
    other: Incomplete
    def is_is_shared_folder(self): ...
    def is_other(self): ...

MoveIntoFamilyError_validator: Incomplete

class MoveIntoVaultError(bb.Union):
    is_shared_folder: Incomplete
    other: Incomplete
    def is_is_shared_folder(self): ...
    def is_other(self): ...

MoveIntoVaultError_validator: Incomplete

class PaperContentError(bb.Union):
    insufficient_permissions: Incomplete
    content_malformed: Incomplete
    doc_length_exceeded: Incomplete
    image_size_exceeded: Incomplete
    other: Incomplete
    def is_insufficient_permissions(self): ...
    def is_content_malformed(self): ...
    def is_doc_length_exceeded(self): ...
    def is_image_size_exceeded(self): ...
    def is_other(self): ...

PaperContentError_validator: Incomplete

class PaperCreateArg(bb.Struct):
    path: Incomplete
    import_format: Incomplete
    def __init__(self, path: Incomplete | None = None, import_format: Incomplete | None = None) -> None: ...

PaperCreateArg_validator: Incomplete

class PaperCreateError(PaperContentError):
    invalid_path: Incomplete
    email_unverified: Incomplete
    invalid_file_extension: Incomplete
    paper_disabled: Incomplete
    def is_invalid_path(self): ...
    def is_email_unverified(self): ...
    def is_invalid_file_extension(self): ...
    def is_paper_disabled(self): ...

PaperCreateError_validator: Incomplete

class PaperCreateResult(bb.Struct):
    url: Incomplete
    result_path: Incomplete
    file_id: Incomplete
    paper_revision: Incomplete
    def __init__(
        self,
        url: Incomplete | None = None,
        result_path: Incomplete | None = None,
        file_id: Incomplete | None = None,
        paper_revision: Incomplete | None = None,
    ) -> None: ...

PaperCreateResult_validator: Incomplete

class PaperDocUpdatePolicy(bb.Union):
    update: Incomplete
    overwrite: Incomplete
    prepend: Incomplete
    append: Incomplete
    other: Incomplete
    def is_update(self): ...
    def is_overwrite(self): ...
    def is_prepend(self): ...
    def is_append(self): ...
    def is_other(self): ...

PaperDocUpdatePolicy_validator: Incomplete

class PaperUpdateArg(bb.Struct):
    path: Incomplete
    import_format: Incomplete
    doc_update_policy: Incomplete
    paper_revision: Incomplete
    def __init__(
        self,
        path: Incomplete | None = None,
        import_format: Incomplete | None = None,
        doc_update_policy: Incomplete | None = None,
        paper_revision: Incomplete | None = None,
    ) -> None: ...

PaperUpdateArg_validator: Incomplete

class PaperUpdateError(PaperContentError):
    revision_mismatch: Incomplete
    doc_archived: Incomplete
    doc_deleted: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_revision_mismatch(self): ...
    def is_doc_archived(self): ...
    def is_doc_deleted(self): ...
    def get_path(self): ...

PaperUpdateError_validator: Incomplete

class PaperUpdateResult(bb.Struct):
    paper_revision: Incomplete
    def __init__(self, paper_revision: Incomplete | None = None) -> None: ...

PaperUpdateResult_validator: Incomplete

class PathOrLink(bb.Union):
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    @classmethod
    def link(cls, val): ...
    def is_path(self): ...
    def is_link(self): ...
    def is_other(self): ...
    def get_path(self): ...
    def get_link(self): ...

PathOrLink_validator: Incomplete

class PathToTags(bb.Struct):
    path: Incomplete
    tags: Incomplete
    def __init__(self, path: Incomplete | None = None, tags: Incomplete | None = None) -> None: ...

PathToTags_validator: Incomplete

class PhotoMetadata(MediaMetadata):
    def __init__(
        self, dimensions: Incomplete | None = None, location: Incomplete | None = None, time_taken: Incomplete | None = None
    ) -> None: ...

PhotoMetadata_validator: Incomplete

class PreviewArg(bb.Struct):
    path: Incomplete
    rev: Incomplete
    def __init__(self, path: Incomplete | None = None, rev: Incomplete | None = None) -> None: ...

PreviewArg_validator: Incomplete

class PreviewError(bb.Union):
    in_progress: Incomplete
    unsupported_extension: Incomplete
    unsupported_content: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_in_progress(self): ...
    def is_unsupported_extension(self): ...
    def is_unsupported_content(self): ...
    def get_path(self): ...

PreviewError_validator: Incomplete

class PreviewResult(bb.Struct):
    file_metadata: Incomplete
    link_metadata: Incomplete
    def __init__(self, file_metadata: Incomplete | None = None, link_metadata: Incomplete | None = None) -> None: ...

PreviewResult_validator: Incomplete

class RelocationPath(bb.Struct):
    from_path: Incomplete
    to_path: Incomplete
    def __init__(self, from_path: Incomplete | None = None, to_path: Incomplete | None = None) -> None: ...

RelocationPath_validator: Incomplete

class RelocationArg(RelocationPath):
    allow_shared_folder: Incomplete
    autorename: Incomplete
    allow_ownership_transfer: Incomplete
    def __init__(
        self,
        from_path: Incomplete | None = None,
        to_path: Incomplete | None = None,
        allow_shared_folder: Incomplete | None = None,
        autorename: Incomplete | None = None,
        allow_ownership_transfer: Incomplete | None = None,
    ) -> None: ...

RelocationArg_validator: Incomplete

class RelocationBatchArg(RelocationBatchArgBase):
    allow_shared_folder: Incomplete
    allow_ownership_transfer: Incomplete
    def __init__(
        self,
        entries: Incomplete | None = None,
        autorename: Incomplete | None = None,
        allow_shared_folder: Incomplete | None = None,
        allow_ownership_transfer: Incomplete | None = None,
    ) -> None: ...

RelocationBatchArg_validator: Incomplete

class RelocationError(bb.Union):
    cant_copy_shared_folder: Incomplete
    cant_nest_shared_folder: Incomplete
    cant_move_folder_into_itself: Incomplete
    too_many_files: Incomplete
    duplicated_or_nested_paths: Incomplete
    cant_transfer_ownership: Incomplete
    insufficient_quota: Incomplete
    internal_error: Incomplete
    cant_move_shared_folder: Incomplete
    other: Incomplete
    @classmethod
    def from_lookup(cls, val): ...
    @classmethod
    def from_write(cls, val): ...
    @classmethod
    def to(cls, val): ...
    @classmethod
    def cant_move_into_vault(cls, val): ...
    @classmethod
    def cant_move_into_family(cls, val): ...
    def is_from_lookup(self): ...
    def is_from_write(self): ...
    def is_to(self): ...
    def is_cant_copy_shared_folder(self): ...
    def is_cant_nest_shared_folder(self): ...
    def is_cant_move_folder_into_itself(self): ...
    def is_too_many_files(self): ...
    def is_duplicated_or_nested_paths(self): ...
    def is_cant_transfer_ownership(self): ...
    def is_insufficient_quota(self): ...
    def is_internal_error(self): ...
    def is_cant_move_shared_folder(self): ...
    def is_cant_move_into_vault(self): ...
    def is_cant_move_into_family(self): ...
    def is_other(self): ...
    def get_from_lookup(self): ...
    def get_from_write(self): ...
    def get_to(self): ...
    def get_cant_move_into_vault(self): ...
    def get_cant_move_into_family(self): ...

RelocationError_validator: Incomplete

class RelocationBatchError(RelocationError):
    too_many_write_operations: Incomplete
    def is_too_many_write_operations(self): ...

RelocationBatchError_validator: Incomplete

class RelocationBatchErrorEntry(bb.Union):
    internal_error: Incomplete
    too_many_write_operations: Incomplete
    other: Incomplete
    @classmethod
    def relocation_error(cls, val): ...
    def is_relocation_error(self): ...
    def is_internal_error(self): ...
    def is_too_many_write_operations(self): ...
    def is_other(self): ...
    def get_relocation_error(self): ...

RelocationBatchErrorEntry_validator: Incomplete

class RelocationBatchJobStatus(async_.PollResultBase):
    @classmethod
    def complete(cls, val): ...
    @classmethod
    def failed(cls, val): ...
    def is_complete(self): ...
    def is_failed(self): ...
    def get_complete(self): ...
    def get_failed(self): ...

RelocationBatchJobStatus_validator: Incomplete

class RelocationBatchLaunch(async_.LaunchResultBase):
    other: Incomplete
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def is_other(self): ...
    def get_complete(self): ...

RelocationBatchLaunch_validator: Incomplete

class RelocationBatchResult(FileOpsResult):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

RelocationBatchResult_validator: Incomplete

class RelocationBatchResultData(bb.Struct):
    metadata: Incomplete
    def __init__(self, metadata: Incomplete | None = None) -> None: ...

RelocationBatchResultData_validator: Incomplete

class RelocationBatchResultEntry(bb.Union):
    other: Incomplete
    @classmethod
    def success(cls, val): ...
    @classmethod
    def failure(cls, val): ...
    def is_success(self): ...
    def is_failure(self): ...
    def is_other(self): ...
    def get_success(self): ...
    def get_failure(self): ...

RelocationBatchResultEntry_validator: Incomplete

class RelocationBatchV2JobStatus(async_.PollResultBase):
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def get_complete(self): ...

RelocationBatchV2JobStatus_validator: Incomplete

class RelocationBatchV2Launch(async_.LaunchResultBase):
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def get_complete(self): ...

RelocationBatchV2Launch_validator: Incomplete

class RelocationBatchV2Result(FileOpsResult):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

RelocationBatchV2Result_validator: Incomplete

class RelocationResult(FileOpsResult):
    metadata: Incomplete
    def __init__(self, metadata: Incomplete | None = None) -> None: ...

RelocationResult_validator: Incomplete

class RemoveTagArg(bb.Struct):
    path: Incomplete
    tag_text: Incomplete
    def __init__(self, path: Incomplete | None = None, tag_text: Incomplete | None = None) -> None: ...

RemoveTagArg_validator: Incomplete

class RemoveTagError(BaseTagError):
    tag_not_present: Incomplete
    def is_tag_not_present(self): ...

RemoveTagError_validator: Incomplete

class RestoreArg(bb.Struct):
    path: Incomplete
    rev: Incomplete
    def __init__(self, path: Incomplete | None = None, rev: Incomplete | None = None) -> None: ...

RestoreArg_validator: Incomplete

class RestoreError(bb.Union):
    invalid_revision: Incomplete
    in_progress: Incomplete
    other: Incomplete
    @classmethod
    def path_lookup(cls, val): ...
    @classmethod
    def path_write(cls, val): ...
    def is_path_lookup(self): ...
    def is_path_write(self): ...
    def is_invalid_revision(self): ...
    def is_in_progress(self): ...
    def is_other(self): ...
    def get_path_lookup(self): ...
    def get_path_write(self): ...

RestoreError_validator: Incomplete

class SaveCopyReferenceArg(bb.Struct):
    copy_reference: Incomplete
    path: Incomplete
    def __init__(self, copy_reference: Incomplete | None = None, path: Incomplete | None = None) -> None: ...

SaveCopyReferenceArg_validator: Incomplete

class SaveCopyReferenceError(bb.Union):
    invalid_copy_reference: Incomplete
    no_permission: Incomplete
    not_found: Incomplete
    too_many_files: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_invalid_copy_reference(self): ...
    def is_no_permission(self): ...
    def is_not_found(self): ...
    def is_too_many_files(self): ...
    def is_other(self): ...
    def get_path(self): ...

SaveCopyReferenceError_validator: Incomplete

class SaveCopyReferenceResult(bb.Struct):
    metadata: Incomplete
    def __init__(self, metadata: Incomplete | None = None) -> None: ...

SaveCopyReferenceResult_validator: Incomplete

class SaveUrlArg(bb.Struct):
    path: Incomplete
    url: Incomplete
    def __init__(self, path: Incomplete | None = None, url: Incomplete | None = None) -> None: ...

SaveUrlArg_validator: Incomplete

class SaveUrlError(bb.Union):
    download_failed: Incomplete
    invalid_url: Incomplete
    not_found: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_download_failed(self): ...
    def is_invalid_url(self): ...
    def is_not_found(self): ...
    def is_other(self): ...
    def get_path(self): ...

SaveUrlError_validator: Incomplete

class SaveUrlJobStatus(async_.PollResultBase):
    @classmethod
    def complete(cls, val): ...
    @classmethod
    def failed(cls, val): ...
    def is_complete(self): ...
    def is_failed(self): ...
    def get_complete(self): ...
    def get_failed(self): ...

SaveUrlJobStatus_validator: Incomplete

class SaveUrlResult(async_.LaunchResultBase):
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def get_complete(self): ...

SaveUrlResult_validator: Incomplete

class SearchArg(bb.Struct):
    path: Incomplete
    query: Incomplete
    start: Incomplete
    max_results: Incomplete
    mode: Incomplete
    def __init__(
        self,
        path: Incomplete | None = None,
        query: Incomplete | None = None,
        start: Incomplete | None = None,
        max_results: Incomplete | None = None,
        mode: Incomplete | None = None,
    ) -> None: ...

SearchArg_validator: Incomplete

class SearchError(bb.Union):
    internal_error: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    @classmethod
    def invalid_argument(cls, val): ...
    def is_path(self): ...
    def is_invalid_argument(self): ...
    def is_internal_error(self): ...
    def is_other(self): ...
    def get_path(self): ...
    def get_invalid_argument(self): ...

SearchError_validator: Incomplete

class SearchMatch(bb.Struct):
    match_type: Incomplete
    metadata: Incomplete
    def __init__(self, match_type: Incomplete | None = None, metadata: Incomplete | None = None) -> None: ...

SearchMatch_validator: Incomplete

class SearchMatchFieldOptions(bb.Struct):
    include_highlights: Incomplete
    def __init__(self, include_highlights: Incomplete | None = None) -> None: ...

SearchMatchFieldOptions_validator: Incomplete

class SearchMatchType(bb.Union):
    filename: Incomplete
    content: Incomplete
    both: Incomplete
    def is_filename(self): ...
    def is_content(self): ...
    def is_both(self): ...

SearchMatchType_validator: Incomplete

class SearchMatchTypeV2(bb.Union):
    filename: Incomplete
    file_content: Incomplete
    filename_and_content: Incomplete
    image_content: Incomplete
    other: Incomplete
    def is_filename(self): ...
    def is_file_content(self): ...
    def is_filename_and_content(self): ...
    def is_image_content(self): ...
    def is_other(self): ...

SearchMatchTypeV2_validator: Incomplete

class SearchMatchV2(bb.Struct):
    metadata: Incomplete
    match_type: Incomplete
    highlight_spans: Incomplete
    def __init__(
        self, metadata: Incomplete | None = None, match_type: Incomplete | None = None, highlight_spans: Incomplete | None = None
    ) -> None: ...

SearchMatchV2_validator: Incomplete

class SearchMode(bb.Union):
    filename: Incomplete
    filename_and_content: Incomplete
    deleted_filename: Incomplete
    def is_filename(self): ...
    def is_filename_and_content(self): ...
    def is_deleted_filename(self): ...

SearchMode_validator: Incomplete

class SearchOptions(bb.Struct):
    path: Incomplete
    max_results: Incomplete
    order_by: Incomplete
    file_status: Incomplete
    filename_only: Incomplete
    file_extensions: Incomplete
    file_categories: Incomplete
    account_id: Incomplete
    def __init__(
        self,
        path: Incomplete | None = None,
        max_results: Incomplete | None = None,
        order_by: Incomplete | None = None,
        file_status: Incomplete | None = None,
        filename_only: Incomplete | None = None,
        file_extensions: Incomplete | None = None,
        file_categories: Incomplete | None = None,
        account_id: Incomplete | None = None,
    ) -> None: ...

SearchOptions_validator: Incomplete

class SearchOrderBy(bb.Union):
    relevance: Incomplete
    last_modified_time: Incomplete
    other: Incomplete
    def is_relevance(self): ...
    def is_last_modified_time(self): ...
    def is_other(self): ...

SearchOrderBy_validator: Incomplete

class SearchResult(bb.Struct):
    matches: Incomplete
    more: Incomplete
    start: Incomplete
    def __init__(
        self, matches: Incomplete | None = None, more: Incomplete | None = None, start: Incomplete | None = None
    ) -> None: ...

SearchResult_validator: Incomplete

class SearchV2Arg(bb.Struct):
    query: Incomplete
    options: Incomplete
    match_field_options: Incomplete
    include_highlights: Incomplete
    def __init__(
        self,
        query: Incomplete | None = None,
        options: Incomplete | None = None,
        match_field_options: Incomplete | None = None,
        include_highlights: Incomplete | None = None,
    ) -> None: ...

SearchV2Arg_validator: Incomplete

class SearchV2ContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

SearchV2ContinueArg_validator: Incomplete

class SearchV2Result(bb.Struct):
    matches: Incomplete
    has_more: Incomplete
    cursor: Incomplete
    def __init__(
        self, matches: Incomplete | None = None, has_more: Incomplete | None = None, cursor: Incomplete | None = None
    ) -> None: ...

SearchV2Result_validator: Incomplete

class SharedLink(bb.Struct):
    url: Incomplete
    password: Incomplete
    def __init__(self, url: Incomplete | None = None, password: Incomplete | None = None) -> None: ...

SharedLink_validator: Incomplete

class SharedLinkFileInfo(bb.Struct):
    url: Incomplete
    path: Incomplete
    password: Incomplete
    def __init__(
        self, url: Incomplete | None = None, path: Incomplete | None = None, password: Incomplete | None = None
    ) -> None: ...

SharedLinkFileInfo_validator: Incomplete

class SingleUserLock(bb.Struct):
    created: Incomplete
    lock_holder_account_id: Incomplete
    lock_holder_team_id: Incomplete
    def __init__(
        self,
        created: Incomplete | None = None,
        lock_holder_account_id: Incomplete | None = None,
        lock_holder_team_id: Incomplete | None = None,
    ) -> None: ...

SingleUserLock_validator: Incomplete

class SymlinkInfo(bb.Struct):
    target: Incomplete
    def __init__(self, target: Incomplete | None = None) -> None: ...

SymlinkInfo_validator: Incomplete

class SyncSetting(bb.Union):
    default: Incomplete
    not_synced: Incomplete
    not_synced_inactive: Incomplete
    other: Incomplete
    def is_default(self): ...
    def is_not_synced(self): ...
    def is_not_synced_inactive(self): ...
    def is_other(self): ...

SyncSetting_validator: Incomplete

class SyncSettingArg(bb.Union):
    default: Incomplete
    not_synced: Incomplete
    other: Incomplete
    def is_default(self): ...
    def is_not_synced(self): ...
    def is_other(self): ...

SyncSettingArg_validator: Incomplete

class SyncSettingsError(bb.Union):
    unsupported_combination: Incomplete
    unsupported_configuration: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_unsupported_combination(self): ...
    def is_unsupported_configuration(self): ...
    def is_other(self): ...
    def get_path(self): ...

SyncSettingsError_validator: Incomplete

class Tag(bb.Union):
    other: Incomplete
    @classmethod
    def user_generated_tag(cls, val): ...
    def is_user_generated_tag(self): ...
    def is_other(self): ...
    def get_user_generated_tag(self): ...

Tag_validator: Incomplete

class ThumbnailArg(bb.Struct):
    path: Incomplete
    format: Incomplete
    size: Incomplete
    mode: Incomplete
    def __init__(
        self,
        path: Incomplete | None = None,
        format: Incomplete | None = None,
        size: Incomplete | None = None,
        mode: Incomplete | None = None,
    ) -> None: ...

ThumbnailArg_validator: Incomplete

class ThumbnailError(bb.Union):
    unsupported_extension: Incomplete
    unsupported_image: Incomplete
    conversion_error: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_unsupported_extension(self): ...
    def is_unsupported_image(self): ...
    def is_conversion_error(self): ...
    def get_path(self): ...

ThumbnailError_validator: Incomplete

class ThumbnailFormat(bb.Union):
    jpeg: Incomplete
    png: Incomplete
    def is_jpeg(self): ...
    def is_png(self): ...

ThumbnailFormat_validator: Incomplete

class ThumbnailMode(bb.Union):
    strict: Incomplete
    bestfit: Incomplete
    fitone_bestfit: Incomplete
    def is_strict(self): ...
    def is_bestfit(self): ...
    def is_fitone_bestfit(self): ...

ThumbnailMode_validator: Incomplete

class ThumbnailSize(bb.Union):
    w32h32: Incomplete
    w64h64: Incomplete
    w128h128: Incomplete
    w256h256: Incomplete
    w480h320: Incomplete
    w640h480: Incomplete
    w960h640: Incomplete
    w1024h768: Incomplete
    w2048h1536: Incomplete
    def is_w32h32(self): ...
    def is_w64h64(self): ...
    def is_w128h128(self): ...
    def is_w256h256(self): ...
    def is_w480h320(self): ...
    def is_w640h480(self): ...
    def is_w960h640(self): ...
    def is_w1024h768(self): ...
    def is_w2048h1536(self): ...

ThumbnailSize_validator: Incomplete

class ThumbnailV2Arg(bb.Struct):
    resource: Incomplete
    format: Incomplete
    size: Incomplete
    mode: Incomplete
    def __init__(
        self,
        resource: Incomplete | None = None,
        format: Incomplete | None = None,
        size: Incomplete | None = None,
        mode: Incomplete | None = None,
    ) -> None: ...

ThumbnailV2Arg_validator: Incomplete

class ThumbnailV2Error(bb.Union):
    unsupported_extension: Incomplete
    unsupported_image: Incomplete
    conversion_error: Incomplete
    access_denied: Incomplete
    not_found: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_unsupported_extension(self): ...
    def is_unsupported_image(self): ...
    def is_conversion_error(self): ...
    def is_access_denied(self): ...
    def is_not_found(self): ...
    def is_other(self): ...
    def get_path(self): ...

ThumbnailV2Error_validator: Incomplete

class UnlockFileArg(bb.Struct):
    path: Incomplete
    def __init__(self, path: Incomplete | None = None) -> None: ...

UnlockFileArg_validator: Incomplete

class UnlockFileBatchArg(bb.Struct):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

UnlockFileBatchArg_validator: Incomplete

class UploadArg(CommitInfo):
    content_hash: Incomplete
    def __init__(
        self,
        path: Incomplete | None = None,
        mode: Incomplete | None = None,
        autorename: Incomplete | None = None,
        client_modified: Incomplete | None = None,
        mute: Incomplete | None = None,
        property_groups: Incomplete | None = None,
        strict_conflict: Incomplete | None = None,
        content_hash: Incomplete | None = None,
    ) -> None: ...

UploadArg_validator: Incomplete

class UploadError(bb.Union):
    payload_too_large: Incomplete
    content_hash_mismatch: Incomplete
    other: Incomplete
    @classmethod
    def path(cls, val): ...
    @classmethod
    def properties_error(cls, val): ...
    def is_path(self): ...
    def is_properties_error(self): ...
    def is_payload_too_large(self): ...
    def is_content_hash_mismatch(self): ...
    def is_other(self): ...
    def get_path(self): ...
    def get_properties_error(self): ...

UploadError_validator: Incomplete

class UploadSessionAppendArg(bb.Struct):
    cursor: Incomplete
    close: Incomplete
    content_hash: Incomplete
    def __init__(
        self, cursor: Incomplete | None = None, close: Incomplete | None = None, content_hash: Incomplete | None = None
    ) -> None: ...

UploadSessionAppendArg_validator: Incomplete

class UploadSessionLookupError(bb.Union):
    not_found: Incomplete
    closed: Incomplete
    not_closed: Incomplete
    too_large: Incomplete
    concurrent_session_invalid_offset: Incomplete
    concurrent_session_invalid_data_size: Incomplete
    payload_too_large: Incomplete
    other: Incomplete
    @classmethod
    def incorrect_offset(cls, val): ...
    def is_not_found(self): ...
    def is_incorrect_offset(self): ...
    def is_closed(self): ...
    def is_not_closed(self): ...
    def is_too_large(self): ...
    def is_concurrent_session_invalid_offset(self): ...
    def is_concurrent_session_invalid_data_size(self): ...
    def is_payload_too_large(self): ...
    def is_other(self): ...
    def get_incorrect_offset(self): ...

UploadSessionLookupError_validator: Incomplete

class UploadSessionAppendError(UploadSessionLookupError):
    content_hash_mismatch: Incomplete
    def is_content_hash_mismatch(self): ...

UploadSessionAppendError_validator: Incomplete

class UploadSessionCursor(bb.Struct):
    session_id: Incomplete
    offset: Incomplete
    def __init__(self, session_id: Incomplete | None = None, offset: Incomplete | None = None) -> None: ...

UploadSessionCursor_validator: Incomplete

class UploadSessionFinishArg(bb.Struct):
    cursor: Incomplete
    commit: Incomplete
    content_hash: Incomplete
    def __init__(
        self, cursor: Incomplete | None = None, commit: Incomplete | None = None, content_hash: Incomplete | None = None
    ) -> None: ...

UploadSessionFinishArg_validator: Incomplete

class UploadSessionFinishBatchArg(bb.Struct):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

UploadSessionFinishBatchArg_validator: Incomplete

class UploadSessionFinishBatchJobStatus(async_.PollResultBase):
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def get_complete(self): ...

UploadSessionFinishBatchJobStatus_validator: Incomplete

class UploadSessionFinishBatchLaunch(async_.LaunchResultBase):
    other: Incomplete
    @classmethod
    def complete(cls, val): ...
    def is_complete(self): ...
    def is_other(self): ...
    def get_complete(self): ...

UploadSessionFinishBatchLaunch_validator: Incomplete

class UploadSessionFinishBatchResult(bb.Struct):
    entries: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None: ...

UploadSessionFinishBatchResult_validator: Incomplete

class UploadSessionFinishBatchResultEntry(bb.Union):
    @classmethod
    def success(cls, val): ...
    @classmethod
    def failure(cls, val): ...
    def is_success(self): ...
    def is_failure(self): ...
    def get_success(self): ...
    def get_failure(self): ...

UploadSessionFinishBatchResultEntry_validator: Incomplete

class UploadSessionFinishError(bb.Union):
    too_many_shared_folder_targets: Incomplete
    too_many_write_operations: Incomplete
    concurrent_session_data_not_allowed: Incomplete
    concurrent_session_not_closed: Incomplete
    concurrent_session_missing_data: Incomplete
    payload_too_large: Incomplete
    content_hash_mismatch: Incomplete
    other: Incomplete
    @classmethod
    def lookup_failed(cls, val): ...
    @classmethod
    def path(cls, val): ...
    @classmethod
    def properties_error(cls, val): ...
    def is_lookup_failed(self): ...
    def is_path(self): ...
    def is_properties_error(self): ...
    def is_too_many_shared_folder_targets(self): ...
    def is_too_many_write_operations(self): ...
    def is_concurrent_session_data_not_allowed(self): ...
    def is_concurrent_session_not_closed(self): ...
    def is_concurrent_session_missing_data(self): ...
    def is_payload_too_large(self): ...
    def is_content_hash_mismatch(self): ...
    def is_other(self): ...
    def get_lookup_failed(self): ...
    def get_path(self): ...
    def get_properties_error(self): ...

UploadSessionFinishError_validator: Incomplete

class UploadSessionOffsetError(bb.Struct):
    correct_offset: Incomplete
    def __init__(self, correct_offset: Incomplete | None = None) -> None: ...

UploadSessionOffsetError_validator: Incomplete

class UploadSessionStartArg(bb.Struct):
    close: Incomplete
    session_type: Incomplete
    content_hash: Incomplete
    def __init__(
        self, close: Incomplete | None = None, session_type: Incomplete | None = None, content_hash: Incomplete | None = None
    ) -> None: ...

UploadSessionStartArg_validator: Incomplete

class UploadSessionStartBatchArg(bb.Struct):
    session_type: Incomplete
    num_sessions: Incomplete
    def __init__(self, num_sessions: Incomplete | None = None, session_type: Incomplete | None = None) -> None: ...

UploadSessionStartBatchArg_validator: Incomplete

class UploadSessionStartBatchResult(bb.Struct):
    session_ids: Incomplete
    def __init__(self, session_ids: Incomplete | None = None) -> None: ...

UploadSessionStartBatchResult_validator: Incomplete

class UploadSessionStartError(bb.Union):
    concurrent_session_data_not_allowed: Incomplete
    concurrent_session_close_not_allowed: Incomplete
    payload_too_large: Incomplete
    content_hash_mismatch: Incomplete
    other: Incomplete
    def is_concurrent_session_data_not_allowed(self): ...
    def is_concurrent_session_close_not_allowed(self): ...
    def is_payload_too_large(self): ...
    def is_content_hash_mismatch(self): ...
    def is_other(self): ...

UploadSessionStartError_validator: Incomplete

class UploadSessionStartResult(bb.Struct):
    session_id: Incomplete
    def __init__(self, session_id: Incomplete | None = None) -> None: ...

UploadSessionStartResult_validator: Incomplete

class UploadSessionType(bb.Union):
    sequential: Incomplete
    concurrent: Incomplete
    other: Incomplete
    def is_sequential(self): ...
    def is_concurrent(self): ...
    def is_other(self): ...

UploadSessionType_validator: Incomplete

class UploadWriteFailed(bb.Struct):
    reason: Incomplete
    upload_session_id: Incomplete
    def __init__(self, reason: Incomplete | None = None, upload_session_id: Incomplete | None = None) -> None: ...

UploadWriteFailed_validator: Incomplete

class UserGeneratedTag(bb.Struct):
    tag_text: Incomplete
    def __init__(self, tag_text: Incomplete | None = None) -> None: ...

UserGeneratedTag_validator: Incomplete

class VideoMetadata(MediaMetadata):
    duration: Incomplete
    def __init__(
        self,
        dimensions: Incomplete | None = None,
        location: Incomplete | None = None,
        time_taken: Incomplete | None = None,
        duration: Incomplete | None = None,
    ) -> None: ...

VideoMetadata_validator: Incomplete

class WriteConflictError(bb.Union):
    file: Incomplete
    folder: Incomplete
    file_ancestor: Incomplete
    other: Incomplete
    def is_file(self): ...
    def is_folder(self): ...
    def is_file_ancestor(self): ...
    def is_other(self): ...

WriteConflictError_validator: Incomplete

class WriteError(bb.Union):
    no_write_permission: Incomplete
    insufficient_space: Incomplete
    disallowed_name: Incomplete
    team_folder: Incomplete
    operation_suppressed: Incomplete
    too_many_write_operations: Incomplete
    other: Incomplete
    @classmethod
    def malformed_path(cls, val): ...
    @classmethod
    def conflict(cls, val): ...
    def is_malformed_path(self): ...
    def is_conflict(self): ...
    def is_no_write_permission(self): ...
    def is_insufficient_space(self): ...
    def is_disallowed_name(self): ...
    def is_team_folder(self): ...
    def is_operation_suppressed(self): ...
    def is_too_many_write_operations(self): ...
    def is_other(self): ...
    def get_malformed_path(self): ...
    def get_conflict(self): ...

WriteError_validator: Incomplete

class WriteMode(bb.Union):
    add: Incomplete
    overwrite: Incomplete
    @classmethod
    def update(cls, val): ...
    def is_add(self): ...
    def is_overwrite(self): ...
    def is_update(self): ...
    def get_update(self): ...

WriteMode_validator: Incomplete
CopyBatchArg_validator = RelocationBatchArgBase_validator
CopyBatchArg = RelocationBatchArgBase
FileId_validator: Incomplete
Id_validator: Incomplete
ListFolderCursor_validator: Incomplete
MalformedPathError_validator: Incomplete
Path_validator: Incomplete
PathOrId_validator: Incomplete
PathR_validator: Incomplete
PathROrId_validator: Incomplete
ReadPath_validator: Incomplete
Rev_validator: Incomplete
SearchV2Cursor_validator: Incomplete
Sha256HexHash_validator: Incomplete
SharedLinkUrl_validator: Incomplete
TagText_validator: Incomplete
WritePath_validator: Incomplete
WritePathOrId_validator: Incomplete
alpha_get_metadata: Incomplete
alpha_upload: Incomplete
copy_v2: Incomplete
copy: Incomplete
copy_batch_v2: Incomplete
copy_batch: Incomplete
copy_batch_check_v2: Incomplete
copy_batch_check: Incomplete
copy_reference_get: Incomplete
copy_reference_save: Incomplete
create_folder_v2: Incomplete
create_folder: Incomplete
create_folder_batch: Incomplete
create_folder_batch_check: Incomplete
delete_v2: Incomplete
delete: Incomplete
delete_batch: Incomplete
delete_batch_check: Incomplete
download: Incomplete
download_zip: Incomplete
export: Incomplete
get_file_lock_batch: Incomplete
get_metadata: Incomplete
get_preview: Incomplete
get_temporary_link: Incomplete
get_temporary_upload_link: Incomplete
get_thumbnail: Incomplete
get_thumbnail_v2: Incomplete
get_thumbnail_batch: Incomplete
list_folder: Incomplete
list_folder_continue: Incomplete
list_folder_get_latest_cursor: Incomplete
list_folder_longpoll: Incomplete
list_revisions: Incomplete
lock_file_batch: Incomplete
move_v2: Incomplete
move: Incomplete
move_batch_v2: Incomplete
move_batch: Incomplete
move_batch_check_v2: Incomplete
move_batch_check: Incomplete
paper_create: Incomplete
paper_update: Incomplete
permanently_delete: Incomplete
properties_add: Incomplete
properties_overwrite: Incomplete
properties_remove: Incomplete
properties_template_get: Incomplete
properties_template_list: Incomplete
properties_update: Incomplete
restore: Incomplete
save_url: Incomplete
save_url_check_job_status: Incomplete
search: Incomplete
search_v2: Incomplete
search_continue_v2: Incomplete
tags_add: Incomplete
tags_get: Incomplete
tags_remove: Incomplete
unlock_file_batch: Incomplete
upload: Incomplete
upload_session_append_v2: Incomplete
upload_session_append: Incomplete
upload_session_finish: Incomplete
upload_session_finish_batch: Incomplete
upload_session_finish_batch_v2: Incomplete
upload_session_finish_batch_check: Incomplete
upload_session_start: Incomplete
upload_session_start_batch: Incomplete
ROUTES: Incomplete
