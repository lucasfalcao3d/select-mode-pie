import bpy
from bpy.types import Menu

# spawn an edit mode selection pie (run while object is in edit mode to get a valid output)


class IMAGE_MT_PIE_uvs_select_mode(Menu):
    bl_label = "UV Select Mode"
    bl_idname = "uv_select_mode.pie"

    def draw(self, context):
        layout = self.layout
        
        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator_enum("tool_settings.mesh_select_mode", "type")
        pie.operator_enum("tool_settings.uv_select_mode", "type")
        
        layout.operator_context = 'INVOKE_REGION_WIN'
        tool_settings = context.tool_settings
        
        # Do smart things depending on whether uv_select_sync is on.

        if tool_settings.use_uv_select_sync:
            props = layout.operator("wm.context_set_value", text="Vertex", icon='VERTEXSEL')
            props.value = "(True, False, False)"
            props.data_path = "tool_settings.mesh_select_mode"

            props = layout.operator("wm.context_set_value", text="Edge", icon='EDGESEL')
            props.value = "(False, True, False)"
            props.data_path = "tool_settings.mesh_select_mode"

            props = layout.operator("wm.context_set_value", text="Face", icon='FACESEL')
            props.value = "(False, False, True)"
            props.data_path = "tool_settings.mesh_select_mode"

        else:
            props = layout.operator("wm.context_set_string", text="Vertex", icon='UV_VERTEXSEL')
            props.value = 'VERTEX'
            props.data_path = "tool_settings.uv_select_mode"

            props = layout.operator("wm.context_set_string", text="Edge", icon='UV_EDGESEL')
            props.value = 'EDGE'
            props.data_path = "tool_settings.uv_select_mode"

            props = layout.operator("wm.context_set_string", text="Face", icon='UV_FACESEL')
            props.value = 'FACE'
            props.data_path = "tool_settings.uv_select_mode"

            props = layout.operator("wm.context_set_string", text="Island", icon='UV_ISLANDSEL')
            props.value = 'ISLAND'
            props.data_path = "tool_settings.uv_select_mode"


def register():
    bpy.utils.register_class(IMAGE_MT_PIE_uvs_select_mode) 
    
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="UV Editor")
    kmi = km.keymap_items.new("wm.call_menu_pie", "SPACE", "PRESS").properties.name="uv_select_mode.pie"


def unregister():
    bpy.utils.unregister_class(IMAGE_MT_PIE_uvs_select_mode)


if __name__ == "__main__":
    register()


