import enum
from pysc2.lib.units import Protoss
from pysc2.lib.upgrades import Upgrades
from pysc2.lib.actions import RAW_FUNCTIONS

PAD = -1

upgrades_list = [
    Upgrades.ResonatingGlaives,
    Upgrades.Blink,
    Upgrades.WarpGateResearch,
    Upgrades.Charge,
    Upgrades.PsiStorm,
    Upgrades.ExtendedThermalLance,
    Upgrades.GraviticBooster,
    Upgrades.GraviticDrive,
    Upgrades.GravitonCatapult,
    Upgrades.AnionPulseCrystals,
    Upgrades.ShadowStrike,
]
upgrades_set = set(upgrades_list)
# all_list = units_list[:-1] + buildings_list + [341, 342] + [472, 473, 474] #miniraly/gas + block_rampy
all_list = [i.value for i in list(Protoss)] + [341, 342] + [472, 473, 474] + [PAD]

# units_to_id = dict(zip(units_list, list(range(units_len))))
# buildings_to_id = dict(zip(buildings_list, list(range(buildings_len))))
upgrades_to_id = dict(zip(upgrades_list, list(range(len(upgrades_list)))))
all_to_id = dict(zip(all_list, list(range(len(all_list)))))

units_list = [
    all_to_id[item] for item in 
    [311, 801, 141, 79, 4, 76, 694, 733, 75, 83, 85, 10, 488,
    82, 495, 1911, 78, 84, 70, 71, 77, 74, 496, 80, 81, 136, 73, PAD]
]
units_set = set(units_list)
buildings_list = [
    all_to_id[item] for item in 
    [61, 1955, 72, 69, 64, 63, 62, 59, 66, 60, 894, 70, 71, 1910, 67, 732, 68, 65, 133, PAD]
]
buildings_set = set(buildings_list)
units_len, buildings_len, upgrades_len, all_len = len(units_list), len(buildings_list), len(upgrades_list), len(all_list)


class SpecialTypes(enum.IntEnum):
    Any = -1
    AnyOwn = -2
    AnyOwnBuilding = -3
    AnyOwnUnit = -4
    OwnBattleUnit = -5
    AnyEnemy = -6
    AnyEnemyBuilding = -7
    AnyEnemyUnit = -8
    OwnTemplars = -9
    GasAssim = -10

class ActionTypes(enum.IntEnum):
    quick = 0
    pt = 1
    unit = 2
    autocast = 3
    no_arg = 4
    
