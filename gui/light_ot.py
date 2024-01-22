import bpy
import os
from bpy_extras.io_utils import ImportHelper, ExportHelper
import time

from ..ops import dff_exporter, dff_importer, col_importer

#######################################################
class LIGHT_OT_EXPORT:
    gFlags1 = 0
    gflags2 = 0

    effects = ["prt_blood", "prt_boatsplash", "prt_bubble", "prt_cardebris",
            "prt_collisionsmoke", "prt_glass", "prt_gunshell", "prt_sand",
            "prt_sand2", "prt_smokeII_3_expand", "prt_smoke_huge", "prt_spark",
            "prt_spark_2", "prt_splash", "prt_wake", "prt_watersplash",
            "prt_wheeldirt", "boat_prop", "camflash", "exhale", "explosion_fuel_car",
            "explosion_large", "explosion_medium", "explosion_molotov", "explosion_small",
            "explosion_tiny", "extinguisher", "fire", "fire_bike", "fire_car",
            "fire_large", "fire_med", "flamethrower", "gunflash", "gunsmoke",
            "heli_dust", "jetpack", "jetthrust", "molotov_flame", "nitro",
            "overheat_car", "overheat_car_electric", "riot_smoke", "spraycan",
            "tank_fire", "teargas", "teargasAD", "water_hydrant", "water_ripples",
            "water_speed", "water_splash", "water_splash_big", "water_splsh_sml",
            "water_swim", "cigarette_smoke", "Flame", "insects", "smoke30lit",
            "smoke30m", "smoke50lit", "vent", "vent2", "waterfall_end",
            "water_fnt_tme", "water_fountain", "tree_hit_fir", "tree_hit_palm",
            "blood_heli", "carwashspray", "cement", "cloudfast", "coke_puff", "coke_trail",
            "explosion_barrel", "explosion_crate", "explosion_door",
            "petrolcan", "puke", "shootlight", "smoke_flare", "wallbust", "ws_factorysmoke"]

    selected_effect = None

#######################################################

class DFF2dfxPanel(bpy.types.Panel):
        bl_label = "2DFX"
        bl_idname = "PT_DFF2DFX"
        bl_space_type = 'VIEW_3D'
        bl_region_type = 'UI'
        bl_category = 'Tools'
        bl_context = 'object'

#######################################################

        def draw(self, context):
            layout = self.layout

            layout.operator("dff2dfx.light_operator", text="LIGHT")
            layout.operator("dff2dfx.particle_operator", text="Particle")
            layout.operator("dff2dfx.sign_operator", text="Sign")
            layout.operator("dff2dfx.slotmachine_operator", text="Slotmachine")
            layout.operator("dff2dfx.escalator_operator", text="Escalator")

#######################################################

class DFF2dfxLightOperator(bpy.types.Operator):
    bl_idname = "dff2dfx.light_operator"
    bl_label = "Light Export"

#######################################################

    def execute(self, context):
        # Add your light export code here
        return {'FINISHED'}
    
#######################################################

class DFF2dfxParticleOperator(bpy.types.Operator):
    bl_idname = "dff2dfx.particle_operator"
    bl_label = "Particle Export"

#######################################################

    def execute(self, context):
        # Add your particle export code here
        return {'FINISHED'}

#######################################################

class DFF2dfxSignOperator(bpy.types.Operator):
    bl_idname = "dff2dfx.sign_operator"
    bl_label = "Sign Export"

#######################################################

    def execute(self, context):
        # Add your sign export code here
        return {'FINISHED'}
    
#######################################################

class DFF2dfxSlotmachineOperator(bpy.types.Operator):
    bl_idname = "dff2dfx.slotmachine_operator"
    bl_label = "Slotmachine Export"

#######################################################


    def execute(self, context):
        # Add your slotmachine export code here
        return {'FINISHED'}
    
#######################################################

class DFF2dfxEscalatorOperator(bpy.types.Operator):
    bl_idname = "dff2dfx.escalator_operator"
    bl_label = "Escalator Export"

#######################################################

    def execute(self, context):
        # Add your escalator export code here
        return {'FINISHED'}
    
#######################################################

def menu_func(self, context):
    self.layout.operator(DFF2dfxLightOperator.bl_idname)
    self.layout.operator(DFF2dfxParticleOperator.bl_idname)
    self.layout.operator(DFF2dfxSignOperator.bl_idname)
    self.layout.operator(DFF2dfxSlotmachineOperator.bl_idname)
    self.layout.operator(DFF2dfxEscalatorOperator.bl_idname)

#######################################################

def register():
    bpy.utils.register_class(DFF2dfxPanel)
    bpy.utils.register_class(DFF2dfxLightOperator)
    bpy.utils.register_class(DFF2dfxParticleOperator)
    bpy.utils.register_class(DFF2dfxSignOperator)
    bpy.utils.register_class(DFF2dfxSlotmachineOperator)
    bpy.utils.register_class(DFF2dfxEscalatorOperator)
    bpy.types.VIEW3D_MT_mesh.append(menu_func)

#######################################################

def unregister():
    bpy.utils.unregister_class(DFF2dfxPanel)
    bpy.utils.unregister_class(DFF2dfxLightOperator)
    bpy.utils.unregister_class(DFF2dfxParticleOperator)
    bpy.utils.unregister_class(DFF2dfxSignOperator)
    bpy.utils.unregister_class(DFF2dfxSlotmachineOperator)
    bpy.utils.unregister_class(DFF2dfxEscalatorOperator)
    bpy.types.VIEW3D_MT_mesh.remove(menu_func)

#######################################################

if __name__ == "__main__":
    register()