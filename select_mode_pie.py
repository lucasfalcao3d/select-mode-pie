bl_info = {
    "name": "Select Mode Pie",
    "author": "Lucas Falcao",
    "version": (0, 4),
    "description": "Pie Menu for Select Mode in Edit mode and UV Editor.",
    "blender": (2, 80, 0),
    "category": "3D view, UV"
}

import bpy
from bpy.types import Menu

# Spawn a pie menu for select mode in Edit Mode in the 3D View


class EDIT_SELECT_MODE(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Edit Select Mode"
    bl_idname = "pie.edit_select_mode"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator_enum("mesh.select_mode", "type")
        
# Spawn a pie menu for select mode in UV Editor 

class UV_SELECT_MODE(Menu):
    bl_label = "UV Select Mode"
    bl_idname = "pie.uv_select_mode"

    def draw(self, context):
        layout = self.layout
        
        
        tool_settings = context.tool_settings
        pie = layout.menu_pie()
        
        # Do smart things depending on whether uv_select_sync is on.

        if tool_settings.use_uv_select_sync:
            op = pie.operator("wm.context_set_value", text="Vertex", icon='VERTEXSEL')
            op.value = "(True, False, False)"
            op.data_path = "tool_settings.mesh_select_mode"

            op = pie.operator("wm.context_set_value", text="Edge", icon='EDGESEL')
            op.value = "(False, True, False)"
            op.data_path = "tool_settings.mesh_select_mode"

            op = pie.operator("wm.context_set_value", text="Face", icon='FACESEL')
            op.value = "(False, False, True)"
            op.data_path = "tool_settings.mesh_select_mode"            
            
        else:
            op = pie.operator("wm.context_set_string", text="Vertex", icon='UV_VERTEXSEL')
            op.value = 'VERTEX'
            op.data_path = "tool_settings.uv_select_mode"

            op = pie.operator("wm.context_set_string", text="Edge", icon='UV_EDGESEL')
            op.value = 'EDGE'
            op.data_path = "tool_settings.uv_select_mode"

            op = pie.operator("wm.context_set_string", text="Face", icon='UV_FACESEL')
            op.value = 'FACE'
            op.data_path = "tool_settings.uv_select_mode"

            op = pie.operator("wm.context_set_string", text="Island", icon='UV_ISLANDSEL')
            op.value = 'ISLAND'
            op.data_path = "tool_settings.uv_select_mode"


classes = (
EDIT_SELECT_MODE,
UV_SELECT_MODE,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Mesh")
    kmi = km.keymap_items.new("wm.call_menu_pie", "SPACE", "PRESS").properties.name="pie.edit_select_mode"     
        
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="UV Editor")
    kmi = km.keymap_items.new("wm.call_menu_pie", "SPACE", "PRESS").properties.name="pie.uv_select_mode"  
        
    
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