global_behavior = {
    'economy': [
        "Train_Probe_quick",
        "Build_Nexus_pt",
        "Build_Assimilator_unit",
        "Effect_ChronoBoostEnergyCost_unit"
    ],
    'production': [
        "Build_Gateway_pt",
        "Build_RoboticsFacility_pt",
        "Build_Stargate_pt",
        "Effect_ChronoBoostEnergyCost_unit"
    ],
    'tech': [
        "Build_Forge_pt",
        "Build_CyberneticsCore_pt",
        "Build_TwilightCouncil_pt",
        "Build_TemplarArchive_pt",
        "Build_DarkShrine_pt",
        "Build_FleetBeacon_pt",
        "Build_RoboticsBay_pt"
    ],
    'army': [
        "Train_Zealot_quick",
        "Train_Stalker_quick",
        "Train_Sentry_quick",
        "Train_Adept_quick",
        "Train_HighTemplar_quick",
        "Train_DarkTemplar_quick",
        "Train_Observer_quick",
        "Train_Immortal_quick",
        "Train_WarpPrism_quick",
        "Train_Colossus_quick",
        "Train_Phoenix_quick",
        "Train_VoidRay_quick",
        "Train_Carrier_quick",
        "Train_Tempest_quick",
        "Train_Mothership_quick",
        "TrainWarp_Zealot_pt",
        "TrainWarp_Stalker_pt",
        "TrainWarp_Sentry_pt",
        "TrainWarp_Adept_pt",
        "TrainWarp_HighTemplar_pt",
        "TrainWarp_DarkTemplar_pt",
        "Train_Oracle_quick",
        "Build_Interceptors_autocast",
        "Build_Interceptors_quick",
        "Morph_Archon_quick",
        "Train_Disruptor_quick"
    ],
    'pylon': [
        "Build_Pylon_pt"
    ],
    'defend': [
        "Build_PhotonCannon_pt",
        "Build_ShieldBattery_pt"
    ],
    'move_army': [
        "Attack_pt",
        "Attack_unit",
        "Move_pt",
        "Move_unit",
        "Patrol_pt",
        "Patrol_unit",
        "Stop_quick",
        "HoldPosition_quick"
    ],
    'micro_army': [
        "Attack_pt",
        "Attack_unit",
        "Move_pt",
        "Move_unit",
        "Patrol_pt",
        "Patrol_unit",
        "Stop_quick",
        "HoldPosition_quick"
    ],
    'skills': [
        "Cancel_VoidRayPrismaticAlignment_quick",
        "Effect_AdeptPhaseShift_pt",
        "Effect_Blink_Stalker_pt",
        "Effect_Charge_autocast",
        "Effect_Charge_pt",
        "Effect_Charge_unit",
        "Effect_Feedback_unit",
        "Effect_ForceField_pt",
        "Effect_GravitonBeam_unit",
        "Effect_GuardianShield_quick",
        "Effect_MassRecall_Mothership_pt",
        "Effect_MassRecall_StrategicRecall_pt",
        "Effect_PurificationNova_pt",
        "Effect_PsiStorm_pt",
        "Effect_TimeWarp_pt",
        "Effect_VoidRayPrismaticAlignment_quick",
    ],
    'move_probes': [
        "Attack_pt",
        "Attack_unit",
        "Move_pt",
        "Move_unit",
        "Stop_quick",
        "HoldPosition_quick",
        "Harvest_Gather_Probe_unit",
        "Harvest_Return_Probe_quick",
    ],
    'upgrade': [
        "Research_AdeptResonatingGlaives_quick",
        "Research_Blink_quick",
        "Research_Charge_quick",
        "Research_ExtendedThermalLance_quick",
        "Research_GraviticBooster_quick",
        "Research_GraviticDrive_quick",
        "Research_InterceptorGravitonCatapult_quick",
        "Research_PhoenixAnionPulseCrystals_quick",
        "Research_ProtossAirArmor_quick",
        "Research_ProtossAirWeapons_quick",
        "Research_ProtossGroundArmor_quick",
        "Research_ProtossGroundWeapons_quick",   
        "Research_ProtossShields_quick",
        "Research_PsiStorm_quick",
        "Research_ShadowStrike_quick",
        "Research_WarpGate_quick",
        "Effect_ChronoBoostEnergyCost_unit"
    ],
    'skip': [
        "no_op"
    ],
    'cancel': [
        "Cancel_quick"
    ]
}
    
    
action_info = {
    #economy
    "Train_Probe_quick": {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Nexus],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 50,
            'gas': 0,
            'limit': 1,
        }
    },
    "Build_Nexus_pt": {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 400,
            'gas': 0,
            'limit': 0,
            'power': False
        }
    },
    "Build_Assimilator_unit": {
        'type': ActionTypes.unit,
        'actors': all_to_id[Protoss.Probe],
        'target': all_to_id[342],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 75,
            'gas': 0,
            'limit': 0,
        }
    },
    "Effect_ChronoBoostEnergyCost_unit" : {
        'type': ActionTypes.unit,
        'actors': all_to_id[Protoss.Nexus],
        'target': SpecialTypes.AnyOwnBuilding,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "Harvest_Gather_Probe_unit" : {
        'type': ActionTypes.unit,
        'actors': all_to_id[Protoss.Probe],
        'target': SpecialTypes.GasAssim,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "Harvest_Return_Probe_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    #production
    "Build_Gateway_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [all_to_id[Protoss.Pylon]],
            'research': [],
            'minerals': 150,
            'gas': 0,
            'limit': 0,
            'power': True
        }
    },
    "Build_RoboticsFacility_pt": {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [all_to_id[Protoss.CyberneticsCore]],
            'research': [],
            'minerals': 150,
            'gas': 100,
            'limit': 0,
            'power': True
        }
    },
    "Build_Stargate_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [all_to_id[Protoss.CyberneticsCore]],
            'research': [],
            'minerals': 150,
            'gas': 150,
            'limit': 0,
            'power': True
        }
    },
    #tech
    "Build_Forge_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 150,
            'gas': 0,
            'limit': 0,
            'power': True
        }
    },
    #########SPEICIAL CASE###############
    "Build_CyberneticsCore_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [all_to_id[Protoss.Gateway], all_to_id[Protoss.WarpGate]],
            'research': [],
            'minerals': 150,
            'gas': 0,
            'limit': 0,
            'power': True
        }
    },
    "Build_TwilightCouncil_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [all_to_id[Protoss.CyberneticsCore]],
            'research': [],
            'minerals': 150,
            'gas': 100,
            'limit': 0,
            'power': True
        }
    },
    "Build_TemplarArchive_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [all_to_id[Protoss.TwilightCouncil]],
            'research': [],
            'minerals': 150,
            'gas': 200,
            'limit': 0,
            'power': True
        }
    },
    "Build_DarkShrine_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [all_to_id[Protoss.TwilightCouncil]],
            'research': [],
            'minerals': 150,
            'gas': 150,
            'limit': 0,
            'power': True
        }
    },
    "Build_FleetBeacon_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [all_to_id[Protoss.Stargate]],
            'research': [],
            'minerals': 300,
            'gas': 200,
            'limit': 0,
            'power': True
        }
    },
    "Build_RoboticsBay_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [all_to_id[Protoss.RoboticsFacility]],
            'research': [],
            'minerals': 150,
            'gas': 150,
            'limit': 0,
            'power': True
        }
    },
    #army
    "Train_Zealot_quick" : {
        'type': ActionTypes.quick,
        'similar': ["TrainWarp_Zealot_pt"],
        'actors': all_to_id[Protoss.Gateway],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 100,
            'gas': 0,
            'limit': 2,
        }
    },
    "Train_Stalker_quick" : {
        'type': ActionTypes.quick,
        'similar': ["TrainWarp_Stalker_pt"],
        'actors': all_to_id[Protoss.Gateway],
        'requirements': {
            'tech': [all_to_id[Protoss.CyberneticsCore]],
            'research': [],
            'minerals': 125,
            'gas': 50,
            'limit': 2,
        }
    },
    "Train_Sentry_quick" : {
        'type': ActionTypes.quick,
        'similar': ["TrainWarp_Sentry_pt"],
        'actors': all_to_id[Protoss.Gateway],
        'requirements': {
            'tech': [all_to_id[Protoss.CyberneticsCore]],
            'research': [],
            'minerals': 50,
            'gas': 100,
            'limit': 2,
        }
    },
    "Train_Adept_quick" : {
        'type': ActionTypes.quick,
        'similar': ["TrainWarp_Adept_pt"],
        'actors': all_to_id[Protoss.Gateway],
        'requirements': {
            'tech': [all_to_id[Protoss.CyberneticsCore]],
            'research': [],
            'minerals': 100,
            'gas': 25,
            'limit': 2,
        }
    },
    "Train_HighTemplar_quick" : {
        'type': ActionTypes.quick,
        'similar': ["TrainWarp_HighTemplar_pt"],
        'actors': all_to_id[Protoss.Gateway],
        'requirements': {
            'tech': [all_to_id[Protoss.TemplarArchive]],
            'research': [],
            'minerals': 50,
            'gas': 150,
            'limit': 2,
        }
    },
    "Train_DarkTemplar_quick" : {
        'type': ActionTypes.quick,
        'similar': ["TrainWarp_DarkTemplar_pt"],
        'actors': all_to_id[Protoss.Gateway],
        'requirements': {
            'tech': [all_to_id[Protoss.DarkShrine]],
            'research': [],
            'minerals': 125,
            'gas': 125,
            'limit': 2,
        }
    },
    "Train_Observer_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.RoboticsFacility],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 25,
            'gas': 75,
            'limit': 1,
        }
    },
    "Train_Immortal_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.RoboticsFacility],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 275,
            'gas': 100,
            'limit': 4,
        }
    },
    "Train_WarpPrism_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.RoboticsFacility],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 250,
            'gas': 0,
            'limit': 2,
        }
    },
    "Train_Colossus_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.RoboticsFacility],
        'requirements': {
            'tech': [all_to_id[Protoss.RoboticsBay]],
            'research': [],
            'minerals': 300,
            'gas': 200,
            'limit': 6,
        }
    },
    "Train_Phoenix_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Stargate],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 150,
            'gas': 100,
            'limit': 2,
        }
    },
    ###################### 200 new patch
    "Train_VoidRay_quick": {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Stargate],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 250,
            'gas': 150,
            'limit': 4,
        }
    },
    "Train_Carrier_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Stargate],
        'requirements': {
            'tech': [all_to_id[Protoss.FleetBeacon]],
            'research': [],
            'minerals': 350,
            'gas': 250,
            'limit': 6,
        }
    },
    "Train_Tempest_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Stargate],
        'requirements': {
            'tech': [all_to_id[Protoss.FleetBeacon]],
            'research': [],
            'minerals': 250,
            'gas': 175,
            'limit': 5,
        }
    },
    "Train_Mothership_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Nexus],
        'requirements': {
            'tech': [all_to_id[Protoss.FleetBeacon]],
            'research': [],
            'minerals': 400,
            'gas': 400,
            'limit': 8,
        }
    },
    "TrainWarp_Zealot_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.WarpGate],
        'requirements': {
            'tech': [],
            'research': [Upgrades.WarpGateResearch],
            'minerals': 100,
            'gas': 0,
            'limit': 2,
            'power': True
        }
    },
    "TrainWarp_Stalker_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.WarpGate],
        'requirements': {
            'tech': [all_to_id[Protoss.CyberneticsCore]],
            'research': [Upgrades.WarpGateResearch],
            'minerals': 125,
            'gas': 50,
            'limit': 2,
            'power': True
        }
    },
    "TrainWarp_Sentry_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.WarpGate],
        'requirements': {
            'tech': [all_to_id[Protoss.CyberneticsCore]],
            'research': [Upgrades.WarpGateResearch],
            'minerals': 50,
            'gas': 100,
            'limit': 2,
            'power': True
        }
    },
    "TrainWarp_Adept_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.WarpGate],
        'requirements': {
            'tech': [all_to_id[Protoss.CyberneticsCore]],
            'research': [Upgrades.WarpGateResearch],
            'minerals': 100,
            'gas': 25,
            'limit': 2,
            'power': True
        }
    },
    "TrainWarp_HighTemplar_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.WarpGate],
        'requirements': {
            'tech': [all_to_id[Protoss.TwilightCouncil]],
            'research': [Upgrades.WarpGateResearch],
            'minerals': 50,
            'gas': 150,
            'limit': 2,
            'power': True
        }
    },
    "TrainWarp_DarkTemplar_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.WarpGate],
        'requirements': {
            'tech': [all_to_id[Protoss.DarkShrine]],
            'research': [Upgrades.WarpGateResearch],
            'minerals': 125,
            'gas': 125,
            'limit': 2,
            'power': True
        }
    },
    "Train_Oracle_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Stargate],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 150,
            'gas': 150,
            'limit': 3,
        }
    },
    "Build_Interceptors_autocast": {
        'type': ActionTypes.autocast,
        'actors': all_to_id[Protoss.Carrier],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 25,
            'gas': 0,
            'limit': 0,
        }
    },
    "Build_Interceptors_quick": {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Carrier],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 25,
            'gas': 0,
            'limit': 0,
        }
    },
    "Morph_Archon_quick": {
        'type': ActionTypes.quick,
        'actors': SpecialTypes.OwnTemplars,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
        
    },
    "Train_Disruptor_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.RoboticsFacility],
        'requirements': {
            'tech': [all_to_id[Protoss.RoboticsBay]],
            'research': [],
            'minerals': 150,
            'gas': 150,
            'limit': 3,
        }
    },
    #pylon
    "Build_Pylon_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 100,
            'gas': 0,
            'limit': 0,
            'power': False
        }
    },
    #defend
    "Build_PhotonCannon_pt": {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 150,
            'gas': 0,
            'limit': 0,
            'power': True
        }
    },
    "Build_ShieldBattery_pt": {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Probe],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 100,
            'gas': 0,
            'limit': 0,
            'power': True
        }
    },
    #move_army
    "Attack_pt" : {
        'type': ActionTypes.pt,
        'actors': SpecialTypes.OwnBattleUnit,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False
        }
    },
    "Attack_unit" : {
        'type': ActionTypes.unit,
        'actors': SpecialTypes.OwnBattleUnit,
        'target': SpecialTypes.Any,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "Move_pt" : {
        'type': ActionTypes.pt,
        'actors': SpecialTypes.OwnBattleUnit,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False
        }
    },
    "Move_unit" : {
        'type': ActionTypes.unit,
        'actors': SpecialTypes.OwnBattleUnit,
        'target': SpecialTypes.Any,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "Patrol_pt" : {
        'type': ActionTypes.pt,
        'actors': SpecialTypes.OwnBattleUnit,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False
        }
    },
    "Patrol_unit" : {
        'type': ActionTypes.unit,
        'actors': SpecialTypes.OwnBattleUnit,
        'target': SpecialTypes.Any,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "Stop_quick" : {
        'type': ActionTypes.quick,
        'actors': SpecialTypes.OwnBattleUnit,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "HoldPosition_quick" : {
        'type': ActionTypes.quick,
        'actors': SpecialTypes.OwnBattleUnit,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    #micro_army
#     "Attack_pt" : {},
#     "Attack_unit" : {},
#     "Move_pt" : {},
#     "Move_unit" : {},
#     "Patrol_pt" : {},
#     "Patrol_unit" : {},
#     "Stop_quick" : {},
#     "HoldPosition_quick" : {},
    #skills
    "Cancel_VoidRayPrismaticAlignment_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.VoidRay],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "Effect_AdeptPhaseShift_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Adept],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False
        }
    },
    "Effect_Blink_Stalker_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Stalker],
        'requirements': {
            'tech': [],
            'research': [Upgrades.Blink],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False
        }
    },
    "Effect_Charge_autocast" : {
        'type': ActionTypes.autocast,
        'actors': all_to_id[Protoss.Zealot],
        'requirements': {
            'tech': [],
            'research': [Upgrades.Charge],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "Effect_Charge_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Zealot],
        'requirements': {
            'tech': [],
            'research': [Upgrades.Charge],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False
        }
    },
    "Effect_Charge_unit" : {
        'type': ActionTypes.unit,
        'actors': all_to_id[Protoss.Zealot],
        'target': SpecialTypes.AnyEnemy,
        'requirements': {
            'tech': [],
            'research': [Upgrades.Charge],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "Effect_Feedback_unit" : {
        'type': ActionTypes.unit,
        'actors': all_to_id[Protoss.HighTemplar],
        'target': SpecialTypes.AnyEnemy,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "Effect_ForceField_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Sentry],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False,
        }
    },
    "Effect_GravitonBeam_unit" : {
        'type': ActionTypes.unit,
        'actors': all_to_id[Protoss.Phoenix],
        'target': SpecialTypes.AnyEnemyUnit,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "Effect_GuardianShield_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Sentry],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    "Effect_MassRecall_Mothership_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Mothership],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False,
        }
    },
    "Effect_MassRecall_StrategicRecall_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Nexus],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False,
        }
    },
    "Effect_PurificationNova_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Disruptor],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False,
        }
    },
    "Effect_PsiStorm_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.HighTemplar],
        'requirements': {
            'tech': [],
            'research': [Upgrades.PsiStorm],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False,
        }
    },
    "Effect_TimeWarp_pt" : {
        'type': ActionTypes.pt,
        'actors': all_to_id[Protoss.Mothership],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
            'power': False,
        }
    },
    "Effect_VoidRayPrismaticAlignment_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.VoidRay],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
    #move_probes
