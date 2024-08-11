from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class AddPropertiesArg(bb.Struct):
    path: Incomplete
    property_groups: Incomplete
    def __init__(self, path: Incomplete | None = None, property_groups: Incomplete | None = None) -> None: ...

AddPropertiesArg_validator: Incomplete

class TemplateError(bb.Union):
    restricted_content: Incomplete
    other: Incomplete
    @classmethod
    def template_not_found(cls, val): ...
    def is_template_not_found(self): ...
    def is_restricted_content(self): ...
    def is_other(self): ...
    def get_template_not_found(self): ...

TemplateError_validator: Incomplete

class PropertiesError(TemplateError):
    unsupported_folder: Incomplete
    @classmethod
    def path(cls, val): ...
    def is_path(self): ...
    def is_unsupported_folder(self): ...
    def get_path(self): ...

PropertiesError_validator: Incomplete

class InvalidPropertyGroupError(PropertiesError):
    property_field_too_large: Incomplete
    does_not_fit_template: Incomplete
    duplicate_property_groups: Incomplete
    def is_property_field_too_large(self): ...
    def is_does_not_fit_template(self): ...
    def is_duplicate_property_groups(self): ...

InvalidPropertyGroupError_validator: Incomplete

class AddPropertiesError(InvalidPropertyGroupError):
    property_group_already_exists: Incomplete
    def is_property_group_already_exists(self): ...

AddPropertiesError_validator: Incomplete

class PropertyGroupTemplate(bb.Struct):
    name: Incomplete
    description: Incomplete
    fields: Incomplete
    def __init__(
        self, name: Incomplete | None = None, description: Incomplete | None = None, fields: Incomplete | None = None
    ) -> None: ...

PropertyGroupTemplate_validator: Incomplete

class AddTemplateArg(PropertyGroupTemplate):
    def __init__(
        self, name: Incomplete | None = None, description: Incomplete | None = None, fields: Incomplete | None = None
    ) -> None: ...

AddTemplateArg_validator: Incomplete

class AddTemplateResult(bb.Struct):
    template_id: Incomplete
    def __init__(self, template_id: Incomplete | None = None) -> None: ...

AddTemplateResult_validator: Incomplete

class GetTemplateArg(bb.Struct):
    template_id: Incomplete
    def __init__(self, template_id: Incomplete | None = None) -> None: ...

GetTemplateArg_validator: Incomplete

class GetTemplateResult(PropertyGroupTemplate):
    def __init__(
        self, name: Incomplete | None = None, description: Incomplete | None = None, fields: Incomplete | None = None
    ) -> None: ...

GetTemplateResult_validator: Incomplete

class ListTemplateResult(bb.Struct):
    template_ids: Incomplete
    def __init__(self, template_ids: Incomplete | None = None) -> None: ...

ListTemplateResult_validator: Incomplete

class LogicalOperator(bb.Union):
    or_operator: Incomplete
    other: Incomplete
    def is_or_operator(self): ...
    def is_other(self): ...

LogicalOperator_validator: Incomplete

class LookUpPropertiesError(bb.Union):
    property_group_not_found: Incomplete
    other: Incomplete
    def is_property_group_not_found(self): ...
    def is_other(self): ...

LookUpPropertiesError_validator: Incomplete

class LookupError(bb.Union):
    not_found: Incomplete
    not_file: Incomplete
    not_folder: Incomplete
    restricted_content: Incomplete
    other: Incomplete
    @classmethod
    def malformed_path(cls, val): ...
    def is_malformed_path(self): ...
    def is_not_found(self): ...
    def is_not_file(self): ...
    def is_not_folder(self): ...
    def is_restricted_content(self): ...
    def is_other(self): ...
    def get_malformed_path(self): ...

LookupError_validator: Incomplete

class ModifyTemplateError(TemplateError):
    conflicting_property_names: Incomplete
    too_many_properties: Incomplete
    too_many_templates: Incomplete
    template_attribute_too_large: Incomplete
    def is_conflicting_property_names(self): ...
    def is_too_many_properties(self): ...
    def is_too_many_templates(self): ...
    def is_template_attribute_too_large(self): ...

ModifyTemplateError_validator: Incomplete

class OverwritePropertyGroupArg(bb.Struct):
    path: Incomplete
    property_groups: Incomplete
    def __init__(self, path: Incomplete | None = None, property_groups: Incomplete | None = None) -> None: ...

OverwritePropertyGroupArg_validator: Incomplete

class PropertiesSearchArg(bb.Struct):
    queries: Incomplete
    template_filter: Incomplete
    def __init__(self, queries: Incomplete | None = None, template_filter: Incomplete | None = None) -> None: ...

PropertiesSearchArg_validator: Incomplete

class PropertiesSearchContinueArg(bb.Struct):
    cursor: Incomplete
    def __init__(self, cursor: Incomplete | None = None) -> None: ...

PropertiesSearchContinueArg_validator: Incomplete

class PropertiesSearchContinueError(bb.Union):
    reset: Incomplete
    other: Incomplete
    def is_reset(self): ...
    def is_other(self): ...

PropertiesSearchContinueError_validator: Incomplete

class PropertiesSearchError(bb.Union):
    other: Incomplete
    @classmethod
    def property_group_lookup(cls, val): ...
    def is_property_group_lookup(self): ...
    def is_other(self): ...
    def get_property_group_lookup(self): ...

PropertiesSearchError_validator: Incomplete

class PropertiesSearchMatch(bb.Struct):
    id: Incomplete
    path: Incomplete
    is_deleted: Incomplete
    property_groups: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        path: Incomplete | None = None,
        is_deleted: Incomplete | None = None,
        property_groups: Incomplete | None = None,
    ) -> None: ...

