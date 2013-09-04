from django import template

register = template.Library()

class RawNode(template.Node):
    def __init__(self, text):
        self.text = text

    def render(self, context):
        return self.text

@register.tag
def raw(parser, token):
    text = []
    while 1:
        token = parser.tokens.pop(0)
        if token.contents == 'endraw':
            break
        if token.token_type == template.TOKEN_VAR:
            text.append('{{ ')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('{%')
        text.append(token.contents)
        if token.token_type == template.TOKEN_VAR:
            text.append(' }}')
        elif token.token_type == template.TOKEN_BLOCK:
            if not text[-1].startswith('='):
                text[-1:-1] = [' ']
            text.append(' %}')
    return RawNode(''.join(text))
