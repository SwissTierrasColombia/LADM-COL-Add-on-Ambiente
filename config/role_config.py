from qgis.PyQt.QtCore import QCoreApplication

try:
    from asistente_ladm_col.config.keys.common import *
    from asistente_ladm_col.config.gui.gui_config import GUI_Config
except ModuleNotFoundError:
    pass

from .general_config import *
from .gui_config import gui_config


class RoleConfig:

    def __init__(self):
        pass

    @staticmethod
    def get_role_configuration():
        default_gui_config = GUI_Config().get_gui_dict(DEFAULT_GUI)
        default_gui_config[MAIN_MENU][0][WIDGET_NAME] = "LADM-COL AM&BIENTE"

        return ENVIRONMENT_ROLE_KEY, {
            ROLE_NAME: QCoreApplication.translate("RoleConfig", "Environment role"),
            ROLE_DESCRIPTION: QCoreApplication.translate("RoleConfig",
                                                         "The <b>environment</b> role is in charge of managing information of territorial objects for the environment sector."),
            ROLE_MODELS: {ROLE_SUPPORTED_MODELS: [LADMNames.LADM_COL_MODEL_KEY,
                                                  LADMNames.ISO19107_MODEL_KEY,
                                                  SECOND_LAW_MODEL_KEY,
                                                  NATIONAL_PROTECTED_FOREST_MODEL_KEY,
                                                  PRODUCER_PROTECTED_FOREST_MODEL_KEY,
                                                  ENVIRONMENT_MODEL_KEY],
                          ROLE_HIDDEN_MODELS: [LADMNames.LADM_COL_MODEL_KEY,
                                               LADMNames.ISO19107_MODEL_KEY],
                          ROLE_CHECKED_MODELS: [SECOND_LAW_MODEL_KEY,
                                                ENVIRONMENT_MODEL_KEY]},
            ROLE_ACTIONS: [ACTION_ETL_ADD_ON_ENVIRONMENT],
            ROLE_QUALITY_RULES: [],
            ROLE_GUI_CONFIG: {TEMPLATE_GUI: gui_config, DEFAULT_GUI: default_gui_config},
            ROLE_NEEDS_AUTOMATIC_VALUE_FOR_BASKETS: True
        }
