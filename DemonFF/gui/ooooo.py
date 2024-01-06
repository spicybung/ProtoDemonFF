import bpy
import struct
from bpy_extras.io_utils import ExportHelper
from ..ops import col_exporter


#######################################################
class EXPORT_OT_col(bpy.types.Operator, ExportHelper):
    
    bl_idname      = "export_col.scene"
    bl_description = "Export a SAMP Collision File"
    bl_label       = "DragonFF Collision for SAMP/open.mp(.col)"
    filename_ext   = ".col.samp"

    filepath       : bpy.props.StringProperty(name="File path",
                                              maxlen=1024,
                                              default="",
                                              subtype='FILE_PATH')
    
    filter_glob    : bpy.props.StringProperty(default="*.col.samp",
                                              options={'HIDDEN'})
    
    directory      : bpy.props.StringProperty(maxlen=1024,
                                              default="",
                                              subtype='FILE_PATH')

    only_selected   :  bpy.props.BoolProperty(
        name        = "Only Selected",
        default     = False
    )
    
    export_version  : bpy.props.EnumProperty(
        items =
        (
            ('1', "GTA 3/VC (COLL)", "Grand Theft Auto 3 and Vice City (PC) - Version 1"),
            ('3', "GTA SA/MP (COL3)", "Grand Theft Auto SA (PC/Xbox) - Coll Version 3"),
            ('2', "GTA SA PS2 (COL2)", "Grand Theft Auto SA (PS2) - Version 2")
        ),
        name = "Version Export"
    )

    #######################################################
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "export_version")
        layout.prop(self, "only_selected")
        return None


    #######################################################
    def get_dff_objects():
        # Retrieve DFF objects here, based on your scene structure
        # For example:
        dff_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH' and obj.name.endswith('.dff')]
        return dff_objects

    #######################################################
    def execute(self, context):
        

        file_path = "/path/to/each/dff_file"

        col_exporter.export_col(
            {
                "file_name"      : file_path,
                "version"        : int(self.export_version),
                "collection"     : None,
                "memory"         : False,
                "mass_export"    : True,
                "only_selected"  : self.only_selected
            }
        )

        # Modify the exported .col file
        # Define the path to the exported .col file
        col_file_path = self.filepath

        # Define the new values to be written
        new_values = [0x73, 0x61, 0x6D, 0x70]

        # Open the .col file in binary mode
        with open(col_file_path, 'r+b') as file:
       # Move to the desired offset (0x47C94)
             # Seek to the specified offsets (08, 09, 0A, 0B)
                offsets_to_modify = [0x00000010]
                for offset, value in zip(offsets_to_modify, new_values):
                    file.seek(offset)
                    packed_value = struct.pack('B', value)
                    file.write(packed_value)  # Write the packed value to the file




        print("New values written at offset [0x03] in the first extension within the DFF file after export.")

  

        # Save settings of the export in scene custom properties for later
        context.scene['dragonff_imported_version_col'] = self.export_version
            
        return {'FINISHED'}

    #######################################################
    def invoke(self, context, event):
        if 'dragonff_imported_version_col' in context.scene:
            self.export_version = context.scene['dragonff_imported_version_col']
        
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}