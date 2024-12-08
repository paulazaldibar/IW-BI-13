from django.contrib import admin
from .models import PromotorMusical, Festival, Interprete, Reseña
from django.utils.html import format_html

# Register your models here.

admin.site.register(PromotorMusical)
admin.site.register(Festival)
admin.site.register(Interprete)
admin.site.register(Reseña)


PROMOTOR_COLORS = {
    'Live Nation': '#DC143C',  # Rojo
    'AEG Presents': '#4dc493',  # Verde
    'OCESA CIE': '#1A66CC',  # Azul
    'MAMA & Company': '#FF7F50',  # Naranja
    'SFX Entertainment': '#FF69B4',  # Rosa
}

# Desregistrar el modelo que ya estaba registrado
admin.site.unregister(Interprete)
# Registrar nuevamente con la configuración personalizada
@admin.register(Interprete)
class InterpreteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero')
    ordering = ['nombre']  # Ordenado alfabéticamente
    search_fields = ('nombre',) # Añade el panel de búsqueda
    list_display_links = ('nombre',) # Añade el link correspondiente a cada nombre
    list_filter = ('genero',) # Permite filtrar los datos, en este caso los filtra por el género
    list_per_page = 10 # Establece 10 objetos por página
    exclude = ('nombre',) # No permite modificar este atributo


# Desregistrar el modelo que ya estaba registrado
admin.site.unregister(Festival)
# Registrar nuevamente con la configuración personalizada
@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ('color_festival', 'ubicacion', 'color_promotor')
    ordering = ['nombre']  # Ordenado alfabéticamente
    search_fields = ('nombre', 'ubicacion', 'promotor')  # Añade el panel de búsqueda
    list_editable = ('ubicacion',)  # Permite modificar la ubicación si fuese necesario
    list_display_links = ('color_festival',)  # Ahora el enlace apunta a un campo existente
    list_filter = ('ubicacion', 'promotor')  # Permite filtrar por ubicación y promotor
    list_per_page = 10  # Establece 10 objetos por página
    exclude = ('nombre',)  # No permite modificar este atributo

    def color_festival(self, obj):
        color = PROMOTOR_COLORS.get(obj.promotor.nombre, '#000000')  # Si no está en el diccionario, usa negro
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            obj.nombre
        )

    def color_promotor(self, obj):
        color = PROMOTOR_COLORS.get(obj.promotor.nombre, '#000000')  # Si no está en el diccionario, usa negro
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            obj.promotor.nombre
        )

    color_festival.short_description = 'Festival (Color)'
    color_promotor.short_description = 'Promotor (Color)'


# Desregistrar el modelo que ya estaba registrado
admin.site.unregister(PromotorMusical)
# Registrar nuevamente con la configuración personalizada
@admin.register(PromotorMusical)
class PromotorMusicalAdmin(admin.ModelAdmin):
    list_display = ('colored_nombre', 'pais_origen', 'descripcion')
    ordering = ['nombre']  # Ordenado alfabéticamente
    search_fields = ('nombre', 'pais_origen')  # Añade el panel de búsqueda
    list_editable = ('descripcion',)  # Permite modificar la descripción si fuese necesario
    list_display_links = ('colored_nombre',)  # Añade el link correspondiente al nombre coloreado
    list_filter = ('pais_origen',)  # Permite filtrar los datos por país de origen
    list_per_page = 10  # Establece 10 objetos por página
    exclude = ('nombre', 'pais_origen')  # No permite modificar estos atributos

    def colored_nombre(self, obj):
        """Aplica un color personalizado al nombre del promotor."""
        color = PROMOTOR_COLORS.get(obj.nombre, '#000000')  # Por defecto negro si no está definido
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            obj.nombre
        )

    colored_nombre.short_description = 'Nombre (Color)'


# Desregistrar el modelo que ya estaba registrado
admin.site.unregister(Reseña)
# Registrar nuevamente con la configuración personalizada
@admin.register(Reseña)
class reseñaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'festival', 'fecha', 'calificacion')
    ordering = ['-calificacion']  # Ordenado por calificación descendiente
    search_fields = ('nombre', 'festival', 'calificacion') # Añade el panel de búsqueda
    list_display_links = ('nombre',) # Añade el link correspondiente a cada nombre
    list_filter = ('calificacion',) # Permite filtrar los datos, en este caso los filtra por la calificación
    list_per_page = 10 # Establece 10 objetos por página
    exclude = ('nombre', 'fecha', 'festival') # No permite modificar este atributo