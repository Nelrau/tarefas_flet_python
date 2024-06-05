import flet as ft

def main(page: ft.Page):
    page.title = 'Pagina'
    # tema
    page.theme_mode = ft.ThemeMode.DARK
    nome = ft.TextField(hint_text='Qual seu nome?')
    page.add(ft.Text('Cadastro:', color=ft.colors.BLUE, size=20), nome,
             ft.Text(nome.value)
             ) 
    page.update()

ft.app(target=main)