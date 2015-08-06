from django import template

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


@register.inclusion_tag("home/navbar/navbar.html", takes_context=True)
def display_navbar(context):
    parent = get_site_root(context)
    calling_page = context['self']
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = menuitem.get_children().live().in_menu().exists()
        menuitem.active = (calling_page.url.startswith(menuitem.url) if calling_page else False)

    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        "request": context['request']
    }


@register.inclusion_tag('home/navbar/navbar_dropdown.html', takes_context=True)
def display_navbar_dropdown(context, parent):
    menuitems_children = parent.get_children().live().in_menu()

    return {
        "parent": parent,
        "menuitems_children": menuitems_children,
        "request": context['request'],
    }


@register.inclusion_tag('home/navbar/sidemenu.html', takes_context=True)
def display_sidemenu(context, parent):
    current_page = context['self']
    has_children = parent.get_children().live().in_menu().exists()
    menuitems_children = parent.get_children().live().in_menu()

    return {
        "current_page": current_page,
        "parent": parent,
        "children": menuitems_children,
        "has_children": has_children,
        "request": context['request']
    }


@register.inclusion_tag('home/include/subsection.html', takes_context=True)
def display_subsection(context):
    current_page = context['self']

    return {
        "current_page": current_page,
    }
