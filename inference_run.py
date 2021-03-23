import pathlib
import libcst
import jedi

# import jedi.inference
# jedi.inference.recursion.recursion_limit = 100
# jedi.inference.recursion.total_function_execution_limit = 1200
# jedi.inference.recursion.per_function_execution_limit = 50
# jedi.inference.recursion.per_function_recursion_limit = 50


class Visitor(libcst.CSTVisitor):
    METADATA_DEPENDENCIES = (libcst.metadata.PositionProvider, )

    def __init__(self, script):
        super().__init__()
        self._script = script

    def visit_Call(self, node):
        func_node: libcst.Attribute = node.func
        name_node = self.get_name_node(func_node)
        pos = self.get_metadata(libcst.metadata.PositionProvider, name_node).start
        print(f"checking name in pos {(pos.line, pos.column)} : {self._script.infer(pos.line, pos.column)}")

    @classmethod
    def get_name_node(cls, node) -> libcst.Name:
        """
        name -> name
        self.name -> name
        self.attr.name -> name
        """
        if isinstance(node, libcst.Attribute):
            name_node = node.attr
        elif isinstance(node.value, libcst.Attribute):
            name_node = node.value.attr
        else:
            name_node = node
        return name_node


filename = "example_class.py"


code = pathlib.Path(filename).read_text()
module_tree = libcst.parse_module(code)
wrapped = libcst.MetadataWrapper(module_tree)
wrapped.visit(Visitor(jedi.Script(path=filename)))