PropertiesSearchMatch_validator: Incomplete

class PropertiesSearchMode(bb.Union):
    other: Incomplete
    @classmethod
    def field_name(cls, val): ...
    def is_field_name(self): ...
    def is_other(self): ...
    def get_field_name(self): ...

PropertiesSearchMode_validator: Incomplete

class PropertiesSearchQuery(bb.Struct):
    query: Incomplete
    mode: Incomplete
    logical_operator: Incomplete
    def __init__(
        self, query: Incomplete | None = None, mode: Incomplete | None = None, logical_operator: Incomplete | None = None
    ) -> None: ...

PropertiesSearchQuery_validator: Incomplete

class PropertiesSearchResult(bb.Struct):
    matches: Incomplete
    cursor: Incomplete
    def __init__(self, matches: Incomplete | None = None, cursor: Incomplete | None = None) -> None: ...

PropertiesSearchResult_validator: Incomplete

class PropertyField(bb.Struct):
    name: Incomplete
    value: Incomplete
    def __init__(self, name: Incomplete | None = None, value: Incomplete | None = None) -> None: ...

PropertyField_validator: Incomplete

class PropertyFieldTemplate(bb.Struct):
    name: Incomplete
    description: Incomplete
    type: Incomplete
    def __init__(
        self, name: Incomplete | None = None, description: Incomplete | None = None, type: Incomplete | None = None
    ) -> None: ...

PropertyFieldTemplate_validator: Incomplete

class PropertyGroup(bb.Struct):
    template_id: Incomplete
    fields: Incomplete
    def __init__(self, template_id: Incomplete | None = None, fields: Incomplete | None = None) -> None: ...

PropertyGroup_validator: Incomplete

class PropertyGroupUpdate(bb.Struct):
    template_id: Incomplete
    add_or_update_fields: Incomplete
    remove_fields: Incomplete
    def __init__(
        self,
        template_id: Incomplete | None = None,
        add_or_update_fields: Incomplete | None = None,
        remove_fields: Incomplete | None = None,
    ) -> None: ...

PropertyGroupUpdate_validator: Incomplete

class PropertyType(bb.Union):
    string: Incomplete
    other: Incomplete
    def is_string(self): ...
    def is_other(self): ...

PropertyType_validator: Incomplete

class RemovePropertiesArg(bb.Struct):
    path: Incomplete
    property_template_ids: Incomplete
    def __init__(self, path: Incomplete | None = None, property_template_ids: Incomplete | None = None) -> None: ...

RemovePropertiesArg_validator: Incomplete

class RemovePropertiesError(PropertiesError):
    @classmethod
    def property_group_lookup(cls, val): ...
    def is_property_group_lookup(self): ...
    def get_property_group_lookup(self): ...

RemovePropertiesError_validator: Incomplete

class RemoveTemplateArg(bb.Struct):
    template_id: Incomplete
    def __init__(self, template_id: Incomplete | None = None) -> None: ...

RemoveTemplateArg_validator: Incomplete

class TemplateFilterBase(bb.Union):
    other: Incomplete
    @classmethod
    def filter_some(cls, val): ...
    def is_filter_some(self): ...
    def is_other(self): ...
    def get_filter_some(self): ...

TemplateFilterBase_validator: Incomplete

class TemplateFilter(TemplateFilterBase):
    filter_none: Incomplete
    def is_filter_none(self): ...

TemplateFilter_validator: Incomplete

class TemplateOwnerType(bb.Union):
    user: Incomplete
    team: Incomplete
    other: Incomplete
    def is_user(self): ...
    def is_team(self): ...
    def is_other(self): ...

TemplateOwnerType_validator: Incomplete

class UpdatePropertiesArg(bb.Struct):
    path: Incomplete
    update_property_groups: Incomplete
    def __init__(self, path: Incomplete | None = None, update_property_groups: Incomplete | None = None) -> None: ...

UpdatePropertiesArg_validator: Incomplete

class UpdatePropertiesError(InvalidPropertyGroupError):
    @classmethod
    def property_group_lookup(cls, val): ...
    def is_property_group_lookup(self): ...
    def get_property_group_lookup(self): ...

UpdatePropertiesError_validator: Incomplete

class UpdateTemplateArg(bb.Struct):
    template_id: Incomplete
    name: Incomplete
    description: Incomplete
    add_fields: Incomplete
    def __init__(
        self,
        template_id: Incomplete | None = None,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        add_fields: Incomplete | None = None,
    ) -> None: ...

UpdateTemplateArg_validator: Incomplete

class UpdateTemplateResult(bb.Struct):
    template_id: Incomplete
    def __init__(self, template_id: Incomplete | None = None) -> None: ...

UpdateTemplateResult_validator: Incomplete
Id_validator: Incomplete
PathOrId_validator: Incomplete
PropertiesSearchCursor_validator: Incomplete
TemplateId_validator: Incomplete
properties_add: Incomplete
properties_overwrite: Incomplete
properties_remove: Incomplete
properties_search: Incomplete
properties_search_continue: Incomplete
properties_update: Incomplete
templates_add_for_team: Incomplete
templates_add_for_user: Incomplete
templates_get_for_team: Incomplete
templates_get_for_user: Incomplete
templates_list_for_team: Incomplete
templates_list_for_user: Incomplete
templates_remove_for_team: Incomplete
templates_remove_for_user: Incomplete
templates_update_for_team: Incomplete
templates_update_for_user: Incomplete
ROUTES: Incomplete
