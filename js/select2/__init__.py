import fanstatic

library = fanstatic.Library('select2', 'resources')
select2_css = fanstatic.Resource(library, 'select2.css')
select2 = fanstatic.Resource(library, 'select2.js', minified='select2.min.js',
                             depends=[select2_css, ])
select2_ca = fanstatic.Resource(
    library,
    'select2_locale_ca.js',
    depends=[select2])
select2_cs = fanstatic.Resource(
    library,
    'select2_locale_cs.js',
    depends=[select2])
select2_da = fanstatic.Resource(
    library,
    'select2_locale_da.js',
    depends=[select2])
select2_de = fanstatic.Resource(
    library,
    'select2_locale_de.js',
    depends=[select2])
select2_es = fanstatic.Resource(
    library,
    'select2_locale_es.js',
    depends=[select2])
select2_et = fanstatic.Resource(
    library,
    'select2_locale_et.js',
    depends=[select2])
select2_eu = fanstatic.Resource(
    library,
    'select2_locale_eu.js',
    depends=[select2])
select2_fr = fanstatic.Resource(
    library,
    'select2_locale_fr.js',
    depends=[select2])
select2_gl = fanstatic.Resource(
    library,
    'select2_locale_gl.js',
    depends=[select2])
select2_he = fanstatic.Resource(
    library,
    'select2_locale_he.js',
    depends=[select2])
select2_hr = fanstatic.Resource(
    library,
    'select2_locale_hr.js',
    depends=[select2])
select2_hu = fanstatic.Resource(
    library,
    'select2_locale_hu.js',
    depends=[select2])
select2_is = fanstatic.Resource(
    library,
    'select2_locale_is.js',
    depends=[select2])
select2_it = fanstatic.Resource(
    library,
    'select2_locale_it.js',
    depends=[select2])
select2_ja = fanstatic.Resource(
    library,
    'select2_locale_ja.js',
    depends=[select2])
select2_lt = fanstatic.Resource(
    library,
    'select2_locale_lt.js',
    depends=[select2])
select2_lv = fanstatic.Resource(
    library,
    'select2_locale_lv.js',
    depends=[select2])
select2_mk = fanstatic.Resource(
    library,
    'select2_locale_mk.js',
    depends=[select2])
select2_nl = fanstatic.Resource(
    library,
    'select2_locale_nl.js',
    depends=[select2])
select2_no = fanstatic.Resource(
    library,
    'select2_locale_no.js',
    depends=[select2])
select2_pl = fanstatic.Resource(
    library,
    'select2_locale_pl.js',
    depends=[select2])
select2_pt_BR = fanstatic.Resource(
    library,
    'select2_locale_pt-BR.js',
    depends=[select2])
select2_pt_PT = fanstatic.Resource(
    library,
    'select2_locale_pt-PT.js',
    depends=[select2])
select2_ro = fanstatic.Resource(
    library,
    'select2_locale_ro.js',
    depends=[select2])
select2_ru = fanstatic.Resource(
    library,
    'select2_locale_ru.js',
    depends=[select2])
select2_sk = fanstatic.Resource(
    library,
    'select2_locale_sk.js',
    depends=[select2])
select2_sv = fanstatic.Resource(
    library,
    'select2_locale_sv.js',
    depends=[select2])
select2_tr = fanstatic.Resource(
    library,
    'select2_locale_tr.js',
    depends=[select2])
select2_ua = fanstatic.Resource(
    library,
    'select2_locale_ua.js',
    depends=[select2])
select2_vi = fanstatic.Resource(
    library,
    'select2_locale_vi.js',
    depends=[select2])
select2_zh_CN = fanstatic.Resource(
    library,
    'select2_locale_zh-CN.js',
    depends=[select2])
select2_zh_TW = fanstatic.Resource(
    library,
    'select2_locale_zh-TW.js',
    depends=[select2])
