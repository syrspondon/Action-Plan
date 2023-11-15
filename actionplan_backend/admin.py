from django.contrib import admin


from .models import BRCA1Breast, BRCA1Ovarine, BRCA2Breast, BRCA2Ovarine, PALB2Ovarine, PALB2Breast

admin.site.register(BRCA1Breast)
admin.site.register(BRCA1Ovarine)
admin.site.register(BRCA2Breast)
admin.site.register(BRCA2Ovarine)
admin.site.register(PALB2Breast)
admin.site.register(PALB2Ovarine)