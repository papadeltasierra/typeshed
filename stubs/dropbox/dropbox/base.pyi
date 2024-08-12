import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

from dropbox import (
    common as common,
    secondary_emails as secondary_emails,
    seen_state as seen_state,
    team as team,
    team_common as team_common,
    team_log as team_log,
    team_policies as team_policies,
    users_common as users_common,
)

class DropboxBase(metaclass=abc.ABCMeta):
    __metaclass__: type[ABCMeta]
    @abstractmethod
    # Ref: https://github.com/dropbox/dropbox-sdk-python/issues/511
    def request(self, route, namespace, arg, arg_binary=None): ...
    def account_set_profile_photo(self, photo): ...
    def auth_token_from_oauth1(self, oauth1_token, oauth1_token_secret): ...
    def auth_token_revoke(self) -> None: ...
    def check_app(self, query: str = ""): ...
    def check_user(self, query: str = ""): ...
    def contacts_delete_manual_contacts(self) -> None: ...
    def contacts_delete_manual_contacts_batch(self, email_addresses) -> None: ...
    def file_properties_properties_add(self, path, property_groups) -> None: ...
    def file_properties_properties_overwrite(self, path, property_groups) -> None: ...
    def file_properties_properties_remove(self, path, property_template_ids) -> None: ...
    def file_properties_properties_search(self, queries, template_filter=...): ...
    def file_properties_properties_search_continue(self, cursor): ...
    def file_properties_properties_update(self, path, update_property_groups) -> None: ...
    def file_properties_templates_add_for_user(self, name, description, fields): ...
    def file_properties_templates_get_for_user(self, template_id): ...
    def file_properties_templates_list_for_user(self): ...
    def file_properties_templates_remove_for_user(self, template_id) -> None: ...
    def file_properties_templates_update_for_user(
        self,
        template_id,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        add_fields: Incomplete | None = None,
    ): ...
    def file_requests_count(self): ...
    def file_requests_create(
        self, title, destination, deadline: Incomplete | None = None, open: bool = True, description: Incomplete | None = None
    ): ...
    def file_requests_delete(self, ids): ...
    def file_requests_delete_all_closed(self): ...
    def file_requests_get(self, id): ...
    def file_requests_list_v2(self, limit: int = 1000): ...
    def file_requests_list(self): ...
    def file_requests_list_continue(self, cursor): ...
    def file_requests_update(
        self,
        id,
        title: Incomplete | None = None,
        destination: Incomplete | None = None,
        deadline=...,
        open: Incomplete | None = None,
        description: Incomplete | None = None,
    ): ...
    def files_alpha_get_metadata(
        self,
        path,
        include_media_info: bool = False,
        include_deleted: bool = False,
        include_has_explicit_shared_members: bool = False,
        include_property_groups: Incomplete | None = None,
        include_property_templates: Incomplete | None = None,
    ): ...
    def files_alpha_upload(
        self,
        f,
        path,
        mode=...,
        autorename: bool = False,
        client_modified: Incomplete | None = None,
        mute: bool = False,
        property_groups: Incomplete | None = None,
        strict_conflict: bool = False,
        content_hash: Incomplete | None = None,
    ): ...
    def files_copy_v2(
        self,
        from_path,
        to_path,
        allow_shared_folder: bool = False,
        autorename: bool = False,
        allow_ownership_transfer: bool = False,
    ): ...
    def files_copy(
        self,
        from_path,
        to_path,
        allow_shared_folder: bool = False,
        autorename: bool = False,
        allow_ownership_transfer: bool = False,
    ): ...
    def files_copy_batch_v2(self, entries, autorename: bool = False): ...
    def files_copy_batch(
        self, entries, autorename: bool = False, allow_shared_folder: bool = False, allow_ownership_transfer: bool = False
    ): ...
    def files_copy_batch_check_v2(self, async_job_id): ...
    def files_copy_batch_check(self, async_job_id): ...
    def files_copy_reference_get(self, path): ...
    def files_copy_reference_save(self, copy_reference, path): ...
    def files_create_folder_v2(self, path, autorename: bool = False): ...
    def files_create_folder(self, path, autorename: bool = False): ...
    def files_create_folder_batch(self, paths, autorename: bool = False, force_async: bool = False): ...
    def files_create_folder_batch_check(self, async_job_id): ...
    def files_delete_v2(self, path, parent_rev: Incomplete | None = None): ...
    def files_delete(self, path, parent_rev: Incomplete | None = None): ...
    def files_delete_batch(self, entries): ...
    def files_delete_batch_check(self, async_job_id): ...
    def files_download(self, path, rev: Incomplete | None = None): ...
    def files_download_to_file(self, download_path, path, rev: Incomplete | None = None): ...
    def files_download_zip(self, path): ...
    def files_download_zip_to_file(self, download_path, path): ...
    def files_export(self, path, export_format: Incomplete | None = None): ...
    def files_export_to_file(self, download_path, path, export_format: Incomplete | None = None): ...
    def files_get_file_lock_batch(self, entries): ...
    def files_get_metadata(
        self,
        path,
        include_media_info: bool = False,
        include_deleted: bool = False,
        include_has_explicit_shared_members: bool = False,
        include_property_groups: Incomplete | None = None,
    ): ...
    def files_get_preview(self, path, rev: Incomplete | None = None): ...
    def files_get_preview_to_file(self, download_path, path, rev: Incomplete | None = None): ...
    def files_get_temporary_link(self, path): ...
    def files_get_temporary_upload_link(self, commit_info, duration: float = 14400.0): ...
    def files_get_thumbnail(self, path, format=..., size=..., mode=...): ...
    def files_get_thumbnail_to_file(self, download_path, path, format=..., size=..., mode=...): ...
    def files_get_thumbnail_v2(self, resource, format=..., size=..., mode=...): ...
    def files_get_thumbnail_to_file_v2(self, download_path, resource, format=..., size=..., mode=...): ...
    def files_get_thumbnail_batch(self, entries): ...
    def files_list_folder(
        self,
        path,
        recursive: bool = False,
        include_media_info: bool = False,
        include_deleted: bool = False,
        include_has_explicit_shared_members: bool = False,
        include_mounted_folders: bool = True,
        limit: Incomplete | None = None,
        shared_link: Incomplete | None = None,
        include_property_groups: Incomplete | None = None,
        include_non_downloadable_files: bool = True,
    ): ...
    def files_list_folder_continue(self, cursor): ...
    def files_list_folder_get_latest_cursor(
        self,
        path,
        recursive: bool = False,
        include_media_info: bool = False,
        include_deleted: bool = False,
        include_has_explicit_shared_members: bool = False,
        include_mounted_folders: bool = True,
        limit: Incomplete | None = None,
        shared_link: Incomplete | None = None,
        include_property_groups: Incomplete | None = None,
        include_non_downloadable_files: bool = True,
    ): ...
    def files_list_folder_longpoll(self, cursor, timeout: int = 30): ...
    def files_list_revisions(self, path, mode=..., limit: int = 10): ...
    def files_lock_file_batch(self, entries): ...
    def files_move_v2(
        self,
        from_path,
        to_path,
        allow_shared_folder: bool = False,
        autorename: bool = False,
        allow_ownership_transfer: bool = False,
    ): ...
    def files_move(
        self,
        from_path,
        to_path,
        allow_shared_folder: bool = False,
        autorename: bool = False,
        allow_ownership_transfer: bool = False,
    ): ...
    def files_move_batch_v2(self, entries, autorename: bool = False, allow_ownership_transfer: bool = False): ...
    def files_move_batch(
        self, entries, autorename: bool = False, allow_shared_folder: bool = False, allow_ownership_transfer: bool = False
    ): ...
    def files_move_batch_check_v2(self, async_job_id): ...
    def files_move_batch_check(self, async_job_id): ...
    def files_paper_create(self, f, path, import_format): ...
    def files_paper_update(self, f, path, import_format, doc_update_policy, paper_revision: Incomplete | None = None): ...
    def files_permanently_delete(self, path, parent_rev: Incomplete | None = None) -> None: ...
    def files_properties_add(self, path, property_groups) -> None: ...
    def files_properties_overwrite(self, path, property_groups) -> None: ...
    def files_properties_remove(self, path, property_template_ids) -> None: ...
    def files_properties_template_get(self, template_id): ...
    def files_properties_template_list(self): ...
    def files_properties_update(self, path, update_property_groups) -> None: ...
    def files_restore(self, path, rev): ...
    def files_save_url(self, path, url): ...
    def files_save_url_check_job_status(self, async_job_id): ...
    def files_search(self, path, query, start: int = 0, max_results: int = 100, mode=...): ...
    def files_search_v2(
        self,
        query,
        options: Incomplete | None = None,
        match_field_options: Incomplete | None = None,
        include_highlights: Incomplete | None = None,
    ): ...
    def files_search_continue_v2(self, cursor): ...
    def files_tags_add(self, path, tag_text) -> None: ...
    def files_tags_get(self, paths): ...
    def files_tags_remove(self, path, tag_text) -> None: ...
    def files_unlock_file_batch(self, entries): ...
    def files_upload(
        self,
        f,
        path,
        mode=...,
        autorename: bool = False,
        client_modified: Incomplete | None = None,
        mute: bool = False,
        property_groups: Incomplete | None = None,
        strict_conflict: bool = False,
        content_hash: Incomplete | None = None,
    ): ...
    def files_upload_session_append_v2(self, f, cursor, close: bool = False, content_hash: Incomplete | None = None) -> None: ...
    def files_upload_session_append(self, f, session_id, offset) -> None: ...
    def files_upload_session_finish(self, f, cursor, commit, content_hash: Incomplete | None = None): ...
    def files_upload_session_finish_batch(self, entries): ...
    def files_upload_session_finish_batch_v2(self, entries): ...
    def files_upload_session_finish_batch_check(self, async_job_id): ...
    def files_upload_session_start(
        self, f, close: bool = False, session_type: Incomplete | None = None, content_hash: Incomplete | None = None
    ): ...
    def files_upload_session_start_batch(self, num_sessions, session_type: Incomplete | None = None): ...
    def openid_userinfo(self): ...
    def paper_docs_archive(self, doc_id) -> None: ...
    def paper_docs_create(self, f, import_format, parent_folder_id: Incomplete | None = None): ...
    def paper_docs_download(self, doc_id, export_format): ...
    def paper_docs_download_to_file(self, download_path, doc_id, export_format): ...
    def paper_docs_folder_users_list(self, doc_id, limit: int = 1000): ...
    def paper_docs_folder_users_list_continue(self, doc_id, cursor): ...
    def paper_docs_get_folder_info(self, doc_id): ...
    def paper_docs_list(self, filter_by=..., sort_by=..., sort_order=..., limit: int = 1000): ...
    def paper_docs_list_continue(self, cursor): ...
    def paper_docs_permanently_delete(self, doc_id) -> None: ...
    def paper_docs_sharing_policy_get(self, doc_id): ...
    def paper_docs_sharing_policy_set(self, doc_id, sharing_policy) -> None: ...
    def paper_docs_update(self, f, doc_id, doc_update_policy, revision, import_format): ...
    def paper_docs_users_add(self, doc_id, members, custom_message: Incomplete | None = None, quiet: bool = False): ...
    def paper_docs_users_list(self, doc_id, limit: int = 1000, filter_by=...): ...
    def paper_docs_users_list_continue(self, doc_id, cursor): ...
    def paper_docs_users_remove(self, doc_id, member) -> None: ...
    def paper_folders_create(
        self, name, parent_folder_id: Incomplete | None = None, is_team_folder: Incomplete | None = None
    ): ...
    def sharing_add_file_member(
        self,
        file,
        members,
        custom_message: Incomplete | None = None,
        quiet: bool = False,
        access_level=...,
        add_message_as_comment: bool = False,
    ): ...
    def sharing_add_folder_member(
        self, shared_folder_id, members, quiet: bool = False, custom_message: Incomplete | None = None
    ) -> None: ...
    def sharing_check_job_status(self, async_job_id): ...
    def sharing_check_remove_member_job_status(self, async_job_id): ...
    def sharing_check_share_job_status(self, async_job_id): ...
    def sharing_create_shared_link(self, path, short_url: bool = False, pending_upload: Incomplete | None = None): ...
    def sharing_create_shared_link_with_settings(self, path, settings: Incomplete | None = None): ...
    def sharing_get_file_metadata(self, file, actions: Incomplete | None = None): ...
    def sharing_get_file_metadata_batch(self, files, actions: Incomplete | None = None): ...
    def sharing_get_folder_metadata(self, shared_folder_id, actions: Incomplete | None = None): ...
    def sharing_get_shared_link_file(self, url, path: Incomplete | None = None, link_password: Incomplete | None = None): ...
    def sharing_get_shared_link_file_to_file(
        self, download_path, url, path: Incomplete | None = None, link_password: Incomplete | None = None
    ): ...
    def sharing_get_shared_link_metadata(self, url, path: Incomplete | None = None, link_password: Incomplete | None = None): ...
    def sharing_get_shared_links(self, path: Incomplete | None = None): ...
    def sharing_list_file_members(
        self, file, actions: Incomplete | None = None, include_inherited: bool = True, limit: int = 100
    ): ...
    def sharing_list_file_members_batch(self, files, limit: int = 10): ...
    def sharing_list_file_members_continue(self, cursor): ...
    def sharing_list_folder_members(self, shared_folder_id, actions: Incomplete | None = None, limit: int = 1000): ...
    def sharing_list_folder_members_continue(self, cursor): ...
    def sharing_list_folders(self, limit: int = 1000, actions: Incomplete | None = None): ...
    def sharing_list_folders_continue(self, cursor): ...
    def sharing_list_mountable_folders(self, limit: int = 1000, actions: Incomplete | None = None): ...
    def sharing_list_mountable_folders_continue(self, cursor): ...
    def sharing_list_received_files(self, limit: int = 100, actions: Incomplete | None = None): ...
    def sharing_list_received_files_continue(self, cursor): ...
    def sharing_list_shared_links(
        self, path: Incomplete | None = None, cursor: Incomplete | None = None, direct_only: Incomplete | None = None
    ): ...
    def sharing_modify_shared_link_settings(self, url, settings, remove_expiration: bool = False): ...
    def sharing_mount_folder(self, shared_folder_id): ...
    def sharing_relinquish_file_membership(self, file) -> None: ...
    def sharing_relinquish_folder_membership(self, shared_folder_id, leave_a_copy: bool = False): ...
    def sharing_remove_file_member(self, file, member): ...
    def sharing_remove_file_member_2(self, file, member): ...
    def sharing_remove_folder_member(self, shared_folder_id, member, leave_a_copy): ...
    def sharing_revoke_shared_link(self, url) -> None: ...
    def sharing_set_access_inheritance(self, shared_folder_id, access_inheritance=...): ...
    def sharing_share_folder(
        self,
        path,
        acl_update_policy: Incomplete | None = None,
        force_async: bool = False,
        member_policy: Incomplete | None = None,
        shared_link_policy: Incomplete | None = None,
        viewer_info_policy: Incomplete | None = None,
        access_inheritance=...,
        actions: Incomplete | None = None,
        link_settings: Incomplete | None = None,
    ): ...
    def sharing_transfer_folder(self, shared_folder_id, to_dropbox_id) -> None: ...
    def sharing_unmount_folder(self, shared_folder_id) -> None: ...
    def sharing_unshare_file(self, file) -> None: ...
    def sharing_unshare_folder(self, shared_folder_id, leave_a_copy: bool = False): ...
    def sharing_update_file_member(self, file, member, access_level): ...
    def sharing_update_folder_member(self, shared_folder_id, member, access_level): ...
    def sharing_update_folder_policy(
        self,
        shared_folder_id,
        member_policy: Incomplete | None = None,
        acl_update_policy: Incomplete | None = None,
        viewer_info_policy: Incomplete | None = None,
        shared_link_policy: Incomplete | None = None,
        link_settings: Incomplete | None = None,
        actions: Incomplete | None = None,
    ): ...
    def users_features_get_values(self, features): ...
    def users_get_account(self, account_id): ...
    def users_get_account_batch(self, account_ids): ...
    def users_get_current_account(self): ...
    def users_get_space_usage(self): ...
