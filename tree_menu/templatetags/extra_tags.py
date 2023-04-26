from django import template

from ..services import get_menu_from_db, build_tree

register = template.Library()


@register.simple_tag
def draw_recursive_nested_list(menu_tree: list) -> str:
    """Recursive function for drawing nested list from given menu tree.
    :param menu_tree: Menu tree
    :return: Nested list as string.
    """
    result = '<ul>'
    for item in menu_tree:
        if item is not None:
            result += f'<li><a href="?menu_item={item["url"]}">{item["name"]}</a>'
            result += draw_recursive_nested_list(item['children'])
            result += '</li>'
    result += '</ul>'
    return result


@register.inclusion_tag('include/tree_menu.html')
def draw_menu(request, menu_name: str):
    """Returns menu tree for given menu name.
    :param request: Request object
    :param menu_name: Menu name
    :return: Menu tree for given name.
    """
    return {'menu': build_tree(get_menu_from_db(menu_name), request.GET.get('menu_item', None))}
