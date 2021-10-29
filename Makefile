
all: i18n/LADM-COL-Add-on-Ambiente_es.qm

update_translations: i18n/LADM-COL-Add-on-Ambiente_locale.ts

clean:
	rm -f i18n/LADM-COL-Add-on-Ambiente_es.qm
	rm -f *.pyc *~

i18n/LADM-COL-Add-on-Ambiente_es.qm: i18n/LADM-COL-Add-on-Ambiente_es.ts
	lrelease i18n/LADM-COL-Add-on-Ambiente.pro

i18n/LADM-COL-Add-on-Ambiente_locale.ts: i18n/LADM-COL-Add-on-Ambiente.pro
	lupdate i18n/LADM-COL-Add-on-Ambiente.pro