#     "Attack_pt" : {},
#     "Attack_unit" : {},
#     "Move_pt" : {},
#     "Move_unit" : {},
#     "Stop_quick" : {},
#     "HoldPosition_quick" : {},
    #upgrade
    "Research_AdeptResonatingGlaives_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.TwilightCouncil],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 100,
            'gas': 100,
            'limit': 0,
        }
    },
    "Research_Blink_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.TwilightCouncil],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 150,
            'gas': 150,
            'limit': 0,
        }
    },
    "Research_Charge_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.TwilightCouncil],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 100,
            'gas': 100,
            'limit': 0,
        }
    },
    "Research_ExtendedThermalLance_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.RoboticsBay],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 150,
            'gas': 150,
            'limit': 0,
        }
    },
    "Research_GraviticBooster_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.RoboticsBay],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 100,
            'gas': 100,
            'limit': 0,
        }
    },
    "Research_GraviticDrive_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.RoboticsBay],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 100,
            'gas': 100,
            'limit': 0,
        }
    },
    "Research_InterceptorGravitonCatapult_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.FleetBeacon],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 150,
            'gas': 150,
            'limit': 0,
        }
    },
    "Research_PhoenixAnionPulseCrystals_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.FleetBeacon],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 150,
            'gas': 150,
            'limit': 0,
        }
    },
    "Research_ProtossAirArmor_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.CyberneticsCore],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 150,
            'gas': 150,
            'limit': 0,
        }
    },
    "Research_ProtossAirWeapons_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.CyberneticsCore],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 100,
            'gas': 100,
            'limit': 0,
        }
    },
    "Research_ProtossGroundArmor_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Forge],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 100,
            'gas': 100,
            'limit': 0,
        }
    },
    "Research_ProtossGroundWeapons_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Forge],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 100,
            'gas': 100,
            'limit': 0,
        }
    },   
    "Research_ProtossShields_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.Forge],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 150,
            'gas': 150,
            'limit': 0,
        }
    },
    "Research_PsiStorm_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.TemplarArchive],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 200,
            'gas': 200,
            'limit': 0,
        }
    },
    "Research_ShadowStrike_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.DarkShrine],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 200,
            'gas': 200,
            'limit': 0,
        }
    },
    "Research_WarpGate_quick" : {
        'type': ActionTypes.quick,
        'actors': all_to_id[Protoss.CyberneticsCore],
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 50,
            'gas': 50,
            'limit': 0,
        }
    },
    #skip
    "no_op" : {
        'type': ActionTypes.no_arg,
    },
    #cancel
    "Cancel_quick" : {
        'type': ActionTypes.quick,
        'actors': SpecialTypes.AnyOwn,
        'requirements': {
            'tech': [],
            'research': [],
            'minerals': 0,
            'gas': 0,
            'limit': 0,
        }
    },
}

