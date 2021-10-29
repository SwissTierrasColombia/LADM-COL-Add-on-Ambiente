import os.path

from qgis.PyQt.QtCore import QCoreApplication

# Add-on
ADD_ON_PLUGIN_NAME = "LADM-COL Add-on Ambiente"
ADD_ON_PLUGIN_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(ADD_ON_PLUGIN_DIR, "../resources")
IMAGES_DIR = os.path.join(RESOURCES_DIR, "images")
MODELS_DIR = os.path.join(RESOURCES_DIR, "models")
PROCESSING_MODELS_DIR = os.path.join(RESOURCES_DIR, "processing", "models")
ENVIRONMENT_ROLE_KEY = "ENVIRONMENT_ROLE"
ACTION_ETL_ADD_ON_ENVIRONMENT = "action_etl_add_on_environment"

SECOND_LAW_MODEL_KEY = "Ley_2da"
NATIONAL_PROTECTED_FOREST_MODEL_KEY = "Reserva_Forestal_Protectora_Nacional"
PRODUCER_PROTECTED_FOREST_MODEL_KEY = "Reserva_Forestal_Protectora_Productora"
ENVIRONMENT_MODEL_KEY = "Ambiente"

# Icons
ACTION_ICON_PATH = os.path.join(IMAGES_DIR, 'reports.svg')
ACTION_ETL_PATH = os.path.join(IMAGES_DIR, 'etl.png')

# LADM-COL plugin
LADM_COL_PLUGIN_ID = "asistente_ladm_col"
LADM_COL_PLUGIN_NAME = "Asistente LADM-COL"
LADM_COL_REQUIRED_VERSION = "3.2.0-beta-1"

WARNING_DEPENDENCY_MISSING = QCoreApplication.translate("LADMCOLEnvironmentAddOn",
                                                        "The '{}' plugin requires '{}' version {}. Please install the required version and then reload the add-on.").format(
    ADD_ON_PLUGIN_NAME, LADM_COL_PLUGIN_NAME, LADM_COL_REQUIRED_VERSION)
