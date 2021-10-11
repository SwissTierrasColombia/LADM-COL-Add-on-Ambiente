from qgis.PyQt.QtCore import QCoreApplication

try:
    from asistente_ladm_col.config.keys.common import *
    from asistente_ladm_col.config.gui.gui_config import GUI_Config
except ModuleNotFoundError:
    pass

from .config import *


class RoleConfig:

    def __init__(self):
        pass

    @staticmethod
    def get_role_configuration():
        gui_config = GUI_Config().get_gui_dict()
        gui_config[MAIN_MENU][0][WIDGET_NAME] = "LADM-COL AM&BIENTE"

        default_gui_config = GUI_Config().get_gui_dict(DEFAULT_GUI)
        default_gui_config[MAIN_MENU][0][WIDGET_NAME] = "LADM-COL AM&BIENTE"

        return ENVIRONMENT_ROLE_KEY, {
            ROLE_NAME: QCoreApplication.translate("RoleConfig", "Environment user"),
            ROLE_DESCRIPTION: QCoreApplication.translate("RoleConfig",
                                                         "The environment user is in charge of ..."),
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
            ROLE_ACTIONS: [
                ACTION_ST_LOGIN,
                ACTION_ST_LOGOUT],
            ROLE_QUALITY_RULES: [],
            ROLE_GUI_CONFIG: {TEMPLATE_GUI: gui_config, DEFAULT_GUI: default_gui_config},
            ROLE_NEEDS_AUTOMATIC_VALUE_FOR_BASKETS: True
        }
