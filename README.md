# LADM-COL Add-on Ambiente

Plugin de QGIS para extender el [Asistente LADM-COL](https://github.com/SwissTierrasColombia/Asistente-LADM-COL) con funcionalidades para el sector ambiente.


En su versión actual (0.2), el Add-on de Ambiente agrega al Asistente LADM-COL:

 + Un nuevo rol llamado `Rol Ambiente`.

 + Cuatro modelos LADM-COL para el sector Ambiente (versión preliminar).
  
   + [Ambiente_V0_1](https://github.com/SwissTierrasColombia/LADM-COL-Add-on-Ambiente/blob/master/resources/models/Ambiente_V20210601.ili).
   + [Ley_2da_V0_1](https://github.com/SwissTierrasColombia/LADM-COL-Add-on-Ambiente/blob/master/resources/models/Reservas_V20210601.ili#L9).
   + [Reserva_Forestal_Protectora_Nacional_V0_1](https://github.com/SwissTierrasColombia/LADM-COL-Add-on-Ambiente/blob/master/resources/models/Reservas_V20210601.ili#L353).
   + [Reserva_Forestal_Protectora_Productora_V0_1](https://github.com/SwissTierrasColombia/LADM-COL-Add-on-Ambiente/blob/master/resources/models/Reservas_V20210601.ili#L616).

 + Una nueva interfaz: menú `LADM-COL Ambiente` para el `rol Ambiente`.

 + Una herramienta ETL denominada `ETL Ley 2da`.

   ![image](https://user-images.githubusercontent.com/652785/139499633-eefb67b4-44ef-448b-a3ad-9bbb6fa4336b.png)

## Instalación

Si usas QGIS > v3.22.0:
  
  1. [Activa los complementos experimentales](https://docs.qgis.org/3.16/es/docs/user_manual/plugins/plugins.html#the-settings-tab). 
  2. Instala el `LADM-COL-Add-on-Ambiente` (versión experimental)


Si usas QGIS <= v3.22.0:

  1. [Activa los complementos experimentales](https://docs.qgis.org/3.16/es/docs/user_manual/plugins/plugins.html#the-settings-tab). 
  2. Instala primero el `Asistente LADM-COL` 3.2.0-beta-1 (versión experimental).
  3. Instala luego el `LADM-COL-Add-on-Ambiente` (versión experimental).

