from asistente_ladm_col.config.general_config import DEFAULT_DATASET_NAME
from asistente_ladm_col.config.keys.ili2db_keys import (ILI2DB_SCHEMAIMPORT,
                                                        ILI2DB_IMPORT,
                                                        ILI2DB_CREATE_BASKET_COL_KEY,
                                                        ILI2DB_DATASET)
from qgis.PyQt.QtCore import QCoreApplication

try:
    from asistente_ladm_col.config.keys.common import *
    from asistente_ladm_col.lib.model_registry import LADMColModel
except ModuleNotFoundError:
    pass

from .config import (SECOND_LAW_MODEL_KEY,
                     NATIONAL_PROTECTED_FOREST_MODEL_KEY,
                     PRODUCER_PROTECTED_FOREST_MODEL_KEY,
                     ENVIRONMENT_MODEL_KEY,
                     MODELS_DIR)


class ModelConfig:

    def __init__(self):
        pass

    @staticmethod
    def get_model_instances():
        models = [
            LADMColModel(SECOND_LAW_MODEL_KEY, {
                MODEL_ALIAS: QCoreApplication.translate("ModelConfig", "Second law model"),
                MODEL_IS_SUPPORTED: True,
                MODEL_SUPPORTED_VERSION: "0.1",
                MODEL_HIDDEN_BY_DEFAULT: False,
                MODEL_CHECKED_BY_DEFAULT: True,
                MODEL_MAPPING: dict(),
                MODEL_DIR: MODELS_DIR,
                MODEL_ILI2DB_PARAMETERS: {
                    ILI2DB_SCHEMAIMPORT: [(ILI2DB_CREATE_BASKET_COL_KEY, None)],
                    ILI2DB_IMPORT: [(ILI2DB_DATASET, DEFAULT_DATASET_NAME)]
                },
                MODEL_BASKET_INFO: {
                    MODEL_BASKET_TOPIC_NAME: "Ley_2da_V0_1.Ley_2da",
                    MODEL_BASKET_TOPIC_NAME_PREFERRED: True  # Prefer this topic name over others in the same DB
                }
            }),
            LADMColModel(NATIONAL_PROTECTED_FOREST_MODEL_KEY, {
                MODEL_ALIAS: QCoreApplication.translate("ModelConfig", "National protected forest model"),
                MODEL_IS_SUPPORTED: True,
                MODEL_SUPPORTED_VERSION: "0.1",
                MODEL_HIDDEN_BY_DEFAULT: False,
                MODEL_CHECKED_BY_DEFAULT: False,
                MODEL_MAPPING: dict(),
                MODEL_DIR: MODELS_DIR
            }),
            LADMColModel(PRODUCER_PROTECTED_FOREST_MODEL_KEY, {
                MODEL_ALIAS: QCoreApplication.translate("ModelConfig", "Producer protected forest model"),
                MODEL_IS_SUPPORTED: True,
                MODEL_SUPPORTED_VERSION: "0.1",
                MODEL_HIDDEN_BY_DEFAULT: False,
                MODEL_CHECKED_BY_DEFAULT: False,
                MODEL_MAPPING: dict(),
                MODEL_DIR: MODELS_DIR
            }),
            LADMColModel(ENVIRONMENT_MODEL_KEY, {
                MODEL_ALIAS: QCoreApplication.translate("ModelConfig", "Environment model"),
                MODEL_IS_SUPPORTED: True,
                MODEL_SUPPORTED_VERSION: "0.1",
                MODEL_HIDDEN_BY_DEFAULT: False,
                MODEL_CHECKED_BY_DEFAULT: True,
                MODEL_MAPPING: dict(),
                MODEL_DIR: MODELS_DIR,
                MODEL_ILI2DB_PARAMETERS: {
                    ILI2DB_SCHEMAIMPORT: [(ILI2DB_CREATE_BASKET_COL_KEY, None)]
                }
            }),
        ]

        return models
