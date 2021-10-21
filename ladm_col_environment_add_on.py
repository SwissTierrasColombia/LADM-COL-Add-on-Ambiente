"""
/***************************************************************************
                               LADM-COL Add-on
                             --------------------
        begin         : 2021-10-05
        git sha       : :%H$
        copyright     : (C) 2021 by Germán Carrillo (SwissTierras Colombia)
        email         : gcarrillo@linuxmail.org
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License v3.0 as          *
 *   published by the Free Software Foundation.                            *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import (Qgis,
                       QgsProcessingException)
from qgis.utils import plugins

import processing

from .config.model_config import ModelConfig
from .config.role_config import RoleConfig
from .config.general_config import *


class LADMCOLEnvironmentAddOn:

    def __init__(self, iface):
        self.iface = iface
        self.ladmcol = None  # To hold instance of Asistente LADM-COL

    def initGui(self):
        self.__initialize_ladm_col_plugin()

    def __initialize_ladm_col_plugin(self):
        if LADM_COL_PLUGIN_ID not in plugins:
            # Let the user know that Asistente LADM-COL is required
            self.iface.messageBar().pushMessage("LADMColAddOn",
                                                QCoreApplication.translate("LADMColAddOn", WARNING_DEPENDENCY_MISSING),
                                                Qgis.Warning)
            return
    
        self.ladmcol = plugins[LADM_COL_PLUGIN_ID]
        self.ladmcol.plugin_unloaded.connect(self.__unload_ladm_col_plugin)

        # Setup additional functionality
        self.__create_actions()

        # Register environment models
        models = ModelConfig.get_model_instances()
        for model in models:
            self.ladmcol.model_registry.register_model(model)

        # Register new role for environmental sector
        role_key, role_config = RoleConfig.get_role_configuration()
        self.ladmcol.role_registry.register_role(role_key, role_config, activate_role=True)

        # Register ETL
        self.ladmcol.app.processing.register_add_on_processing_models(PROCESSING_MODELS_DIR)

    def __create_actions(self):
        self.__run_etl_action = QAction(QIcon(ACTION_ETL_PATH),
                                        QCoreApplication.translate("LADMCOLEnvironmentAddOn", "Run 2nd law ETL"),
                                        self.ladmcol.main_window)

        # Signal-slot connections
        self.__run_etl_action.triggered.connect(self.__run_etl)

        self.ladmcol.gui_builder.register_actions({ACTION_ETL_ADD_ON_ENVIRONMENT: self.__run_etl_action})
        self.ladmcol.add_actions_to_db_engines([ACTION_ETL_ADD_ON_ENVIRONMENT], ['pg', 'gpkg'])

    def __run_etl(self):
        self.ladmcol.logger.info(__name__, "Running ETL model...")

        try:
            processing.execAlgorithmDialog("model:ETL Ambiente ley 2da", dict())
        except QgsProcessingException as e:
            self.ladmcol.logger.warning_msg(__name__, QCoreApplication.translate("LADMCOLEnvironmentAddOn",
                                                                                 "There was an error running the ETL model. See the QGIS log for details."))
            self.ladmcol.logger.critical(__name__, QCoreApplication.translate("LADMCOLEnvironmentAddOn",
                                                                              "Error running the ETL model. Details: {}").format(
                str(e)))
            return

        self.ladmcol.logger.info(__name__, "ETL model finished!")

    def __unload_ladm_col_plugin(self):
        # Called when the LADM-COL plugin is uninstalled, informing us
        # we have to reset all member vars that deal with the plugin
        self.ladmcol = None

    def unload(self):
        if self.ladmcol:  # In case LADM-COL has not been uninstalled yet...
            self.ladmcol.role_registry.unregister_role(ENVIRONMENT_ROLE_KEY)
            self.ladmcol.model_registry.unregister_model(ENVIRONMENT_MODEL_KEY, True)
