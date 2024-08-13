from _typeshed import Incomplete

class ASTNode:
    path: Incomplete
    lineno: Incomplete
    lexpos: Incomplete
    def __init__(self, path, lineno, lexpos) -> None: ...

class AstNamespace(ASTNode):
    name: Incomplete
    doc: Incomplete
    def __init__(self, path, lineno, lexpos, name, doc) -> None: ...

class AstImport(ASTNode):
    target: Incomplete
    def __init__(self, path, lineno, lexpos, target) -> None: ...

class AstAlias(ASTNode):
    name: Incomplete
    type_ref: Incomplete
    doc: Incomplete
    annotations: Incomplete
    def __init__(self, path, lineno, lexpos, name, type_ref, doc) -> None: ...
    def set_annotations(self, annotations) -> None: ...

class AstTypeDef(ASTNode):
    name: Incomplete
    extends: Incomplete
    doc: Incomplete
    fields: Incomplete
    examples: Incomplete
    def __init__(self, path, lineno, lexpos, name, extends, doc, fields, examples) -> None: ...

class AstStructDef(AstTypeDef):
    subtypes: Incomplete
    def __init__(
        self, path, lineno, lexpos, name, extends, doc, fields, examples, subtypes: Incomplete | None = None
    ) -> None: ...

class AstStructPatch(ASTNode):
    name: Incomplete
    fields: Incomplete
    examples: Incomplete
    def __init__(self, path, lineno, lexpos, name, fields, examples) -> None: ...

class AstUnionDef(AstTypeDef):
    closed: Incomplete
    def __init__(self, path, lineno, lexpos, name, extends, doc, fields, examples, closed: bool = False) -> None: ...

class AstUnionPatch(ASTNode):
    name: Incomplete
    fields: Incomplete
    examples: Incomplete
    closed: Incomplete
    def __init__(self, path, lineno, lexpos, name, fields, examples, closed) -> None: ...

class AstTypeRef(ASTNode):
    name: Incomplete
    args: Incomplete
    nullable: Incomplete
    ns: Incomplete
    def __init__(self, path, lineno, lexpos, name, args, nullable, ns) -> None: ...

class AstTagRef(ASTNode):
    tag: Incomplete
    def __init__(self, path, lineno, lexpos, tag) -> None: ...

class AstAnnotationRef(ASTNode):
    annotation: Incomplete
    ns: Incomplete
    def __init__(self, path, lineno, lexpos, annotation, ns) -> None: ...

class AstAnnotationDef(ASTNode):
    name: Incomplete
    annotation_type: Incomplete
    annotation_type_ns: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, path, lineno, lexpos, name, annotation_type, annotation_type_ns, args, kwargs) -> None: ...

class AstAnnotationTypeDef(ASTNode):
    name: Incomplete
    doc: Incomplete
    params: Incomplete
    def __init__(self, path, lineno, lexpos, name, doc, params) -> None: ...

class AstField(ASTNode):
    name: Incomplete
    type_ref: Incomplete
    doc: Incomplete
    has_default: bool
    default: Incomplete
    annotations: Incomplete
    def __init__(self, path, lineno, lexpos, name, type_ref) -> None: ...
    def set_doc(self, docstring) -> None: ...
    def set_default(self, default) -> None: ...
    def set_annotations(self, annotations) -> None: ...

class AstVoidField(ASTNode):
    name: Incomplete
    doc: Incomplete
    annotations: Incomplete
    def __init__(self, path, lineno, lexpos, name) -> None: ...
    def set_doc(self, docstring) -> None: ...
    def set_annotations(self, annotations) -> None: ...

class AstSubtypeField(ASTNode):
    name: Incomplete
    type_ref: Incomplete
    def __init__(self, path, lineno, lexpos, name, type_ref) -> None: ...

class AstRouteDef(ASTNode):
    name: Incomplete
    version: Incomplete
    deprecated: Incomplete
    arg_type_ref: Incomplete
    result_type_ref: Incomplete
    error_type_ref: Incomplete
    doc: Incomplete
    attrs: Incomplete
    def __init__(
        self,
        path,
        lineno,
        lexpos,
        name,
        version,
        deprecated,
        arg_type_ref,
        result_type_ref,
        error_type_ref: Incomplete | None = None,
    ) -> None: ...
    def set_doc(self, docstring) -> None: ...
    def set_attrs(self, attrs) -> None: ...

class AstAttrField(ASTNode):
    name: Incomplete
    value: Incomplete
    def __init__(self, path, lineno, lexpos, name, value) -> None: ...

class AstExample(ASTNode):
    label: Incomplete
    text: Incomplete
    fields: Incomplete
    def __init__(self, path, lineno, lexpos, label, text, fields) -> None: ...

class AstExampleField(ASTNode):
    name: Incomplete
    value: Incomplete
    def __init__(self, path, lineno, lexpos, name, value) -> None: ...

class AstExampleRef(ASTNode):
    label: Incomplete
    def __init__(self, path, lineno, lexpos, label) -> None: ...
