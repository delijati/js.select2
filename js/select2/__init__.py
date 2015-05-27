import js.jquery
import fanstatic

library = fanstatic.Library('select2', 'resources')

select2 = fanstatic.Group([
    fanstatic.Resource(library, 'js/select2.js',
        minified='js/select2.min.js',
        depends=[js.jquery.jquery]),
    fanstatic.Resource(library, 'css/select2.css')
    ])

select2_az = fanstatic.Resource(
    library, 'js/i18n/az.js',
    depends=[select2])

select2_bg = fanstatic.Resource(
    library, 'js/i18n/bg.js',
    depends=[select2])

select2_ca = fanstatic.Resource(
    library, 'js/i18n/ca.js',
    depends=[select2])

select2_cs = fanstatic.Resource(
    library, 'js/i18n/cs.js',
    depends=[select2])

select2_da = fanstatic.Resource(
    library, 'js/i18n/da.js',
    depends=[select2])

select2_de = fanstatic.Resource(
    library, 'js/i18n/de.js',
    depends=[select2])

select2_en = fanstatic.Resource(
    library, 'js/i18n/en.js',
    depends=[select2])

select2_es = fanstatic.Resource(
    library, 'js/i18n/es.js',
    depends=[select2])

select2_et = fanstatic.Resource(
    library, 'js/i18n/et.js',
    depends=[select2])

select2_eu = fanstatic.Resource(
    library, 'js/i18n/eu.js',
    depends=[select2])

select2_fa = fanstatic.Resource(
    library, 'js/i18n/fa.js',
    depends=[select2])

select2_fi = fanstatic.Resource(
    library, 'js/i18n/fi.js',
    depends=[select2])

select2_fr = fanstatic.Resource(
    library, 'js/i18n/fr.js',
    depends=[select2])

select2_gl = fanstatic.Resource(
    library, 'js/i18n/gl.js',
    depends=[select2])

select2_he = fanstatic.Resource(
    library, 'js/i18n/he.js',
    depends=[select2])

select2_hi = fanstatic.Resource(
    library, 'js/i18n/hi.js',
    depends=[select2])

select2_hr = fanstatic.Resource(
    library, 'js/i18n/hr.js',
    depends=[select2])

select2_hu = fanstatic.Resource(
    library, 'js/i18n/hu.js',
    depends=[select2])

select2_id = fanstatic.Resource(
    library, 'js/i18n/id.js',
    depends=[select2])

select2_is = fanstatic.Resource(
    library, 'js/i18n/is.js',
    depends=[select2])

select2_it = fanstatic.Resource(
    library, 'js/i18n/it.js',
    depends=[select2])

select2_ko = fanstatic.Resource(
    library, 'js/i18n/ko.js',
    depends=[select2])

select2_lt = fanstatic.Resource(
    library, 'js/i18n/lt.js',
    depends=[select2])

select2_lv = fanstatic.Resource(
    library, 'js/i18n/lv.js',
    depends=[select2])

select2_mk = fanstatic.Resource(
    library, 'js/i18n/mk.js',
    depends=[select2])

select2_nb = fanstatic.Resource(
    library, 'js/i18n/nb.js',
    depends=[select2])

select2_nl = fanstatic.Resource(
    library, 'js/i18n/nl.js',
    depends=[select2])

select2_pl = fanstatic.Resource(
    library, 'js/i18n/pl.js',
    depends=[select2])

select2_pt_BR = fanstatic.Resource(
    library, 'js/i18n/pt-BR.js',
    depends=[select2])

select2_pt = fanstatic.Resource(
    library, 'js/i18n/pt.js',
    depends=[select2])

select2_ro = fanstatic.Resource(
    library, 'js/i18n/ro.js',
    depends=[select2])

select2_ru = fanstatic.Resource(
    library, 'js/i18n/ru.js',
    depends=[select2])

select2_sk = fanstatic.Resource(
    library, 'js/i18n/sk.js',
    depends=[select2])

select2_sr = fanstatic.Resource(
    library, 'js/i18n/sr.js',
    depends=[select2])

select2_sv = fanstatic.Resource(
    library, 'js/i18n/sv.js',
    depends=[select2])

select2_th = fanstatic.Resource(
    library, 'js/i18n/th.js',
    depends=[select2])

select2_tr = fanstatic.Resource(
    library, 'js/i18n/tr.js',
    depends=[select2])

select2_uk = fanstatic.Resource(
    library, 'js/i18n/uk.js',
    depends=[select2])

select2_vi = fanstatic.Resource(
    library, 'js/i18n/vi.js',
    depends=[select2])

select2_zh_CN = fanstatic.Resource(
    library, 'js/i18n/zh-CN.js',
    depends=[select2])

select2_zh_TW = fanstatic.Resource(
    library, 'js/i18n/zh-TW.js',
    depends=[select2])