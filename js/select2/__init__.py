import fanstatic

library = fanstatic.Library('select2', 'resources')
select2_css = fanstatic.Resource(library, 'select2.css')
select2 = fanstatic.Resource(library, 'select2.js', minified='select2.min.js',
                             depends=[select2_css, ])
