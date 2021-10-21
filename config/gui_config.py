from qgis.PyQt.QtCore import QCoreApplication

try:
    from asistente_ladm_col.config.keys.common import *
    from asistente_ladm_col.lib.model_registry import LADMColModel
except ModuleNotFoundError:
    pass

from .general_config import ACTION_ETL_ADD_ON_ENVIRONMENT

gui_config = {
        MAIN_MENU: [{  # List of main menus
            WIDGET_TYPE: MENU,
            WIDGET_NAME: "LADM-COL AM&BIENTE",
            OBJECT_NAME: MENU_LADM_COL_OBJECTNAME,
            ACTIONS: [
                {
                    WIDGET_TYPE: MENU,
                    WIDGET_NAME: QCoreApplication.translate("AsistenteLADMCOLPlugin", "Data management"),
                    OBJECT_NAME: "ladm_col_data_management_menu",
                    ICON: DATA_MANAGEMENT_ICON,
                    ACTIONS: [
                        ACTION_SCHEMA_IMPORT,
                        ACTION_IMPORT_DATA,
                        ACTION_EXPORT_DATA
                    ]
                },
                ACTION_LOAD_LAYERS,
                SEPARATOR,
                ACTION_CHECK_QUALITY_RULES,
                ACTION_PARCEL_QUERY,
                {
                    WIDGET_TYPE: MENU,
                    WIDGET_NAME: QCoreApplication.translate("AsistenteLADMCOLPlugin", "Reports"),
                    OBJECT_NAME: MENU_REPORTS_OBJECTNAME,
                    ICON: REPORTS_ICON,
                    ACTIONS: [
                        ACTION_REPORT_ANNEX_17,
                        ACTION_REPORT_ANT
                    ]
                },
                ACTION_ETL_ADD_ON_ENVIRONMENT,
                SEPARATOR,
                ACTION_SETTINGS,
                SEPARATOR,
                ACTION_HELP,
                ACTION_ABOUT
            ]
        }], TOOLBAR: [{  # List of toolbars
            WIDGET_NAME: QCoreApplication.translate("AsistenteLADMCOLPlugin", "LADM-COL tools"),
            OBJECT_NAME: 'ladm_col_toolbar',
            ACTIONS: [
                ACTION_LOAD_LAYERS,
                ACTION_ETL_ADD_ON_ENVIRONMENT,
                SEPARATOR,
                ACTION_SETTINGS
            ]
        }]
    }