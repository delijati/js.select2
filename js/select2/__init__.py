import js.jquery
import fanstatic

library = fanstatic.Library('select2', 'resources')

select2_css = fanstatic.Resource(
    library,
    'css/select2.css',
    minified='js/select2.min.css')

select2 = fanstatic.Resource(
    library, 'js/select2.js',
    minified='js/select2.min.js',
    depends=[select2_css, js.jquery.jquery])

select2_full = fanstatic.Resource(
    library, 'js/select2.full.js',
    minified='js/select2.full.min.js',
    depends=[select2_css, js.jquery.jquery])

locales = {}

select2_ar = locales['ar'] = fanstatic.Resource(
    library, 'js/i18n/ar.js',
    depends=[select2])

select2_az = locales['az'] = fanstatic.Resource(
    library, 'js/i18n/az.js',
    depends=[select2])

select2_bg = locales['bg'] = fanstatic.Resource(
    library, 'js/i18n/bg.js',
    depends=[select2])

select2_ca = locales['ca'] = fanstatic.Resource(
    library, 'js/i18n/ca.js',
    depends=[select2])

select2_cs = locales['cs'] = fanstatic.Resource(
    library, 'js/i18n/cs.js',
    depends=[select2])

select2_da = locales['da'] = fanstatic.Resource(
    library, 'js/i18n/da.js',
    depends=[select2])

select2_de = locales['de'] = fanstatic.Resource(
    library, 'js/i18n/de.js',
    depends=[select2])

select2_el = locales['el'] = fanstatic.Resource(
    library, 'js/i18n/el.js',
    depends=[select2])

select2_en = locales['en'] = fanstatic.Resource(
    library, 'js/i18n/en.js',
    depends=[select2])

select2_es = locales['es'] = fanstatic.Resource(
    library, 'js/i18n/es.js',
    depends=[select2])

select2_et = locales['et'] = fanstatic.Resource(
    library, 'js/i18n/et.js',
    depends=[select2])

select2_eu = locales['eu'] = fanstatic.Resource(
    library, 'js/i18n/eu.js',
    depends=[select2])

select2_fa = locales['fa'] = fanstatic.Resource(
    library, 'js/i18n/fa.js',
    depends=[select2])

select2_fi = locales['fi'] = fanstatic.Resource(
    library, 'js/i18n/fi.js',
    depends=[select2])

select2_fr = locales['fr'] = fanstatic.Resource(
    library, 'js/i18n/fr.js',
    depends=[select2])

select2_gl = locales['gl'] = fanstatic.Resource(
    library, 'js/i18n/gl.js',
    depends=[select2])

select2_he = locales['he'] = fanstatic.Resource(
    library, 'js/i18n/he.js',
    depends=[select2])

select2_hi = locales['hi'] = fanstatic.Resource(
    library, 'js/i18n/hi.js',
    depends=[select2])

select2_hr = locales['hr'] = fanstatic.Resource(
    library, 'js/i18n/hr.js',
    depends=[select2])

select2_hu = locales['hu'] = fanstatic.Resource(
    library, 'js/i18n/hu.js',
    depends=[select2])

select2_hy = locales['hy'] = fanstatic.Resource(
    library, 'js/i18n/hy.js',
    depends=[select2])

select2_id = locales['id'] = fanstatic.Resource(
    library, 'js/i18n/id.js',
    depends=[select2])

select2_is = locales['is'] = fanstatic.Resource(
    library, 'js/i18n/is.js',
    depends=[select2])

select2_it = locales['it'] = fanstatic.Resource(
    library, 'js/i18n/it.js',
    depends=[select2])

select2_ja = locales['ja'] = fanstatic.Resource(
    library, 'js/i18n/ja.js',
    depends=[select2])

select2_km = locales['km'] = fanstatic.Resource(
    library, 'js/i18n/km.js',
    depends=[select2])

select2_ko = locales['ko'] = fanstatic.Resource(
    library, 'js/i18n/ko.js',
    depends=[select2])

select2_lt = locales['lt'] = fanstatic.Resource(
    library, 'js/i18n/lt.js',
    depends=[select2])

select2_lv = locales['lv'] = fanstatic.Resource(
    library, 'js/i18n/lv.js',
    depends=[select2])

select2_mk = locales['mk'] = fanstatic.Resource(
    library, 'js/i18n/mk.js',
    depends=[select2])

select2_ms = locales['ms'] = fanstatic.Resource(
    library, 'js/i18n/ms.js',
    depends=[select2])

select2_nb = locales['nb'] = fanstatic.Resource(
    library, 'js/i18n/nb.js',
    depends=[select2])

select2_nl = locales['nl'] = fanstatic.Resource(
    library, 'js/i18n/nl.js',
    depends=[select2])

select2_pl = locales['pl'] = fanstatic.Resource(
    library, 'js/i18n/pl.js',
    depends=[select2])

select2_pt_BR = locales['pt_BR'] = locales['pt-BR'] = fanstatic.Resource(
    library, 'js/i18n/pt-BR.js',
    depends=[select2])

select2_pt = locales['pt'] = fanstatic.Resource(
    library, 'js/i18n/pt.js',
    depends=[select2])

select2_ro = locales['ro'] = fanstatic.Resource(
    library, 'js/i18n/ro.js',
    depends=[select2])

select2_ru = locales['ru'] = fanstatic.Resource(
    library, 'js/i18n/ru.js',
    depends=[select2])

select2_sk = locales['sk'] = fanstatic.Resource(
    library, 'js/i18n/sk.js',
    depends=[select2])

select2_sl = locales['sl'] = fanstatic.Resource(
    library, 'js/i18n/sl.js',
    depends=[select2])

select2_sr_Cyrl = locales['sr_Cyrl'] = locales['sr-Cyrl'] = fanstatic.Resource(
    library, 'js/i18n/sr-Cyrl.js',
    depends=[select2])

select2_sr = locales['sr'] = fanstatic.Resource(
    library, 'js/i18n/sr.js',
    depends=[select2])

select2_sv = locales['sv'] = fanstatic.Resource(
    library, 'js/i18n/sv.js',
    depends=[select2])

select2_th = locales['th'] = fanstatic.Resource(
    library, 'js/i18n/th.js',
    depends=[select2])

select2_tr = locales['tr'] = fanstatic.Resource(
    library, 'js/i18n/tr.js',
    depends=[select2])

select2_uk = locales['uk'] = fanstatic.Resource(
    library, 'js/i18n/uk.js',
    depends=[select2])

select2_vi = locales['vi'] = fanstatic.Resource(
    library, 'js/i18n/vi.js',
    depends=[select2])

select2_zh_CN = locales['zh_CN'] = locales['zh-CN'] = fanstatic.Resource(
    library, 'js/i18n/zh-CN.js',
    depends=[select2])

select2_zh_TW = locales['zh_TW'] = locales['zh-TW'] = fanstatic.Resource(
    library, 'js/i18n/zh-TW.js',
    depends=[select2])
