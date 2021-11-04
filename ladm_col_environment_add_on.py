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
from functools import partial
import webbrowser

from qgis.PyQt.QtCore import (QObject,
                              QCoreApplication)
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import (Qgis,
                       QgsProcessingException)
from qgis.utils import plugins

import processing

try:
    from asistente_ladm_col.config.general_config import HELP_URL
    from asistente_ladm_col.lib.context import Context
    from asistente_ladm_col.utils.decorators import (db_connection_required,
                                                     qgis_model_baker_required)
except ModuleNotFoundError:
    pass

from .config.model_config import ModelConfig
from .config.role_config import RoleConfig
from .config.general_config import *
from .config.translator import install_qt_translator


class LADMCOLEnvironmentAddOn(QObject):

    def __init__(self, iface):
        QObject.__init__(self)
        self.iface = iface
        self.ladmcol = None  # To hold instance of Asistente LADM-COL

        self.__translator = install_qt_translator()

    def initGui(self):
        self.__initialize_ladm_col_plugin()

    def __initialize_ladm_col_plugin(self):
        if LADM_COL_PLUGIN_ID not in plugins:
            # Let the user know that Asistente LADM-COL is required
            self.iface.messageBar().pushMessage("LADMCOLEnvironmentAddOn",
                                                WARNING_DEPENDENCY_MISSING,
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
        self.__run_etl_action = QAction(QIcon(ACTION_ETL_ICON_PATH),
                                        QCoreApplication.translate("LADMCOLEnvironmentAddOn", "Run 2nd law ETL"),
                                        self.ladmcol.main_window)
        self.__help_action = QAction(QIcon(ACTION_HELP_ICON_PATH),
                                     QCoreApplication.translate("LADMCOLEnvironmentAddOn", "Help"),
                                     self.ladmcol.main_window)

        # Signal-slot connections
        self.__run_etl_action.triggered.connect(partial(self.__run_etl, Context()))
        self.__help_action.triggered.connect(self.__show_help)

        self.ladmcol.gui_builder.register_actions({ACTION_ETL_ADD_ON_ENVIRONMENT: self.__run_etl_action,
                                                   ACTION_HELP_ADD_ON_ENVIRONMENT: self.__help_action})
        self.ladmcol.add_actions_to_db_engines([ACTION_ETL_ADD_ON_ENVIRONMENT,
                                                ACTION_HELP_ADD_ON_ENVIRONMENT],
                                               ['pg', 'gpkg'])

    @qgis_model_baker_required
    @db_connection_required
    def __run_etl(self, *args):
        self.ladmcol.logger.info(__name__, "Running ETL model...")

        db = self.ladmcol.get_db_connection()
        layers = {db.names.L2DA_DRR_T: None,
                  db.names.L2DA_UAB_COMPENSATION_T: None,
                  db.names.L2DA_UAB_RESERVE_T: None,
                  db.names.L2DA_UAB_SUBTRACTION_T: None,
                  db.names.L2DA_UE_COMPENSATION_T: None,
                  db.names.L2DA_UE_RESERVE_T: None,
                  db.names.L2DA_UE_SUBTRACTION_T: None,
                  db.names.COL_RRRSOURCE_T: None,
                  db.names.COL_UEBAUNIT_T: None,
                  db.names.MA_ADMINISTRATIVE_SOURCE_T: None,
                  db.names.MA_PARTY_T: None}

        self.ladmcol.app.core.get_layers(db, layers, load=True)

        if not layers:
            return

        params = {'ENTRADAReservaLey2da': None,
                  'ENTRADASustraccion': None,
                  'EntradaCompensacin': None,
                  'SALIDAFuenteAdministrativa': layers[db.names.MA_ADMINISTRATIVE_SOURCE_T],
                  'SALIDAL2DARRR': layers[db.names.L2DA_DRR_T],
                  'SALIDAL2DAUABCompensacion': layers[db.names.L2DA_UAB_COMPENSATION_T],
                  'SALIDAL2DAUABReserva': layers[db.names.L2DA_UAB_RESERVE_T],
                  'SALIDAL2DAUABSustraccion': layers[db.names.L2DA_UAB_SUBTRACTION_T],
                  'SALIDAL2DAUECompensacion': layers[db.names.L2DA_UE_COMPENSATION_T],
                  'SALIDAL2DAUEReserva': layers[db.names.L2DA_UE_RESERVE_T],
                  'SALIDAL2DAUESustraccion': layers[db.names.L2DA_UE_SUBTRACTION_T],
                  'SALIDAMAInteresado': layers[db.names.MA_PARTY_T],
                  'SALIDAcolrrrfuente': layers[db.names.COL_RRRSOURCE_T],
                  'SALIDAcoluebaunit': layers[db.names.COL_UEBAUNIT_T]}

        try:
            processing.execAlgorithmDialog("model:ETL Ambiente ley 2da", params)
        except QgsProcessingException as e:
            self.ladmcol.logger.warning_msg(__name__, QCoreApplication.translate("LADMCOLEnvironmentAddOn",
                                                                                 "There was an error running the ETL model. See the QGIS log for details."))
            self.ladmcol.logger.critical(__name__, QCoreApplication.translate("LADMCOLEnvironmentAddOn",
                                                                              "Error running the ETL model. Details: {}").format(
                str(e)))
            return

        self.ladmcol.logger.info(__name__, "ETL model finished!")

    def __show_help(self):
        webbrowser.open("{}/{}".format(HELP_URL, HELP_ENVIRONMENT_URL_PART))

    def __unload_ladm_col_plugin(self):
        # Called when the LADM-COL plugin is uninstalled, informing us
        # we have to reset all member vars that deal with the plugin
        self.ladmcol = None

    def unload(self):
        if self.ladmcol:  # In case LADM-COL has not been uninstalled yet...
            self.ladmcol.role_registry.unregister_role(ENVIRONMENT_ROLE_KEY)
            self.ladmcol.model_registry.unregister_model(ENVIRONMENT_MODEL_KEY, True)
