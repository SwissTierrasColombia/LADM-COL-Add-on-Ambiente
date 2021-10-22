from copy import deepcopy

from asistente_ladm_col.config.query_names import QueryNames

from .general_config import (SECOND_LAW_MODEL_KEY,
                             ENVIRONMENT_MODEL_KEY)


class DBMappingConfig:
    """
    Stores the mapping of DB object (tables/fields) names given by INTERLIS,
    for each model supported by default by the Asistente LADM-COL.

    A model mapping could be an empty dict, but it is better to set a proper
    mapping for two reasons:

    1) They allow us to abstract names for any DB engine (note that the same
       table will probably have different names depending on the DB engine,
       think about capital case vs. lower case or variations).
    2) They allow us to check that some variables that we'll use in several
       modules are properly set and are actually found in the DB. For
       instance, we can easily detect if a user changes the underlying .ili
       model and pretends it to be a known model.

    How to set a mapping:

    1. You need the ilinames that are present in the DB (ili2db metadata tables). You can do this by code,
       just get a DBConnector object and call its get_db_mapping() method, like this:

       a = qgis.utils.plugins['asistente_ladm_col']
       a.get_db_connection().get_db_mapping()

    2. Choose variable names you'll use throughout the code. Example: "LC_MYTABLE_T".
        We suggest you to use these suffixes: t for tables, d for domains, f for fields.
        If your variable points to an application or extended model, use its prefix.

    3. You can map both tables and fields. It depends on what you'll use in your code.

    4. Note that fields coming for relations have a special notation for their ilinames,
       namely, they include a ".." separator. Don't worry, get_db_mapping() will give you
       the proper iliname you need to use, also in the case of fields coming for relations.
    """
    __DB_MAPPING_CONFIG = {
        SECOND_LAW_MODEL_KEY: {
            "Ley_2da.Ley_2da.L2DA_DRR": {
                QueryNames.VARIABLE_NAME: "L2DA_DRR_T", QueryNames.FIELDS_DICT: {}
            },
            "Ley_2da.Ley_2da.L2DA_UAB_Compensacion": {
                QueryNames.VARIABLE_NAME: "L2DA_UAB_COMPENSATION_T", QueryNames.FIELDS_DICT: {}
            },
            "Ley_2da.Ley_2da.L2DA_UAB_Reserva": {
                QueryNames.VARIABLE_NAME: "L2DA_UAB_RESERVE_T", QueryNames.FIELDS_DICT: {}
            },
            "Ley_2da.Ley_2da.L2DA_UAB_Sustraccion": {
                QueryNames.VARIABLE_NAME: "L2DA_UAB_SUBTRACTION_T", QueryNames.FIELDS_DICT: {}
            },
            "Ley_2da.Ley_2da.L2DA_UE_Compensacion": {
                QueryNames.VARIABLE_NAME: "L2DA_UE_COMPENSATION_T", QueryNames.FIELDS_DICT: {}
            },
            "Ley_2da.Ley_2da.L2DA_UE_Reserva": {
                QueryNames.VARIABLE_NAME: "L2DA_UE_RESERVE_T", QueryNames.FIELDS_DICT: {}
            },
            "Ley_2da.Ley_2da.L2DA_UE_Sustraccion": {
                QueryNames.VARIABLE_NAME: "L2DA_UE_SUBTRACTION_T", QueryNames.FIELDS_DICT: {}
            }
        },
        ENVIRONMENT_MODEL_KEY: {
            "LADM_COL.LADM_Nucleo.col_rrrFuente": {
                QueryNames.VARIABLE_NAME: "COL_RRRSOURCE_T", QueryNames.FIELDS_DICT: {}
            },
            "LADM_COL.LADM_Nucleo.col_ueBaunit": {
                QueryNames.VARIABLE_NAME: "COL_UEBAUNIT_T", QueryNames.FIELDS_DICT: {},
            },
            "Ambiente.Ambiente.MA_FuenteAdministrativa": {
                QueryNames.VARIABLE_NAME: "MA_ADMINISTRATIVE_SOURCE_T", QueryNames.FIELDS_DICT: {},
            },
            "Ambiente.Ambiente.MA_Interesado": {
                QueryNames.VARIABLE_NAME: "MA_PARTY_T", QueryNames.FIELDS_DICT: {},
            },
        }
    }

    def get_model_mapping(self, model_key):
        # Return a deepcopy of the mapping to protect the original config
        return deepcopy(self.__DB_MAPPING_CONFIG.get(model_key, dict()))
