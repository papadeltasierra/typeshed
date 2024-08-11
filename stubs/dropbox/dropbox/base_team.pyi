import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

from dropbox import (
    account as account,
    auth as auth,
    check as check,
    common as common,
    contacts as contacts,
    file_requests as file_requests,
    files as files,
    openid as openid,
    paper as paper,
    secondary_emails as secondary_emails,
    seen_state as seen_state,
    sharing as sharing,
    team_common as team_common,
    team_policies as team_policies,
    users_common as users_common,
)

class DropboxTeamBase(metaclass=abc.ABCMeta):
    __metaclass__ = ABCMeta
    @abstractmethod
    def request(self, route, namespace, request_arg, request_binary, timeout: Incomplete | None = None): ...
    def file_properties_templates_add_for_team(self, name, description, fields): ...
    def file_properties_templates_get_for_team(self, template_id): ...
    def file_properties_templates_list_for_team(self): ...
    def file_properties_templates_remove_for_team(self, template_id) -> None: ...
    def file_properties_templates_update_for_team(
        self,
        template_id,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        add_fields: Incomplete | None = None,
    ): ...
    def team_devices_list_member_devices(
        self,
        team_member_id,
        include_web_sessions: bool = True,
        include_desktop_clients: bool = True,
        include_mobile_clients: bool = True,
    ): ...
    def team_devices_list_members_devices(
        self,
        cursor: Incomplete | None = None,
        include_web_sessions: bool = True,
        include_desktop_clients: bool = True,
        include_mobile_clients: bool = True,
    ): ...
    def team_devices_list_team_devices(
        self,
        cursor: Incomplete | None = None,
        include_web_sessions: bool = True,
        include_desktop_clients: bool = True,
        include_mobile_clients: bool = True,
    ): ...
    def team_devices_revoke_device_session(self, arg) -> None: ...
    def team_devices_revoke_device_session_batch(self, revoke_devices): ...
    def team_features_get_values(self, features): ...
    def team_get_info(self): ...
    def team_groups_create(
        self,
        group_name,
        add_creator_as_owner: bool = False,
        group_external_id: Incomplete | None = None,
        group_management_type: Incomplete | None = None,
    ): ...
    def team_groups_delete(self, arg): ...
    def team_groups_get_info(self, arg): ...
    def team_groups_job_status_get(self, async_job_id): ...
    def team_groups_list(self, limit: int = 1000): ...
    def team_groups_list_continue(self, cursor): ...
    def team_groups_members_add(self, group, members, return_members: bool = True): ...
    def team_groups_members_list(self, group, limit: int = 1000): ...
    def team_groups_members_list_continue(self, cursor): ...
    def team_groups_members_remove(self, group, users, return_members: bool = True): ...
    def team_groups_members_set_access_type(self, group, user, access_type, return_members: bool = True): ...
    def team_groups_update(
        self,
        group,
        return_members: bool = True,
        new_group_name: Incomplete | None = None,
        new_group_external_id: Incomplete | None = None,
        new_group_management_type: Incomplete | None = None,
    ): ...
    def team_legal_holds_create_policy(
        self,
        name,
        members,
        description: Incomplete | None = None,
        start_date: Incomplete | None = None,
        end_date: Incomplete | None = None,
    ): ...
    def team_legal_holds_get_policy(self, id): ...
    def team_legal_holds_list_held_revisions(self, id): ...
    def team_legal_holds_list_held_revisions_continue(self, id, cursor: Incomplete | None = None): ...
    def team_legal_holds_list_policies(self, include_released: bool = False): ...
    def team_legal_holds_release_policy(self, id) -> None: ...
    def team_legal_holds_update_policy(
        self, id, name: Incomplete | None = None, description: Incomplete | None = None, members: Incomplete | None = None
    ): ...
    def team_linked_apps_list_member_linked_apps(self, team_member_id): ...
    def team_linked_apps_list_members_linked_apps(self, cursor: Incomplete | None = None): ...
    def team_linked_apps_list_team_linked_apps(self, cursor: Incomplete | None = None): ...
    def team_linked_apps_revoke_linked_app(self, app_id, team_member_id, keep_app_folder: bool = True) -> None: ...
    def team_linked_apps_revoke_linked_app_batch(self, revoke_linked_app): ...
    def team_member_space_limits_excluded_users_add(self, users: Incomplete | None = None): ...
    def team_member_space_limits_excluded_users_list(self, limit: int = 1000): ...
    def team_member_space_limits_excluded_users_list_continue(self, cursor): ...
    def team_member_space_limits_excluded_users_remove(self, users: Incomplete | None = None): ...
    def team_member_space_limits_get_custom_quota(self, users): ...
    def team_member_space_limits_remove_custom_quota(self, users): ...
    def team_member_space_limits_set_custom_quota(self, users_and_quotas): ...
    def team_members_add_v2(self, new_members, force_async: bool = False): ...
    def team_members_add(self, new_members, force_async: bool = False): ...
    def team_members_add_job_status_get_v2(self, async_job_id): ...
    def team_members_add_job_status_get(self, async_job_id): ...
    def team_members_delete_profile_photo_v2(self, user): ...
    def team_members_delete_profile_photo(self, user): ...
    def team_members_get_available_team_member_roles(self): ...
    def team_members_get_info_v2(self, members): ...
    def team_members_get_info(self, members): ...
    def team_members_list_v2(self, limit: int = 1000, include_removed: bool = False): ...
    def team_members_list(self, limit: int = 1000, include_removed: bool = False): ...
    def team_members_list_continue_v2(self, cursor): ...
    def team_members_list_continue(self, cursor): ...
    def team_members_move_former_member_files(self, user, transfer_dest_id, transfer_admin_id): ...
    def team_members_move_former_member_files_job_status_check(self, async_job_id): ...
    def team_members_recover(self, user) -> None: ...
    def team_members_remove(
        self,
        user,
        wipe_data: bool = True,
        transfer_dest_id: Incomplete | None = None,
        transfer_admin_id: Incomplete | None = None,
        keep_account: bool = False,
        retain_team_shares: bool = False,
    ): ...
    def team_members_remove_job_status_get(self, async_job_id): ...
    def team_members_secondary_emails_add(self, new_secondary_emails): ...
    def team_members_secondary_emails_delete(self, emails_to_delete): ...
    def team_members_secondary_emails_resend_verification_emails(self, emails_to_resend): ...
    def team_members_send_welcome_email(self, arg) -> None: ...
    def team_members_set_admin_permissions_v2(self, user, new_roles: Incomplete | None = None): ...
    def team_members_set_admin_permissions(self, user, new_role): ...
    def team_members_set_profile_v2(
        self,
        user,
        new_email: Incomplete | None = None,
        new_external_id: Incomplete | None = None,
        new_given_name: Incomplete | None = None,
        new_surname: Incomplete | None = None,
        new_persistent_id: Incomplete | None = None,
        new_is_directory_restricted: Incomplete | None = None,
    ): ...
    def team_members_set_profile(
        self,
        user,
        new_email: Incomplete | None = None,
        new_external_id: Incomplete | None = None,
        new_given_name: Incomplete | None = None,
        new_surname: Incomplete | None = None,
        new_persistent_id: Incomplete | None = None,
        new_is_directory_restricted: Incomplete | None = None,
    ): ...
    def team_members_set_profile_photo_v2(self, user, photo): ...
    def team_members_set_profile_photo(self, user, photo): ...
    def team_members_suspend(self, user, wipe_data: bool = True) -> None: ...
    def team_members_unsuspend(self, user) -> None: ...
    def team_namespaces_list(self, limit: int = 1000): ...
    def team_namespaces_list_continue(self, cursor): ...
    def team_properties_template_add(self, name, description, fields): ...
    def team_properties_template_get(self, template_id): ...
    def team_properties_template_list(self): ...
    def team_properties_template_update(
        self,
        template_id,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        add_fields: Incomplete | None = None,
    ): ...
    def team_reports_get_activity(self, start_date: Incomplete | None = None, end_date: Incomplete | None = None): ...
    def team_reports_get_devices(self, start_date: Incomplete | None = None, end_date: Incomplete | None = None): ...
    def team_reports_get_membership(self, start_date: Incomplete | None = None, end_date: Incomplete | None = None): ...
    def team_reports_get_storage(self, start_date: Incomplete | None = None, end_date: Incomplete | None = None): ...
    def team_sharing_allowlist_add(self, domains: Incomplete | None = None, emails: Incomplete | None = None): ...
    def team_sharing_allowlist_list(self, limit: int = 1000): ...
    def team_sharing_allowlist_list_continue(self, cursor): ...
    def team_sharing_allowlist_remove(self, domains: Incomplete | None = None, emails: Incomplete | None = None): ...
    def team_team_folder_activate(self, team_folder_id): ...
    def team_team_folder_archive(self, team_folder_id, force_async_off: bool = False): ...
    def team_team_folder_archive_check(self, async_job_id): ...
    def team_team_folder_create(self, name, sync_setting: Incomplete | None = None): ...
    def team_team_folder_get_info(self, team_folder_ids): ...
    def team_team_folder_list(self, limit: int = 1000): ...
    def team_team_folder_list_continue(self, cursor): ...
    def team_team_folder_permanently_delete(self, team_folder_id) -> None: ...
    def team_team_folder_rename(self, team_folder_id, name): ...
    def team_team_folder_update_sync_settings(
        self, team_folder_id, sync_setting: Incomplete | None = None, content_sync_settings: Incomplete | None = None
    ): ...
    def team_token_get_authenticated_admin(self): ...
    def team_log_get_events(
        self,
        limit: int = 1000,
        account_id: Incomplete | None = None,
        time: Incomplete | None = None,
        category: Incomplete | None = None,
        event_type: Incomplete | None = None,
    ): ...
    def team_log_get_events_continue(self, cursor): ...