get_graph = {
    'unit': {
        all_to_id[Protoss.Assimilator]: "Build_Assimilator_unit",
        all_to_id[Protoss.AssimilatorRich]: "Build_Assimilator_unit",
        all_to_id[Protoss.CyberneticsCore]: "Build_CyberneticsCore_pt",
        all_to_id[Protoss.DarkShrine]: "Build_DarkShrine_pt",
        all_to_id[Protoss.FleetBeacon]: "Build_FleetBeacon_pt",
        all_to_id[Protoss.Forge]: "Build_Forge_pt",
        all_to_id[Protoss.Gateway]: "Build_Gateway_pt",
        all_to_id[Protoss.Nexus]: "Build_Nexus_pt",
        all_to_id[Protoss.PhotonCannon]: "Build_PhotonCannon_pt",
        all_to_id[Protoss.Pylon]: "Build_Pylon_pt",
        all_to_id[Protoss.RoboticsBay]: "Build_RoboticsBay_pt",
        all_to_id[Protoss.RoboticsFacility]: "Build_RoboticsFacility_pt",
        all_to_id[Protoss.ShieldBattery]: "Build_ShieldBattery_pt",
        all_to_id[Protoss.Stargate]: "Build_Stargate_pt",
        all_to_id[Protoss.TemplarArchive]: "Build_TemplarArchive_pt",
        all_to_id[Protoss.TwilightCouncil]: "Build_TwilightCouncil_pt",
        all_to_id[Protoss.WarpGate]: "Build_Gateway_pt",
        
        all_to_id[Protoss.Adept]: "Train_Adept_quick",
        all_to_id[Protoss.Archon]: "Morph_Archon_quick",
        all_to_id[Protoss.Carrier]: "Train_Carrier_quick",
        all_to_id[Protoss.Colossus]: "Train_Colossus_quick",
        all_to_id[Protoss.DarkTemplar]: "Train_DarkTemplar_quick",
        all_to_id[Protoss.Disruptor]: "Train_Disruptor_quick",
        all_to_id[Protoss.HighTemplar]: "Train_HighTemplar_quick",
        all_to_id[Protoss.Immortal]: "Train_Immortal_quick",
        all_to_id[Protoss.Interceptor]: "Build_Interceptors_autocast",
        all_to_id[Protoss.Mothership]: "Train_Mothership_quick",
        all_to_id[Protoss.Observer]: "Train_Observer_quick",
        all_to_id[Protoss.Oracle]: "Train_Oracle_quick",
        all_to_id[Protoss.Phoenix]: "Train_Phoenix_quick",
        all_to_id[Protoss.Probe]: "Train_Probe_quick",
        all_to_id[Protoss.Sentry]: "Train_Sentry_quick",
        all_to_id[Protoss.Stalker]: "Train_Stalker_quick",
        all_to_id[Protoss.Tempest]: "Train_Tempest_quick",
        all_to_id[Protoss.VoidRay]: "Train_VoidRay_quick",
        all_to_id[Protoss.WarpPrism]: "Train_WarpPrism_quick",
        all_to_id[Protoss.Zealot]: "Train_Zealot_quick",
        
    },
    'upgrade': {
        Upgrades.ResonatingGlaives: "Research_AdeptResonatingGlaives_quick",
        Upgrades.Blink: "Research_Blink_quick",
        Upgrades.WarpGateResearch: "Research_WarpGate_quick",
        Upgrades.Charge: "Research_Charge_quick",
        Upgrades.PsiStorm: "Research_PsiStorm_quick",
        Upgrades.ExtendedThermalLance: "Research_ExtendedThermalLance_quick",
        Upgrades.GraviticBooster: "Research_GraviticBooster_quick",
        Upgrades.GraviticDrive: "Research_GraviticDrive_quick",
        Upgrades.GravitonCatapult: "Research_InterceptorGravitonCatapult_quick",
        Upgrades.AnionPulseCrystals: "Research_PhoenixAnionPulseCrystals_quick",
        Upgrades.ShadowStrike: "Research_ShadowStrike_quick",
    }
}

