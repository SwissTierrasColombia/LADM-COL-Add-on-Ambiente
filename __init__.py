"""
/***************************************************************************
                               LADM-COL Add-on
                             --------------------
        begin         : 2021-07-27
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
from qgis.core import Qgis
from qgis.utils import pluginMetadata

from .config.general_config import (ADD_ON_PLUGIN_NAME,
                                    LADM_COL_PLUGIN_ID,
                                    LADM_COL_REQUIRED_VERSION,
                                    WARNING_DEPENDENCY_MISSING)


def classFactory(iface):
    # First make sure Asistente LADM-COL is installed
    ladmcol_version = pluginMetadata(LADM_COL_PLUGIN_ID, 'version')
    if ladmcol_version != '__error__':  # LADM-COL plugin found
        if ladmcol_version == LADM_COL_REQUIRED_VERSION:  # TODO: improve way to check minimum dependency
            from .ladm_col_environment_add_on import LADMCOLEnvironmentAddOn
            return LADMCOLEnvironmentAddOn(iface)

    iface.messageBar().pushMessage(ADD_ON_PLUGIN_NAME,
                                   WARNING_DEPENDENCY_MISSING,
                                   Qgis.Warning, 0)
    from mock import Mock
    return Mock()
