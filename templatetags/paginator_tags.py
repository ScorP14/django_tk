from django import template
from django.core.paginator import Paginator

register = template.Library()

Paginator
@register.simple_tag
def get_proper_elided_page_range(pag, number, on_each_side=2, on_ends=1):
    if pag.num_pages <= 9:
        return range(1, pag.num_pages+1)
    paginator_nums_list = list(pag.get_elided_page_range(number, on_each_side=on_each_side, on_ends=on_ends))
    middle_index = len(paginator_nums_list) // 2
    for index, char in enumerate(paginator_nums_list):
        if char == pag.ELLIPSIS:
            if index < middle_index:
                paginator_nums_list[index] = paginator_nums_list[middle_index] // 2
            else:
                paginator_nums_list[index] = (paginator_nums_list[-1] + paginator_nums_list[middle_index]) // 2 + 1
    return paginator_nums_list