# PROTOSS_ACTIONS = [
#  'Train_Probe_quick',
#  'Build_Nexus_pt',
#  'Build_Assimilator_unit',
#  'Effect_ChronoBoostEnergyCost_unit',
#  'Harvest_Gather_Probe_unit',
#  'Harvest_Return_Probe_quick',
#  'Build_Gateway_pt',
#  'Build_RoboticsFacility_pt',
#  'Build_Stargate_pt',
#  'Build_Forge_pt',
#  'Build_CyberneticsCore_pt',
#  'Build_TwilightCouncil_pt',
#  'Build_TemplarArchive_pt',
#  'Build_DarkShrine_pt',
#  'Build_FleetBeacon_pt',
#  'Build_RoboticsBay_pt',
#  'Train_Zealot_quick',
#  'Train_Stalker_quick',
#  'Train_Sentry_quick',
#  'Train_Adept_quick',
#  'Train_HighTemplar_quick',
#  'Train_DarkTemplar_quick',
#  'Train_Observer_quick',
#  'Train_Immortal_quick',
#  'Train_WarpPrism_quick',
#  'Train_Colossus_quick',
#  'Train_Phoenix_quick',
#  'Train_VoidRay_quick',
#  'Train_Carrier_quick',
#  'Train_Tempest_quick',
#  'Train_Mothership_quick',
#  'TrainWarp_Zealot_pt',
#  'TrainWarp_Stalker_pt',
#  'TrainWarp_Sentry_pt',
#  'TrainWarp_Adept_pt',
#  'TrainWarp_HighTemplar_pt',
#  'TrainWarp_DarkTemplar_pt',
#  'Train_Oracle_quick',
#  'Build_Interceptors_autocast',
#  'Build_Interceptors_quick',
#  'Morph_Archon_quick',
#  'Train_Disruptor_quick',
#  'Build_Pylon_pt',
#  'Build_PhotonCannon_pt',
#  'Build_ShieldBattery_pt',
#  'Attack_pt',
#  'Attack_unit',
#  'Move_pt',
#  'Move_unit',
#  'Patrol_pt',
#  'Patrol_unit',
#  'Stop_quick',
#  'HoldPosition_quick',
#  'Cancel_VoidRayPrismaticAlignment_quick',
#  'Effect_AdeptPhaseShift_pt',
#  'Effect_Blink_Stalker_pt',
#  'Effect_Charge_autocast',
#  'Effect_Charge_pt',
#  'Effect_Charge_unit',
#  'Effect_Feedback_unit',
#  'Effect_ForceField_pt',
#  'Effect_GravitonBeam_unit',
#  'Effect_GuardianShield_quick',
#  'Effect_MassRecall_Mothership_pt',
#  'Effect_MassRecall_StrategicRecall_pt',
#  'Effect_PurificationNova_pt',
#  'Effect_PsiStorm_pt',
#  'Effect_TimeWarp_pt',
#  'Effect_VoidRayPrismaticAlignment_quick',
#  'Research_AdeptResonatingGlaives_quick',
#  'Research_Blink_quick',
#  'Research_Charge_quick',
#  'Research_ExtendedThermalLance_quick',
#  'Research_GraviticBooster_quick',
#  'Research_GraviticDrive_quick',
#  'Research_InterceptorGravitonCatapult_quick',
#  'Research_PhoenixAnionPulseCrystals_quick',
#  'Research_ProtossAirArmor_quick',
#  'Research_ProtossAirWeapons_quick',
#  'Research_ProtossGroundArmor_quick',
#  'Research_ProtossGroundWeapons_quick',
#  'Research_ProtossShields_quick',
#  'Research_PsiStorm_quick',
#  'Research_ShadowStrike_quick',
#  'Research_WarpGate_quick',
#  'no_op',
#  'Cancel_quick'
# ]

PROTOSS_ACTIONS = [
 'Train_Probe_quick',
 'Build_Nexus_pt',
 'Build_Assimilator_unit',
 'Effect_ChronoBoostEnergyCost_unit',
 'Harvest_Gather_Probe_unit',
 'Harvest_Return_Probe_quick',
 'Build_Gateway_pt',
 'Build_Pylon_pt',
 'Build_CyberneticsCore_pt',
 'Train_Zealot_quick',
 'Train_Stalker_quick',
 'TrainWarp_Zealot_pt',
 'TrainWarp_Stalker_pt',
 'Attack_pt',
 'Move_pt',
 'Research_WarpGate_quick',
 'no_op',
]

n_actions = len(PROTOSS_ACTIONS)
id_to_action = dict(zip(range(len(PROTOSS_ACTIONS)), PROTOSS_ACTIONS))
action_to_id = dict(zip(PROTOSS_ACTIONS, range(len(PROTOSS_ACTIONS))))