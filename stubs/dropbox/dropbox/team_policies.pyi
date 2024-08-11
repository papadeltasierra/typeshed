from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class CameraUploadsPolicyState(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_other(self): ...

CameraUploadsPolicyState_validator: Incomplete

class ComputerBackupPolicyState(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    default: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_default(self): ...
    def is_other(self): ...

ComputerBackupPolicyState_validator: Incomplete

class EmmState(bb.Union):
    disabled: Incomplete
    optional: Incomplete
    required: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_optional(self): ...
    def is_required(self): ...
    def is_other(self): ...

EmmState_validator: Incomplete

class ExternalDriveBackupPolicyState(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    default: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_default(self): ...
    def is_other(self): ...

ExternalDriveBackupPolicyState_validator: Incomplete

class FileLockingPolicyState(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_other(self): ...

FileLockingPolicyState_validator: Incomplete

class FileProviderMigrationPolicyState(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    default: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_default(self): ...
    def is_other(self): ...

FileProviderMigrationPolicyState_validator: Incomplete

class GroupCreation(bb.Union):
    admins_and_members: Incomplete
    admins_only: Incomplete
    def is_admins_and_members(self): ...
    def is_admins_only(self): ...

GroupCreation_validator: Incomplete

class OfficeAddInPolicy(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_other(self): ...

OfficeAddInPolicy_validator: Incomplete

class PaperDefaultFolderPolicy(bb.Union):
    everyone_in_team: Incomplete
    invite_only: Incomplete
    other: Incomplete
    def is_everyone_in_team(self): ...
    def is_invite_only(self): ...
    def is_other(self): ...

PaperDefaultFolderPolicy_validator: Incomplete

class PaperDeploymentPolicy(bb.Union):
    full: Incomplete
    partial: Incomplete
    other: Incomplete
    def is_full(self): ...
    def is_partial(self): ...
    def is_other(self): ...

PaperDeploymentPolicy_validator: Incomplete

class PaperDesktopPolicy(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_other(self): ...

PaperDesktopPolicy_validator: Incomplete

class PaperEnabledPolicy(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    unspecified: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_unspecified(self): ...
    def is_other(self): ...

PaperEnabledPolicy_validator: Incomplete

class PasswordControlMode(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_other(self): ...

PasswordControlMode_validator: Incomplete

class PasswordStrengthPolicy(bb.Union):
    minimal_requirements: Incomplete
    moderate_password: Incomplete
    strong_password: Incomplete
    other: Incomplete
    def is_minimal_requirements(self): ...
    def is_moderate_password(self): ...
    def is_strong_password(self): ...
    def is_other(self): ...

PasswordStrengthPolicy_validator: Incomplete

class RolloutMethod(bb.Union):
    unlink_all: Incomplete
    unlink_most_inactive: Incomplete
    add_member_to_exceptions: Incomplete
    def is_unlink_all(self): ...
    def is_unlink_most_inactive(self): ...
    def is_add_member_to_exceptions(self): ...

RolloutMethod_validator: Incomplete

class SharedFolderBlanketLinkRestrictionPolicy(bb.Union):
    members: Incomplete
    anyone: Incomplete
    other: Incomplete
    def is_members(self): ...
    def is_anyone(self): ...
    def is_other(self): ...

SharedFolderBlanketLinkRestrictionPolicy_validator: Incomplete

class SharedFolderJoinPolicy(bb.Union):
    from_team_only: Incomplete
    from_anyone: Incomplete
    other: Incomplete
    def is_from_team_only(self): ...
    def is_from_anyone(self): ...
    def is_other(self): ...

SharedFolderJoinPolicy_validator: Incomplete

class SharedFolderMemberPolicy(bb.Union):
    team: Incomplete
    anyone: Incomplete
    other: Incomplete
    def is_team(self): ...
    def is_anyone(self): ...
    def is_other(self): ...

SharedFolderMemberPolicy_validator: Incomplete

class SharedLinkCreatePolicy(bb.Union):
    default_public: Incomplete
    default_team_only: Incomplete
    team_only: Incomplete
    default_no_one: Incomplete
    other: Incomplete
    def is_default_public(self): ...
    def is_default_team_only(self): ...
    def is_team_only(self): ...
    def is_default_no_one(self): ...
    def is_other(self): ...

SharedLinkCreatePolicy_validator: Incomplete

class ShowcaseDownloadPolicy(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_other(self): ...

ShowcaseDownloadPolicy_validator: Incomplete

class ShowcaseEnabledPolicy(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_other(self): ...

ShowcaseEnabledPolicy_validator: Incomplete

class ShowcaseExternalSharingPolicy(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_other(self): ...

ShowcaseExternalSharingPolicy_validator: Incomplete

class SmartSyncPolicy(bb.Union):
    local: Incomplete
    on_demand: Incomplete
    other: Incomplete
    def is_local(self): ...
    def is_on_demand(self): ...
    def is_other(self): ...

SmartSyncPolicy_validator: Incomplete

class SmarterSmartSyncPolicyState(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_other(self): ...

SmarterSmartSyncPolicyState_validator: Incomplete

class SsoPolicy(bb.Union):
    disabled: Incomplete
    optional: Incomplete
    required: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_optional(self): ...
    def is_required(self): ...
    def is_other(self): ...

SsoPolicy_validator: Incomplete

class SuggestMembersPolicy(bb.Union):
    disabled: Incomplete
    enabled: Incomplete
    other: Incomplete
    def is_disabled(self): ...
    def is_enabled(self): ...
    def is_other(self): ...

SuggestMembersPolicy_validator: Incomplete

class TeamMemberPolicies(bb.Struct):
    sharing: Incomplete
    emm_state: Incomplete
    office_addin: Incomplete
    suggest_members_policy: Incomplete
    def __init__(
        self,
        sharing: Incomplete | None = None,
        emm_state: Incomplete | None = None,
        office_addin: Incomplete | None = None,
        suggest_members_policy: Incomplete | None = None,
    ) -> None: ...

TeamMemberPolicies_validator: Incomplete

class TeamSharingPolicies(bb.Struct):
    shared_folder_member_policy: Incomplete
    shared_folder_join_policy: Incomplete
    shared_link_create_policy: Incomplete
    group_creation_policy: Incomplete
    shared_folder_link_restriction_policy: Incomplete
    def __init__(
        self,
        shared_folder_member_policy: Incomplete | None = None,
        shared_folder_join_policy: Incomplete | None = None,
        shared_link_create_policy: Incomplete | None = None,
        group_creation_policy: Incomplete | None = None,
        shared_folder_link_restriction_policy: Incomplete | None = None,
    ) -> None: ...

TeamSharingPolicies_validator: Incomplete

class TwoStepVerificationPolicy(bb.Union):
    require_tfa_enable: Incomplete
    require_tfa_disable: Incomplete
    other: Incomplete
    def is_require_tfa_enable(self): ...
    def is_require_tfa_disable(self): ...
    def is_other(self): ...

TwoStepVerificationPolicy_validator: Incomplete

class TwoStepVerificationState(bb.Union):
    required: Incomplete
    optional: Incomplete
    disabled: Incomplete
    other: Incomplete
    def is_required(self): ...
    def is_optional(self): ...
    def is_disabled(self): ...
    def is_other(self): ...

TwoStepVerificationState_validator: Incomplete
ROUTES: Incomplete
