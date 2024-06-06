from flet import *

def main(page: Page):
    page.title = 'Pagina'
    page.window_width = 300
    page.window_height = 600
    page.scroll= True
    page.window_maximized = False
    page.update()
    page.appbar = AppBar(
        leading = PopupMenuButton(Icon(icons.LIST_SHARP), items=[PopupMenuItem('logar')]),  
        title=Text('Lista de cadastro', color='#0055ff', width=190),
        bgcolor='#001188',
        actions= [
                 PopupMenuButton(
                        items=[PopupMenuItem('Save'),
                               PopupMenuItem('Atualizar'),
                               PopupMenuItem('Sair')                               
                        ],
                 ),
                    
                 ],
                 )
    
    # tema
    page.theme_mode = ThemeMode.DARK
    nome = TextField(hint_text='Qual seu nome?', bgcolor='#000000')
    email = TextField(hint_text= 'Email:', bgcolor='#000000')
    page.add( Text('Nome:', color=colors.BLUE, size=20),
             nome,
             Text('Email:'),
             email)
    
    page.update()

app(target=main, )